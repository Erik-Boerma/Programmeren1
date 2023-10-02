import time
from turtle import *
from random import *

def main():
    """
    Main functie. Roept de andere functies op om hun werk te doen. 
    """
    tri()
    done() # tell turtle the drawing is done.

def testing():
    """
    Test functie. Hier staan alle assertions om de functies te testen.
    """

def tri():
    """Draws 100-pixel sides of an equilateral triangle.
    """
    width(5)    # width of the line to draw
    clr = choice(['darkgreen', 'red', 'blue'])  #choose a random color
    color(clr)  # set the color of the line
    shape('turtle') # set the shape of the pencil
    dot(10, 'red')  # set the endpoints of the lines

    forward(200)    #move forward
    left(200)       #turn 200 degrees left 
    forward(200)    #move forward
    left(200)       #turn 200 degrees left 
    forward(200)    #move forward
    left(200)       #turn 200 degrees left 


main()
testing()