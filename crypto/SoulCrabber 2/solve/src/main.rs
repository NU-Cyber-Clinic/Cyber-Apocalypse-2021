use rand::{Rng,SeedableRng};
use rand::rngs::StdRng;

fn get_rng(seed : u64) -> StdRng {
    return StdRng::seed_from_u64(seed);
}

fn main() -> std::io::Result<()> {
    let seed_start = 1587040332;
    let seed_final = 1618576333;
    for seed in seed_start..seed_final{
        let mut rng = get_rng(seed);
        for _z in 0..41{
            print!("{:02x}", rng.gen::<u8>());
        }
        print!("\n")
    }
    Ok(())
}