# In Haskell me do it like diz:
#
# sieve (p:xs) = [x | x <- xs, x `mod` p /= 0]
# primes = map head $ iterate sieve [2..]
#
# or with unfoldr (import from Data.List)
# primes = map head $ unfoldr (\x -> Just (x, sieve x)) [2..]

from itertools import tee, count

def sieve(xs):
    xs, ys = tee(xs)
    p = next(ys)
    return xs, (y for y in ys if y % p != 0)

def iterate_sieve():
    xs = count(2) 
    while True:
        ps, xs = sieve(xs) 
        yield ps 

def primes():
    return map(lambda xs: next(xs), iterate_sieve())
