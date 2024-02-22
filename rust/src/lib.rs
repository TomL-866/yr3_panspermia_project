extern crate pyo3;
extern crate rand;

mod quantile_function;

use pyo3::prelude::*;
use rand::{rngs::ThreadRng, Rng};

const RUNS: usize = 1_000_000;
const SOLAR_MASS: f64 = 1.98840987e30; // SI units

#[pyfunction]
fn get_stellar_masses() -> Vec<f64> {
    // u is a random number. We need 'RUNS' number of these
    let mut rng: ThreadRng = rand::thread_rng();
    let mut u: Vec<f64> = vec![0.0; RUNS]; // initialize vector with size RUNS

    for i in 0..RUNS {
        u[i] = rng.gen_range(0.0..1.0);
    } // Populate u vector with random values

    // We need to calculate stellar masses for each value of u.
    let mut stellar_mass: Vec<f64> = vec![0.0; RUNS]; // initialize vector with size RUNS

    for i in 0..RUNS {
        stellar_mass[i] = quantile_function::quantile_func(u[i]) * SOLAR_MASS;
    } // Populate stellar_mass vector with values in SI units

    stellar_mass
}

#[pymodule]
fn rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(get_stellar_masses, m)?)?;
    Ok(())
}
