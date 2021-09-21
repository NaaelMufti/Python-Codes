from turtle import *

reset()
counter = 0 
sides = int(input("How many sides (3-20)? ") )

while counter < sides:
    forward(100)
    left(360/sides)
    counter = counter + 1
