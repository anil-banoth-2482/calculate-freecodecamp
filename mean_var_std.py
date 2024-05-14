import numpy as np
import sys

def calculate(my_list):
     print(my_list[0])
     if(len(my_list)!=9):
         
         return ValueError("List must contain nine numbers.")

     array=np.array(my_list)
     array1=array.reshape(3,3)
     print(array1)
     calculation={}
     
     calculation['mean']=[list(np.mean(array1,axis=0)),list(np.mean(array1,axis=1)),float(np.mean(array1))]
     calculation['variance']=[list(np.var(array1,axis=0)),list(np.var(array1,axis=1)),float(np.var(array1))]
     calculation['standard deviation']=[np.std(array1,axis=0),np.std(array1,axis=1),np.std(array1)]
     calculation['max']=[list(np.max(array1,axis=0)),list(np.max(array1,axis=1)),np.max(array1)]
     calculation['min']=[list(np.min(array1,axis=0)),list(np.min(array1,axis=1)),np.min(array1)]
     calculation['sum']=[list(np.sum(array1,axis=0)),list(np.sum(array1,axis=1)),np.sum(array1)]
     
     return calculation

    

if __name__=="__main__":
   
   input_list=list(map(int,input("enter the nine numbers sepatated by spaces: ").split()))
   
   try:
       
    print(calculate(input_list))
   except ValueError as e:
     print(e)

       