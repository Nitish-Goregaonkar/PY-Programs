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


# Program to calculate the area and perimeter of a square
side = float(input("Enter the side length of the square: "))

area = side * side
perimeter = 4 * side

print(f"The area of the square is {area}")
print(f"The perimeter of the square is {perimeter}")


# Program to swap the values of two variables
a = input("Enter the value of a: ")
b = input("Enter the value of b: ")

# Swapping the values without using a temporary variable
temp = a
a = b
b = temp

print(f"The value of a after swapping: {a}")
print(f"The value of b after swapping: {b}")





