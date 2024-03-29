use std::collections::HashMap;
use std::f64::consts::PI;
use std::hash::{Hash, Hasher};
use std::cmp::PartialEq;
use std::cmp::Eq;

#[derive(PartialEq, Debug, Copy, Clone)]
pub struct Key {
    pub value: f64,
}

impl Eq for Key {}

impl Hash for Key {
    fn hash<H: Hasher>(&self, state: &mut H) {
        self.value.to_bits().hash(state);
    }
}

const AU_TO_M: f64 = 1.496e11;
const M_SUN: f64 = 1.989e30;
const G: f64 = 6.67430e-11;

pub fn get_coll_times(n_o: Vec<f64>, v_o: Vec<f64>, stellar_masses: Vec<f64>) -> (HashMap<Key, HashMap<Key, f64>>, HashMap<Key, HashMap<Key, HashMap<Key, f64>>>, HashMap<Key, HashMap<Key, HashMap<Key, f64>>>) {
    let mut coll_times_earth = HashMap::new();
    let mut coll_times_disk_side = HashMap::new();
    let mut coll_times_disk_top = HashMap::new();
    
    for k in 0..stellar_masses.len() {
        let stellar_mass_key = Key { value: stellar_masses[k] };
    
        for i in 0..n_o.len() {
            let n_o_key = Key { value: n_o[i] };
    
            for j in 0..v_o.len() {
                let v_o_key = Key { value: v_o[j] };
    
                coll_times_earth
                    .entry(n_o_key)
                    .or_insert_with(HashMap::new)
                    .insert(v_o_key, t_coll_earth(n_o[i], v_o[j]));
    
                coll_times_disk_side
                    .entry(stellar_mass_key)
                    .or_insert_with(HashMap::new)
                    .entry(n_o_key)
                    .or_insert_with(HashMap::new)
                    .insert(v_o_key, t_coll_disk_side(n_o[i], v_o[j], stellar_masses[k]));
    
                coll_times_disk_top
                    .entry(stellar_mass_key)
                    .or_insert_with(HashMap::new)
                    .entry(n_o_key)
                    .or_insert_with(HashMap::new)
                    .insert(v_o_key, t_coll_disk_top(n_o[i], v_o[j], stellar_masses[k]));
            }
        }
    }

    (coll_times_earth, coll_times_disk_side, coll_times_disk_top)
}

fn t_coll_earth(n_o: f64, v_o: f64) -> f64 {
    let r_earth = 6.371e6; // in meters
    let m_earth = 5.972e24; // in kilograms

    let v_esc = f64::sqrt(2.0 * G * m_earth / r_earth);
    let c = PI * r_earth.powi(2) * (1.0 + v_esc.powi(2) / v_o.powi(2)); 

    1.0 / (n_o * c * v_o)
}

fn t_coll_disk_side(n_o: f64, v_o: f64, stellar_mass: f64) -> f64 {
    let disk_mass: f64 = 0.1 * stellar_mass;
    let disk_radius: f64 = 200.0 * AU_TO_M * (stellar_mass / M_SUN).powf(0.3);
    let csa_sideview: f64 = 0.1 * AU_TO_M * disk_radius;

    let v_esc = f64::sqrt(2.0 * G * (stellar_mass + disk_mass) / disk_radius);

    1.0 / (n_o * csa_sideview * (1.0 + v_esc.powi(2) / v_o.powi(2)) * v_o)
}

fn t_coll_disk_top(n_o: f64, v_o: f64, stellar_mass: f64) -> f64 {
    let disk_mass: f64 = 0.1 * stellar_mass;
    let disk_radius: f64 = 200.0 * AU_TO_M * (stellar_mass / M_SUN).powf(0.3);
    let csa_topview: f64 = PI * disk_radius.powi(2);

    let v_esc = f64::sqrt(2.0 * G * (stellar_mass + disk_mass) / disk_radius);

    1.0 / (n_o * csa_topview * (1.0 + v_esc.powi(2) / v_o.powi(2)) * v_o)
}