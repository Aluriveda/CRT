def right_triangle(n: int) -> str:
    lines = []
    
    for i in range(1, n + 1):
        lines.append('*' * i)
    
    return '\n'.join(lines)