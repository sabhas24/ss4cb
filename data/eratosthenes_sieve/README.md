# Eratosthenes Sieve

## Algorithm name

Sieve of Eratosthenes

## Author

Victor Manuel Montini (2026-03-23)

## Algorithm description

The Sieve of Eratosthenes is an ancient algorithm for finding all prime numbers up to a given limit. It works by iteratively marking the multiples of each prime number as composite, starting from 2. The algorithm begins with a boolean array initialized to true for all indices, then sets indices 0 and 1 to false. For each number starting at 2, if it is still marked true, all of its multiples (starting from its square) are marked false. After processing all numbers up to the square root of the limit, the indices that remain true correspond to prime numbers.

## Model used to create the base code

claude-sonnet-4-6

### Prompt

```
Write a Python function called eratosthenes_sieve that receives a number `limit` and returns a list of all prime numbers up to and including that limit, using the Sieve of Eratosthenes algorithm. Use descriptive English variable names.
```

## Obfuscated version

manually obfuscated
