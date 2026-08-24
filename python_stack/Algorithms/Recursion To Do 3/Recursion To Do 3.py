def r_binary_search(arr, val, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    if start > end:
        return False
    
    mid = (start + end) // 2
    
    if arr[mid] == val:
        return True
    elif arr[mid] > val:
        return r_binary_search(arr, val, start, mid - 1)
    else:
        return r_binary_search(arr, val, mid + 1, end)

print(r_binary_search([1,3,5,6],4))

print(r_binary_search([4,5,6,8,12],5))


def rGCF(a, b):
    if b == 0:
        return a
        
    return rGCF(b, a % b)


print(rGCF(12345,12345))
print(rGCF(123456,987654))


def tarai(x: int, y: int, z: int) -> int:
    """Standard recursive Tarai function."""
    if x <= y:
        return y
    else:
        return tarai(
            tarai(x - 1, y, z),
            tarai(y - 1, z, x),
            tarai(z - 1, x, y)
        )


result = tarai(10, 2, 9)
print(f"tarai(10, 2, 9) = {result}")