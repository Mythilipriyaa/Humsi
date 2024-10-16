def is_triangle(a: int, b: int, c: int) -> bool:
    return a + b > c and a + c > b and b + c > a
print(is_triangle(3, 4, 5))  

