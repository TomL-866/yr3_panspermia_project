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
    let m_r = M_EARTH; // m_R in Adams and Napier 2022
    let m_2 = M_UPP;
    let a = (2.0 - P) * m_r / m_2.powf(2.0 - P); // A in Adams and Napier 2022

    a * (u * M_UPP.powf(1.0 - P) + (1.0 - u) * M_LOW.powf(1.0 - P)).powf(1.0 / (1.0 - P))

    // TODO: Fix this equation

    // Ideas for fix:
    // Cumulative distribution function (CDF) of the power law is
    // A / (2 - P) * m**(-(P - 1))
    // see https://compphys.notes.dmaitre.phyip3.dur.ac.uk/lectures/lecture-5/probability-distributions/
    // see https://websites.umich.edu/~mejn/courses/2006/cmplxsys899/powerlaws.pdf for CDF
}
