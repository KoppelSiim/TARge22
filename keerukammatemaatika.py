import math

def main():
    print(time_converter(3600))
    #print(student_helper(45))
    #print(greetings(3))
    #print(adding_numbers(1,2))

def time_converter(seconds: int) -> str:
    """Convert time in seconds to hours and minutes."""
    hours = seconds // 3600
    minutes = hours % 60
    return f"{seconds} sekundit on {hours} tund(i) ja {minutes} minut(it)."

def student_helper(angle: int) -> str:
    """Return the sine and cosine of the given angle in degrees."""
    sine = round(math.sin(angle),1)
    cosine = round(math.cos(angle),1)
    return f"Nurk: {angle}, siinus: {sine}, koosinus: {cosine}."

def greetings(n: int) -> str:
    """Return a string that contains "Hey" n times."""
    lots_of_heys = n*"Hey"
    return lots_of_heys


def adding_numbers(num_a: int, num_b: int) -> str:
    """Return given numbers added together as a string."""
    string_numbers = str(num_a) + str(num_b)
    return string_numbers

if __name__ == '__main__':
    main()