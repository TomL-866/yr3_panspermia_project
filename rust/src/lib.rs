extern crate pyo3;
extern crate rand;

mod quantile_function;
mod rock_dist;
mod monte_carlo;
use monte_carlo::Key;

use pyo3::prelude::*;
use rand::{rngs::ThreadRng, Rng};
use std::collections::HashMap;

const RUNS: usize = 100_000;
const AU_TO_M: f64 = 1.496e11;

// Converting my custom Key struct to a Python float
use pyo3::types::PyFloat;

impl IntoPy<PyObject> for Key {
    fn into_py(self, py: Python) -> PyObject {
        PyFloat::new(py, self.value).into() 
    }
}

// Functions begin
#[pyfunction]
pub fn get_stellar_masses() -> Vec<f64> {
    let mut rng: ThreadRng = rand::thread_rng(); // Quantile function takes in a random number from 0 to 1 (uniform distribution)

    let stellar_mass: Vec<f64> = (0..RUNS)
        .map(|_| quantile_function::quantile_func(rng.gen_range(0.0..1.0)))
        .collect();

    stellar_mass // SI units
}

#[pyfunction]
pub fn get_rock_masses() -> Vec<f64> {
    let mut rng: ThreadRng = rand::thread_rng();

    let rock_mass: Vec<f64> = (0..RUNS)
        .map(|_| rock_dist::rock_dist(rng.gen_range(0.0..1.0)))
        .collect();

    rock_mass // SI units
}

#[pyfunction]
pub fn return_coll_times() -> (HashMap<Key, HashMap<Key, f64>>, HashMap<Key, HashMap<Key, HashMap<Key, f64>>>, HashMap<Key, HashMap<Key, HashMap<Key, f64>>>) {
    let mut n_o: Vec<f64> = vec![0.01, 0.05, 0.1, 0.5, 1.0];
    let mut v_o: Vec<f64> = vec![1.0, 5.0, 10.0, 20.0, 30.0];

    // unit conversions
    for i in 0..n_o.len() {
        n_o[i] /= AU_TO_M.powi(3);
    }
    for i in 0..v_o.len() {
        v_o[i] *= 1_000.0;
    }

    let stellar_masses: Vec<f64> = get_stellar_masses();

    monte_carlo::get_coll_times(n_o, v_o, stellar_masses)
}

#[pymodule]
fn rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(get_stellar_masses, m)?)?;
    m.add_function(wrap_pyfunction!(get_rock_masses, m)?)?;
    m.add_function(wrap_pyfunction!(return_coll_times, m)?)?;
    Ok(())
}
