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
