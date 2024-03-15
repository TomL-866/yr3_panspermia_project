const P: f64 = 1.8;
const M_MOON: f64 = 7.34767309e22;
const M_LOW: f64 = 10.0;
const M_UPP: f64 = M_MOON;
const M_EARTH: f64 = 5.97216787e24;

/// This function generates a mass distribution of rocks,
/// rocks being the type of rock 'Oumuamua is thought to be.
///
/// Args:
///    u (f64): Random number between 0 and 1
///
/// Returns:
///   f64: Rock mass in kg
pub fn rock_dist(u: f64) -> f64 {
    (u * M_UPP.powf(1.0 - P) + (1.0 - u) * M_LOW.powf(1.0 - P)).powf(1.0 / (1.0 - P))
}
