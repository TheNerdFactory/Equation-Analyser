# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 12:57:54 2020

@author: Kalebh
"""


import numpy as np
import matplotlib.pyplot as plt
import functions as fn

def main():
    rerun = "y"
    while rerun == "y" or rerun == "Y":
       #Gets user input and returns, in a list, the equation, the minimum value
       #of x, the maximum value of x and the "p"recision"
       ui = fn.user_input()
       
       #Sets size of x&y space arrays
       a_size = int(ui[3])  
       
       #Creates an array of values starting and ending at x_min and x_max
       x_space = np.linspace(ui[1], ui[2], a_size)
        
       #Empty array to be filled by evaluated equation values
       y_space = np.array([]) 
    
       #Empty array to be filled with terms of the relevant numerical
       #integration series
       inte_space = np.array([])   
    
       #'Gap' between points in x_space
       del_x = (ui[2]-ui[1])/(a_size)
    
       #Error checking variable for while loop
       runtime = True
       
       #Evaluates the user input equation for each value in x-space and appends that
       #value to the y-space array, giving us two arrays, one covering the domain of the function
       #the other covering the range of the function
       for item in x_space:
           y_space = np.append(y_space,fn.eqn_converter(ui[0], item))
           
           #Updates user on program process at the end of the loop
           #(Informs them )
           if item == x_space[a_size-1]:
               print("Equation Evaluated...\n")
               print("Processing Data...\n")
           
       #Empty array to be filled with the paired input (domain) and output (range)
       #of the user-inputted function
       domain_and_range = np.array([])  
          
       #Appends array with paired input and output values for the given function
       for i in range(len(y_space)):
           domain_and_range = np.append(domain_and_range, [x_space[i], y_space[i]])
           
           #Informs user that this array has been filled
           if i == a_size-1 :
               print("Data Processed...")
       
       #reshapes the array to simplify conversion to .csv format
       domain_and_range = domain_and_range.reshape(a_size,2) 
                
       #Asks user whether or not they wish to have their function plotted
       plot_call = input("Do you wish to plot your equation? (y/n) ")
       
       #Checks for postive answer for plotting
       if plot_call =="y" or plot_call == "Y":
           
           #Calls function that displays and saves the plot
           fn.plotter(x_space, y_space, ui[0], a_size)
           
           while runtime:
               
               #Asks user whether or not they wish to have their function numerically integrated
               inte_call = input("Do you also wish to integrate your equation? (y/n) ")
           
               #Checks for positive answer to integrating 
               if inte_call == "y" or inte_call == "Y":
                   while runtime:
                       #Asks for user to choose method of numerical integration
                       inte_type = input("Trapezium Rule (1) or Simpson's Rule (2): ")
                       
                       if inte_type == "1":
                           
                           #Fills an array with the appropriate values for each term of the trapezium rule, then ends loop
                           # ( See https://en.wikipedia.org/wiki/Trapezoidal_rule )
                           for i in range(len(y_space)):
                               inte_space = np.append(inte_space, fn.trapezium_integrator(y_space[i], del_x, i, a_size-1))
                           print("The area under the graph, as approximated by the Trapezium Rule is " + str(np.sum(inte_space)))
                           runtime = False
                       elif inte_type == "2":
                            #Fills an array with the appropriate values for each term of Simpson's rule, then ends loop
                            #( See https://en.wikipedia.org/wiki/Simpson%27s_rule ) 
                            for i in range(len(y_space)):
                                inte_space = np.append(inte_space, fn.simpson_integrator(y_space[i], del_x, i, a_size-1))
                            print("The area under the graph, as approximated by Simpson's Rule is " + str(np.sum(inte_space)))
                            runtime = False  
                       else: 
                            #Calls input error function for any incorrect input 
                            fn.input_error()
               #Checks for negative answer to integrating 
               elif inte_call == "n" or inte_call == "N":
                   #Ends loop and gets user imput on whether or not they wish to analyse another equation
                   runtime = False
                   rerun = input("Would you like to enter another equation? (y/n) ") 
                   break
           #Asks user if they wish to analyse another equation and breaks the loop
           rerun = input("Would you like to enter another equation? (y/n) ") 
           break
       #Checks for negative answer to plotting equaioyn 
       elif plot_call == "n" or plot_call == "N":
           rerun = input("Would you like to enter another equation? (y/n) ")
           np.savetxt('plot.csv', domain_and_range, delimiter=",")
           print("Your equation values have been saves in a .csv file for future use. Thank you for using this program! :)")
           break
          
            
    """
    Need to strip any full stops within ui[0] to allow for proper name formatting for files
    """
    np.savetxt(str(ui[0]) + '.csv', domain_and_range, delimiter=",")
    print("Your equation values have been saves in a .csv file for future use. Thank you for using this program! :)")
    rerun = "x"

if __name__ == "__main__":
    main()