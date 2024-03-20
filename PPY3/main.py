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

#task7
#I transformed module into package
from packageTask7.square_generator import SquareGenerator
packageGenerator=SquareGenerator
print("Squares from package: ",packageGenerator.generate_squares(1,1,10))


#task8
class SquareGenerator:
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End value cannot be less than start value")

        squares = [x ** 2 for x in range(start, end + 1)]
        return squares

class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End value cannot be less than start value")

        cubes = [x ** 3 for x in range(start, end + 1)]
        return cubes

# Example usage:
cubic_gen = CubicGenerator()
result = cubic_gen.generate_squares(1, 5)
print("Cubes from the subclass:", result)

class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End value cannot be less than start value for square generation")

        squares = [x ** 2 for x in range(start, end + 1)]
        return squares

# Example usage:
cubic_gen = CubicGenerator()
try:
    result = cubic_gen.generate_squares(5, 1)
    print("Generated list of squares:", result)
except ValueError as e:
    print("Error:", e)

#task10
from abc import ABC, abstractmethod

class SquareGenerator(ABC):
    @abstractmethod
    def generate_squares(self, start, end):
        pass

class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End value cannot be less than start value")

        squares = [x ** 3 for x in range(start, end + 1)]
        return squares

cubic_gen = CubicGenerator()
print("From ABC class: ",cubic_gen.generate_squares(1, 5))
