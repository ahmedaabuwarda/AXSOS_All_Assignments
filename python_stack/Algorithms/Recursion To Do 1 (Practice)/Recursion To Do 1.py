def sigma(number):
    if number <= 0:
        return 0

    return number + sigma(number-1)

print(sigma(5))

def factorial(number):
    if number <= 1:
        return 1

    return number * factorial(number-1)

print(factorial(5))