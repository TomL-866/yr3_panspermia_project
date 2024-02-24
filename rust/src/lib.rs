extern crate pyo3;
extern crate rand;

mod quantile_function;

use pyo3::prelude::*;
use rand::{rngs::ThreadRng, Rng};

const RUNS: usize = 1_000_000;

#[pyfunction]
fn get_stellar_masses() -> Vec<f64> {
    let mut rng: ThreadRng = rand::thread_rng(); // Quantile function takes in a random number from 0 to 1 (uniform distribution)
    let mut stellar_mass: Vec<f64> = vec![0.0; RUNS];

    for i in 0..RUNS {
        stellar_mass[i] = quantile_function::quantile_func(rng.gen_range(0.0..1.0));
    }

    stellar_mass // SI units
}

#[pymodule]
fn rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(get_stellar_masses, m)?)?;
    Ok(())
}
