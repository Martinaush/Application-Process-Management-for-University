# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 09:02:01 2022

@author: Martin Ramirez Tinoco
"""

from Student_Marks import *

import pandas as pd

def print_menu():
    
    print("*"*30)
    
    print("MENU")
    
    print("*"*30)
    
    print("1-. Visualize your data")
    
    print("2-. Visualize your data sorted in terms of average final score")
    
    print("3-. Describing each assessment")
    
    print("4-. Describe a columns in specific, please be concious")
    
    print("5-. Data containing Passes/Fail depending on the average of each assessment")
    
    print("6 -. Press 0 to exit")



def Menu():
    
    option = -1 # Key of the menu
    
    # Initiliazing data
    
    students = Worksheet.initialize("Marks.csv")
    
    # Checking value passed
    
    while option != 0:
        
        option = -1
        
        # Printing menu
    
        print_menu()
        
        while True:
        
            try:

                while option < 0 or option > 5:
                
                    option = input("Please give me what you want to do: \t")

                    option = int(option)

                    if option < 0 or option > 5:

                        print("Please give me an appropiate number... ")

                break

            except:

                continue

        # Body of the menu function
        
        if option == 0:
            
            print("Have a good day!")
            
            break

        if option == 1:

            students = Worksheet.initialize("Marks.csv")

            display(students)

        if option == 2:

            students_final = Worksheet.add_totals()

            display(Worksheet.sort())

        if option == 3:

            display(Worksheet.describe())
            
        if option == 4:
            
            col = str(input("Please tell me the assessment you are insterested on: \t"))
            
            display(Worksheet.describe_column(col))
            
        if option == 5:
            
            display(Worksheet.passes())


        
        