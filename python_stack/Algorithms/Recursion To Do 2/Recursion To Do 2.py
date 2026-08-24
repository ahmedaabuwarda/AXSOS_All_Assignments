import math


def fib(num):

    num = math.trunc(num)

    if num <= 0:
        return 0

    if num <= 1:
        return 1

    return fib(num - 1) + fib(num - 2)

print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))


def rTrib(num):
    num = max(0, math.trunc(num))
    
    # Base
    if num == 0 or num == 1:
        return 0
    if num == 2:
        return 1
        
    return rTrib(num - 1) + rTrib(num - 2) + rTrib(num - 3)

print(rTrib(2))
print(rTrib(3))
print(rTrib(4))
print(rTrib(5))


def ackermann(num1, num2):
  if num1 == 0:
    return num2 + 1
  
  if num2 == 0:
    return ackermann(num1 - 1, 1)
  
  return ackermann(num1 - 1, ackermann(num1, num2 - 1))


# print(ackermann(2))
# print(ackermann(3))
# print(ackermann(4))
# print(ackermann(5))


def zib(n, memo={0: 1, 1: 1, 2: 2}):
    if n in memo:
        return memo[n]
    
    if n % 2 == 1:
        k = (n - 1) // 2
        memo[n] = zib(k) + zib(k - 1) + 1

    else:
        k = n // 2
        memo[n] = zib(k) + zib(k + 1) + 1

    return memo[n]


print(f"Zib(10) = {zib(10)}")
print(f"Zib(100) = {zib(100)}")


def find_best_zib(target):

    mapping = {}
    for i in range(5000):
        val = zib(i)
        mapping[val] = max(mapping.get(val, -1), i)
    
    return mapping.get(target, None)

print(f"bestZibNum(3186) = {find_best_zib(3186)}")
print(f"bestZibNum(3183) = {find_best_zib(3183)}")
