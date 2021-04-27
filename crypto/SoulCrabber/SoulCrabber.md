1. See rust
2. Panic
3. The seed is static => Random generator is not so random anymore. It'll generate the same 'random' numbers every time it runs. Everytime StdRng::gen() runs it gives a new result, but it's predictable
4. Still uses XOR
5. Go to Rust Playground and print the XOR key with this
```rust
use rand::{Rng,SeedableRng};
use rand::rngs::StdRng;

fn get_rng() -> StdRng {
    let seed = 13371337;
    return StdRng::seed_from_u64(seed);
}

fn main() -> std::io::Result<()> {
    let mut rng = get_rng();
    for i in 0..29 {
        print!("{}", format!("{:02x}", rng.gen::<u8>()));
    }
    Ok(())
}
```
6. Grab the ciphertext from out.txt and XOR it with the key generated above
7. CyberChef ftw.
8. CHTB{mem0ry_s4f3_crypt0_f41l} (i think this is it, the discord chat's a mess sorry about that)