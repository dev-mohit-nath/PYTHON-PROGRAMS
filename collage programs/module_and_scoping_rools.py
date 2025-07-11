#import a module
import math
print("PI:",math.pi)

#Define a viriable in a module

x = 5

def my_function():
    global x
    x = 10
    
my_function()
    
print("X after function Call: ", x)
    
    
