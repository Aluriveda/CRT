def number_triangle(n: int) -> str:
    lines = []
    
    for i in range(1, n + 1):
        line = ''.join(str(num) for num in range(1, i + 1))
        lines.append(line)
    
    return '\n'.join(lines)