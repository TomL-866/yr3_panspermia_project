/// This module contains functions representing equations in https://doi.org/10.1093/mnras/sts479

const MU: f64 = 0.2; // Equation assumes we're working in solar masses
const ALPHA: f64 = 2.3;
const BETA: f64 = 1.4;
const UPPER_MASS_LIMIT: f64 = 50.0; // Equation assumes we're working in solar masses
const LOWER_MASS_LIMIT: f64 = 0.1; // Equation assumes we're working in solar masses

/// This function replicates the quantile function,
/// Equation 4 in Table 1 of https://doi.org/10.1093/mnras/sts479.
/// Values of constants are taken directly from the paper,
/// except from the upper and lower mass limits.
///
/// Args:
///   u: A f64 value, a random number between 0 and 1.
///
/// Returns:
///  f64: The stellar mass value associated with the given u value (in solar masses).
///
pub fn quantile_func(u: f64) -> f64 {
    MU * ((u * (auxiliary_func(UPPER_MASS_LIMIT) - auxiliary_func(LOWER_MASS_LIMIT))
        + auxiliary_func(LOWER_MASS_LIMIT))
    .powf(1.0 / (1.0 - BETA))
        - 1.0)
        .powf(1.0 / (1.0 - ALPHA))
}

/// This function replicates the auxiliary function,
/// Equation 1 in Table 1 of https://doi.org/10.1093/mnras/sts479.
/// Values of constants are taken directly from the paper.
///
/// Args:
///  stellar_mass: A f64 value, the stellar mass value.
///
/// Returns:
///  f64: The value of the auxiliary function for the given stellar mass.
///
fn auxiliary_func(stellar_mass: f64) -> f64 {
    (1.0 + (stellar_mass / MU).powf(1.0 - ALPHA)).powf(1.0 - BETA)
}
