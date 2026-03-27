# Algorithm name
Sieve of Sundaram

## Author
Pablo Redruello (2026-03-26)

## Algorithm Description
The Sieve of Sundaram is a deterministic algorithm for finding all prime numbers up to a specified integer. It works by identifying numbers of the form i + j + 2ij, where 1 ≤ i ≤ j and i + j + 2ij ≤ m, with m = (n-1)/2. Any natural number k that is NOT in this form will correspond to a prime number p such that p = 2k + 1. This algorithm effectively filters out composite odd numbers, leaving only the indices that generate primes.

## Model Used to Create the Base Code
GPT-5.3

### Prompt
Could you give me the algorithm for the Sundaram sieve in Java?

## Obfuscated Version
manually obfuscated