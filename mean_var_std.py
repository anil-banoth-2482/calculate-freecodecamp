import numpy as np
import sys

def calculate(list):

     array=np.array(list)
     array1=array.reshape(3,3)
     print(array1)
    


    

if __name__=="__main__":
   input_str=input("enter the nine numbers sepatated by spaces: ")
   input_list=input_str.split()
   print(input_list)
   while(len(input_list)!=9):
       print("List must contain nine numbers.")
       input_str=input("enter the nine numbers sepatated by spaces: ")
   calculate(input_list)
       