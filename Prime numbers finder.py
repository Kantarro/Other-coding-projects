# 2 methods finding prime numbers: 1) Sieve of Eratosthenes 2) finding
# if it has factors of previous terms (finding up to √x)

# Finding all prime numbers between 1 and 1 000 000

# 1) Sieve of Eratosthenes

# method i), less efficient
n = list(range(2, 101)) # 1 is not prime nor composite
index = 0 # start at index 0 for prime 2

# stop while loop until n[index] is last item of list n
while n[index] != n[-1]:
    for k in n[:]: # iterate through a copy of n, since remove(k) shifts the original list n, tampers with iteration
        if k > n[index] and k % n[index] == 0: # 2 is the base case for n[index]
            n.remove(k) # remove multiples of n[index] greater than itself
    index += 1 # the next n[index] will be prime and repeat the process w.r.t. it
print(n) # all primes less than 100

# But no need to wait until prime n[index] == n[-1]. Just test until the prime is at most the
# square root of the maximum number of the list, S. Once n[index] <= S, numbers greater than
# n[index] are composite XOR prime. If they are composite, they would've already been removed
# if they have prime factors less than n[index], else they are going to be removed in current
# iteration. If n[index] == S, then all composite numbers greater than S except S^2 is removed
# (since they have prime factors less than S. Not possible if they have prime factors only greater than
# S since their product will go out of range, i.e., be greater than max(n)). Often times n[index] < S
# and when index += 1, n[index] > S, which will terminate while loop (n[index] == S rare case).

# method ii), more efficient
from math import sqrt
n = list(range(2, 122)) # example where the largest number is the square of a prime (121 = 11^2)
S = sqrt(max(n))
index = 0 # start at index 0 for prime 2

# stop while loop until n[index] is last item of list n
while n[index] <= S:
    for k in n[:]: # iterate through a copy of n, since remove(k) shifts the original list n, tampers with iteration
        if k > n[index] and k % n[index] == 0: # 2 is the base case for n[index]
            n.remove(k) # remove multiples of n[index] greater than itself
    index += 1 # the next n[index] will be prime (as it isn't a multiple of the previous prime) and repeat the process w.r.t. it
print(n)

# 2)
