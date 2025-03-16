def square_root(n):
    x = n / 2  # Initial guess
    for _ in range(10):  # Iterate 10 times for approximation
        x = (x + n / x) / 2
    return x

num = float(input("Enter a number: "))
print("Square root:", square_root(num))



def rectangle_area(length, width):
    return length * width

length = float(input("Enter length: "))
width = float(input("Enter width: "))
print("Area of rectangle:", rectangle_area(length, width))
