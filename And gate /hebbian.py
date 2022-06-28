import numpy as np 
from random import randint
#inputs 

X=np.array([[1,1,1],[1,-1,1],[-1,1,1],[-1,-1,1]])
#output
Y_ad=np.array([[1],[-1],[-1],[-1]])




print('input is:')
print (X)
print('output for And Gate is: ')
print (Y_ad)
# print('output for Or Gate is: ')
# print (Y_ad)
weights_ad=np.zeros((3))
# weights_o=np.zeros((3))
print( weights_ad)


# update weight for and gate /logic
def update_weight_ad(X,Y,weights):
    for i in range(4):
         
        weights=weights+X[i]*Y[i]
        
        #print weights
        slope =-(weights[0]/weights[1])
        c=-(weights[2]/weights[0])
        if slope<0 and weights[0]>0:
            weights_main=weights
        
    return weights_main

        
        
    
weights_ad=update_weight_ad(X,Y_ad,weights_ad)



print('Checking after learning selectg a input')
rand_int=int(input('Enter the test case no you want to try'))
print('Select a logic you also want  to check')
logicgate=input()
print( weights_ad)
print('selected input is %d '%rand_int)
print( X[rand_int])
def check_learning(X,weights,rand_int):
    Yin=0
    for i in range(3):
        Yin+=X[rand_int,i]*weights[i]
    if Yin<0:
        Yin=-1
    else:
        Yin=1
    return Yin

# print(weights_ad)
if logicgate=='a' or logicgate=='A':
    weights_in=weights_ad

Yin=check_learning(X,weights_in,rand_int)
print (Yin)
        