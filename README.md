# Quantum Cryptography

## Shor's Algorithm

Please do not actually use classical_shor.py to try to factorize large numbers, it is a really inefficient way of factorization for a classical computer.

```bash
python3 -m timeit -s 'import classical_shor' 'classical_shor.solve(80609)'
100 loops, best of 3: 3.11 msec per loop ((3.11 * 10^-3) seconds)
```

pure_factorizatrion.py is a much better algorithm for finding primes on a classical computer.

```bash
python3 -m timeit -s 'import pure_factorization' 'pure_factorization.factorize(80609)'
100000 loops, best of 3: 3.56 usec per loop ((3.56 * 10^-6) seconds)
```

* classical_shor.py
  * Shor's algorithm implemented purely with classical algorithm
* pure_factorization.py
  * Classical way of finding prime factors

## Grover's Algorithm

Reduces the time complexity of finding the input to a black box(Oracle) function that produces a particular output from O(N) to O(sqrt(N)).