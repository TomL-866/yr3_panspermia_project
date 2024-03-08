extern crate pyo3;
extern crate rand;

mod quantile_function;
mod rock_dist;

use pyo3::prelude::*;
use rand::{rngs::ThreadRng, Rng};

const RUNS: usize = 1_000_000;

#[pyfunction]
pub fn get_stellar_masses() -> Vec<f64> {
    let mut rng: ThreadRng = rand::thread_rng(); // Quantile function takes in a random number from 0 to 1 (uniform distribution)

    let stellar_mass: Vec<f64> = (0..RUNS)
    .map(|_| quantile_function::quantile_func(rng.gen_range(0.0..1.0)))
    .collect();

    stellar_mass // SI units
}

#[pyfunction]
pub fn get_rock_masses() -> Vec<f64>{
    let mut rng: ThreadRng = rand::thread_rng(); 

    let rock_mass: Vec<f64> = (0..RUNS)
    .map(|_| rock_dist::rock_dist(rng.gen_range(0.0..1.0)))
    .collect();

    println!("!! FIX ROCK MASS EQUATION !!");
    rock_mass // SI units
}

#[pymodule]
fn rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(get_stellar_masses, m)?)?;
    m.add_function(wrap_pyfunction!(get_rock_masses, m)?)?;
    Ok(())
}
