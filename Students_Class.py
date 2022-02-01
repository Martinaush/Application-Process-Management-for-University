#!/usr/bin/env python
# coding: utf-8

# # Importing Students Marks 

# This Worksheet class has been created to manage students marks (their marks can contain up to 26 modules)

# In[1]:


import pandas as pd

import string

# We define the class Worksheet

class Worksheet:
    
    # We will use the function above to create an object in this class
        
    def __init__(self, name, numcolumns):
        
        self.__name = name
        
        self.__col = numcolumns
        
        self.__body = []
        
    def get_body(self):
        
        return self.__body
        
        
    # Retrieving the number of rows and columns respectively
    
    def max_row(self):
        
        return len(self.__body)
        
    def max_column(self):
        
        return self.__col
    
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
    
    def read_cell(self,label):
        
        label = Worksheet.manage_labels(label)
        
        row = int(label[0])
        
        col = int(label[1])
        
        if self.__body[row][col] != None:
            
            return self.__body[row][col]
        
        else:
            
            print("None")
            
    
    # w.write cell(label, newval) Replace the value in the cell denoted by the string `label'
    # with the value of parameter `newval'. Return the old value from that cell. Ignored
    # the possibility of there being no cell with that label.
    
    def write_cell(self, label, newval):
        
        label = Worksheet.manage_labels(label)
        
        aux = self.__body[label[0]][label[1]] 
        
        self.__body[label[0]][label[1]] = newval
        
        if aux != None:
        
            return aux
        
        else:
            
            print("None")
    
    # w.append(self, newvals) Append a new row at the end of this worksheet i.e. beneath
    
    def append(self,newvals = None):
        
        if newvals == None:
            
            newvals = [None]*self.__col
            
        elif len(newvals) != self.__col:
            
            while len(newvals) != self.__col:
                
                newvals.append(None)
        
        self.__body.append(newvals)
        
        
    # Printing the body of the function
    
    def show(self):
        
        # Printing first row
        
        print(" "*9, end = "")
        
        alphabet_string = string.ascii_uppercase
        
        alphabet_list = list(alphabet_string)
        
        for i in range(0, self.__col):
            
            print("%-10s"%alphabet_list[i], end = "")
            
        print()
            
        # Separation between rows
        
        print("="*(10*self.__col + 8))
        
        # Printing indexes
        
        for i in range(self.max_row()):
            
            print("[ ",i+1,"] : ", end = "")
            
            for j in range(self.max_column()):
                
                print("%-10s"%self.__body[i][j], end = "")
                
            print()
            
        print("-"*(10*self.__col + 8))
        
        
    # Adding all the marks together and stored another worksheet
    
    def add_totals(self):
    
        body = self.get_body()

        # Creating another worksheet

        w2 = Worksheet("w2", self.max_column() + 1)

        for i in range(0, self.max_row()):

            suma = 0

            for j in range(0, self.max_column()):

                try:

                    num = int(body[i][j])

                    suma += num

                except:

                    continue

            # Adding the column

            body[i].append(suma)

            w2.append(body[i])

        w2.show()
        
        return w2


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

            return w
        
        except:
            print("*** Trouble loading %s." % filename)
              
        


# In[2]:


student_file = "Students.csv"

students = Worksheet.initialize(student_file)

students.show()


# In[3]:


students.add_totals()


# In[ ]:




