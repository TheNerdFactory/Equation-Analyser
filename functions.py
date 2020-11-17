# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 12:53:50 2020

@author: Kalebh
"""
"""
This is a fuctions module
"""

import numpy as np
import matplotlib.pyplot as plt

def plotter(x,y,eqn,a_size):
    """
    Parameters
    ----------
    x : Float Numpy Array
        Range of x values that the equation is evaluated across.
    y : Float Numpy Array
        Evaluated equations values across the range of x values.
    eqn : String
          User inputed equation string.
    a_size : int
        Controls size of x, zeros and ones arrays.
    Returns
    -------
    None.
    """
    i = 1
    plt.figure()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("y = " + eqn)
   #plt.plot(x,np.zeros(a_size),"k-")
   #plt.plot(np.ones(a_size),y,"k-")
    plt.plot(x,y)
    plt.savefig("plot " + str(i) + ".png",  dpi=750, format="png")
    plt.show()
    i += 1
    
def eqn_converter(eqn_string,x):
    """
    Parameters
    ----------
    eqn_string : String
                 Equation to be evaluated.
    x : Float
        Value at which the equation is evaluated.
    Returns
    -------
    Float
    Evauated equation value for a given x.
    """
    return eval(eqn_string)

def user_input():
    """
    Returns
    -------
    Eqn_string : String
                 Equation to be evaluated.
    x_min : float
            Minimum X Value to be evaluated
    x_max : float
            Maximum X Value to be evaluated
    """
    Eqn_string = input("Enter your equation here: ") #Get equation from user
    x_min = float(input("Enter your minumum x value: ")) #Get minimum x value 
    x_max = float(input("Enter your maximum x value: ")) #Get maximum x value
    precision = float(input("Enter the number of function values to be considered for integration: "))
    print("")
    
    return Eqn_string, x_min, x_max, precision

def trapezium_integrator(y, del_x, i, max_i):
    """
    Parameters
    ----------
    y : float
        value of the equation for a given x, to be used to .
    del_x : float
            Avg. "gap" between x values.
    i : int
        position of y in the array y_space.
    max_i : int
            position of last value in y_space.

    Returns
    -------
    Appropriate value in the Trapezium Rule series.
    (i.e. 2* del_x/2 * y for all values except the first and last terms)
    """
    #For details, see https://en.wikipedia.org/wiki/Trapezoidal_rule
    
    #Checks if y is the first or last value in y_space, then evaluates the 
    #appropriate value 
    if i == 0 or i == max_i:   
        return del_x * 0.5 * y 
    elif i > 0 and i < max_i:
        return del_x * y

def simpson_integrator(y, del_x, i, max_i):
    """
    Parameters
    ----------
    y : float
        value of the equation for a given x, to be used to .
    del_x : float
            Avg. "gap" between x values.
    i : int
        position of y in the array y_space.
    max_i : int
            position of last value in y_space.

    Returns
    -------
    Appropriate value in the Simpson's Rule series.
    """
    if i == 0 or i == max_i:
        return del_x * 1/3 * y 
    elif i > 0 and i < max_i:
        if i%2 == 0:
            return 2/3 * del_x * y
        else:
            return 4/3 * del_x * y
        
def input_error():
    print("ERROR: Invalid input. Please try again")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    