#task1
import math

squares=[x**2 for x in range(1,11)]
print("task1: ",squares)

#task2
def squareFunc(start, end):
    squares2 = [x ** 2 for x in range(start, end )]
    return squares2

print("task2: ",squareFunc(1,11))
