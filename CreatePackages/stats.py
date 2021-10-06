def mean(numbers):
    """
    This function returns the mean of the given list of numbers
    """
    return sum(numbers)/len(numbers)


def median(numbers):
    """
    This function returns median of the given list of numbers
    """
    numbers.sort()

    if len(numbers) % 2 == 0:
       median1 = numbers[len(numbers) // 2]
       median2 = numbers[len(numbers) // 2 - 1]
       mymedian = (median1 + median2) / 2
    else:
       mymedian = numbers[len(numbers) // 2]
    return mymedian

Practice Exercise
Create a new module named geometry and add to the mymath package.
Create a module name geometry
Add a function named area_of_rectangle that takes length and breadth as input and returns the area of a rectangle.
Add a function named area_of_circle that takes radius as input and returns the area of a circle.
Modify the __init__.py to include this module.
Import and test the function area_of_circle from python terminal.
