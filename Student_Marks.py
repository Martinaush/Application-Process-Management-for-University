# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 23:25:54 2022

@author: Martin Ramirez Tinoco
"""

import pandas as pd

import string

# We define the class Worksheet

class Worksheet:
    
    # -------------------------------------------------------------------------------
    
    # Global constants
    
    # -------------------------------------------------------------------------------    
    
    # Names for the 2 dataframes
    
    names = ["ID","Lab-1","Lab-2","Lab-3","Lab-4","Lab-5","Lab-6","Lab-7","Lab-8",
             "Lab-9","Lab-10","Lab-11","Lab-12","Lab-13","Lab-14","Quiz-1","Quiz-2","Quiz-3","Quiz-4","Quiz-5","Quiz-6","Midterm","Final"]
    
    
    
    # Dataframes
    
    df_1 = pd.DataFrame() # Containing results
    
    df_2 = pd.DataFrame() # Containing results and averages
    
    df_passes = pd.DataFrame() # Containing passes
    
    # ------------------------------------------------------------------------------- 
    
    # We will use the function above to create an object in this class
        
    def __init__(self, name, numcolumns):
        
        self.__name = name
        
        self.__col = numcolumns
        
        self.__body = []
        
    def get_body(self):
        
        return self.__body
        
    # -------------------------------------------------------------------------------
    
    # Global Functions
    
    # -------------------------------------------------------------------------------  
    
    # We need to create an auxiliary function to manage labels
    # Labels are in this form "A1" or "B3" or "C5" etc.
    
    def manage_labels(label):
        
        col = label[0]
        
        row = int(label[1]) - 1
        
        tup = [row,0]
        
        alphabet_string = string.ascii_uppercase
        
        alphabet_list = list(alphabet_string)
        
        for i in range(0,len(alphabet_list)):
            
            if alphabet_list[i] == col:
                
                tup[1] = i
                
        return tup

    
    # Return the value in the cell denoted by the string 'label'. Ignored 
    # the possibility of there being no cell with that label.
    
    def read_cell(label):
        
        label = Worksheet.manage_labels(label)
        
        row = int(label[0])
        
        col = int(label[1])
        
        if Worksheet.df_1.iloc[row][col] != None:
            
            return Worksheet.df_1.iloc[row][col]
        
        else:
            
            print("None")
            
    
    # w.write cell(label, newval) Replace the value in the cell denoted by the string `label'
    # with the value of parameter `newval'. Return the old value from that cell. Ignored
    # the possibility of there being no cell with that label.
    
    def write_cell(label, newval):
        
        label = Worksheet.manage_labels(label)
        
        aux = Worksheet.df_1.iloc[label[0]][label[1]] 
        
        Worksheet.df_1.iloc[label[0]][label[1]] = newval
        
        if aux != None:
        
            return aux
        
        else:
            
            print("None")
    
    # w.append(self, newvals) Append a new row at the end of this worksheet i.e. beneath
    
    def append(self,newvals = None):
        
        for i in range(len(newvals)):
            
            try:
                
                newvals[i] = int(newvals[i])
                
            except:
                
                newvals[i] = 0
        
        if newvals == None:
            
            newvals = [0]*self.__col
            
        elif len(newvals) != self.__col:
            
            while len(newvals) != self.__col:
                
                newvals.append(0)
            
        self.__body.append(newvals)
        
    # Adding all the marks together and stored another worksheet
    
    def add_totals():
        
        vector_sum = 0 # Vector containing total
        
        # Populating it
        
        ncol = Worksheet.df_1.shape[1]
        
        vector_sum = round(Worksheet.df_1.iloc[:,1:].sum(axis = 1)/ncol,2)

        Worksheet.df_2 = Worksheet.df_1
        
        Worksheet.df_2['Result'] = vector_sum

        return Worksheet.df_2
    
    # Data frame sorted in terms of column result
    
    def sort():
        
        return Worksheet.df_2.sort_values(by = ['Result','Final'], ascending = [False,False])
    
    # Function to show the DataFrame containing averages
    
    def Averages():
        
        return Worksheet.df_2
    
    # Describing each column
    
    def describe():
        
        return Worksheet.df_2.iloc[:,1:].describe()
    
    # Function that gives us a summary of each column
    
    def describe_column(col):
        
        if col == "Result":
            
            return Worksheet.df_2.loc[:,col].describe()
        
        else:
            
            return Worksheet.df_1.loc[:,col].describe()

    # Function that gives you the students passing each assessment (to pass the exam they should score
    # above the average)
    
    def passes():
        
        col = Worksheet.df_2.shape[1] # Clumns of the dataframe df_2
        
        Worksheet.df_passes = Worksheet.df_2
        
        column_names = Worksheet.df_2.columns[1:]
        
        for col in column_names:
            
            avg_column = float(Worksheet.describe_column(col)[1])
            
            vector = Worksheet.df_2[col] >= avg_column
            
            for i in range(len(vector)):
                
                if vector[i] == True:
                    
                    Worksheet.df_passes.loc[i,col] = 'Pass'
                    
                else:
                    
                    Worksheet.df_passes.loc[i,col] = 'Fail'
            
            
        return Worksheet.df_passes
            
            

    # Initialize the Worksheet using a csv
    
    def initialize(filename):
        # Read each student's comps from .csv  'filename' and create
        # student object. Format: surname, name, mark1, mark2 and so on
        
        try:
            afile = open(filename, "r")
            
            for line in afile:
                
                comp = line.split(",")
                
                n = len(comp)
                
                break
            
            w = Worksheet("w", n)
            
            afile = open(filename, "r")
            
            for line in afile:
                
                if not line.isspace():
                    
                    line = line.strip("\n")
                    
                    comp = line.split(",")
                    
                    w.append(comp)
        
            Worksheet.df_1 = pd.DataFrame(w.get_body(), columns = Worksheet.names)
            
            # We initilize the dataframe with Results
            
            Worksheet.add_totals()
        
            return Worksheet.df_1
        
        except:
            print("*** Trouble loading %s." % filename)
              
        