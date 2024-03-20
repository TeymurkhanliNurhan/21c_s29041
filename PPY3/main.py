#task1
import math

squares=[x**2 for x in range(1,11)]
print("task1: ",squares)

#task2
def squareFunc(start, end):
    squares2 = [x ** 2 for x in range(start, end )]
    return squares2

print("task2: ",squareFunc(1,11))


#task3
class SquareClass:
    def class_square_method(self,start,end):
     squares3=[x**2 for x in range(start,end)]
     return squares3

start=int(input("Enter start "))
end=int(input("Enter end "))
squareGen=SquareClass()
print("Squares with class: ",squareGen.class_square_method(start,end+1))

#task4
squareGen4=SquareClass()
roots=[math.sqrt(x) for x in squareGen4.class_square_method(start,end+1)]
print("Roots from class with library: ",roots)

#task5
class InvalidRangeError(Exception):
    """"""
class SquareGenerator:
    def generate_squares(self, start, end):

        if end < start:
            raise InvalidRangeError("End value cannot be less than start value")

        squares = [x ** 2 for x in range(start, end + 1)]
        return squares


squareGen5 = SquareGenerator()
try:
    result = squareGen5.generate_squares(10, 1)
    print("Generated list of squares:", result)
except InvalidRangeError as e:
    print("Error:", e)

    # task6
    # I imported a new module square_generator.py and imported SquareGenerator class to there
    from square_generator import SquareGenerator

    moduleGenerator = SquareGenerator
    print("Squares from module: ", moduleGenerator.generate_squares(1, 1, 10))
