import time 
from functools import lru_cache

# 1. The FAST version (with cache)
@lru_cache(maxsize=None)
def fibo_fast(num):
    if num == 0 or num == 1:
        return num
    return fibo_fast(num-1) + fibo_fast(num-2)

# 2. The SLOW version (without cache)
def fibo_slow(num):
    if num == 0 or num == 1:
        return num
    return fibo_slow(num-1) + fibo_slow(num-2)

n = int(input("Enter the number to calculate: "))

# Timing the FAST version
start = time.perf_counter()
result_fast = fibo_fast(n)
end = time.perf_counter()
print(f"Cached Result: {result_fast} | Time: {end - start:.8f}s")

# Timing the SLOW version (Warning: don't go above n=35!)
start = time.perf_counter()
result_slow = fibo_slow(n)
end = time.perf_counter()
print(f"Slow Result: {result_slow} | Time: {end - start:.8f}s")

