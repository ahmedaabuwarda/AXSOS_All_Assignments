def tribonacci(n: int) -> int:
    # Handle the base cases directly
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    
    # Initialize the first three Tribonacci numbers
    t0, t1, t2 = 0, 1, 1
    
    # Iteratively calculate up to the n-th number
    for _ in range(3, n + 1):
        next_t = t0 + t1 + t2
        t0, t1, t2 = t1, t2, next_t
        
    return t2

print(tribonacci(5))