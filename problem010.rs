use std::num::sqrt;

fn is_prime(n: int) -> bool {
    let upper_limit = sqrt(n as f64) + 1.0;
    for i in range(2, upper_limit as int) {
        if n % i == 0 {
            return false;
        }
    }
    return true;
}

fn main() {
    let mut primes = ~[2, 3, 5, 7];

    let mut i = 8;
    while i < 2000000 {
        if is_prime(i) {
            primes.push(i);
        }
        i = i + 1;
    }

    let mut total = 0;
    for &x in primes.iter() {
        total += x
    }

    println!("{}", total);
}
