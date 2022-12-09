import math

def main():
    #print(sum_and_difference(10,5))
    #print(float_division(3,9))
    #print(integer_division(10,4))
    #print(powerful_operations(5,4))
    #print(find_average(9,4))
    #print(area_of_a_circle(5.4))
    #print(area_of_an_equilateral_triangle(1.4))
    #print (calculate_discriminant(1,5,1))
    print (calculate_cathetus_length(2,4))
          
def sum_and_difference(num_a: int, num_b: int) -> tuple:
    """Return the sum and difference of given variables num_a and num_b."""
    sum = num_a + num_b
    difference = num_a - num_b
    
    return sum, difference

def float_division(num_a: int, num_b: int) -> float:
    """Divide given variables num_a and num_b and return the result."""
    division = num_a / num_b
    return division

def integer_division(num_a: int, num_b: int) -> int:
    """Divide given variables num_a and num_b and return the result rounded down."""
    division = num_a//num_b
    return division

def powerful_operations(num_a: int, num_b: int) -> tuple:
    """Return the product of given variables, num_a to the power of num_b and the remainder of division of variables."""
    multiply_numbers = num_a * num_b
    power = num_a ** num_b
    remainder = num_a % num_b
    return multiply_numbers, power, remainder

def find_average(num_a: int, num_b: int) -> float:
    """Return the average of given variables."""
    average = (num_a + num_b)/2
    return average

def area_of_a_circle(radius: float) -> float:
    """Calculate and return the area of a circle."""
    circle_area = math.pi * (radius ** 2)
    return circle_area

def area_of_an_equilateral_triangle(side_length: float) -> int:
    """Calculate and return the area of an equilateral triangle. √3/4 × (side)2"""
    triangle_area = round((math.sqrt(3))/4 * (side_length ** 2))
    return triangle_area

def calculate_discriminant(a: int, b: int, c: int) -> int:
    """Calculate discriminant with given variables and return the result."""
    discriminant = b ** 2 - 4*a*c
    return discriminant

def calculate_cathetus_length(a: int, c: int) -> float:
    """Return the length of cathetus when the lengths of the second cathetus and hypotenuse are given."""
    b = c ** 2 - a ** 2
    return b
    
if __name__ == '__main__':
    main()