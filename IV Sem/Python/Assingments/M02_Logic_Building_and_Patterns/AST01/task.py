def count_digits(n: int) -> int:
    # Handle negative numbers by taking absolute value
    n = abs(n)
    
    # Special case for 0
    if n == 0:
        return 1
    
    count = 0
    while n > 0:
        n //= 10
        count += 1
    
    return count