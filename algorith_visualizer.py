import matplotlib.pyplot as plt
import numpy as np 

def binary_search(arr, lm_in, rm_in, x):
    if len(arr) < 0:
        return "The passed array's lenth is less than 0"

    elif len(arr) == 0:
        return "The list can not be an empty list"
    
    elif len(arr) == 1:
        return "There is only one item in the array you passed"
    

    elif arr[lm_in] > arr[rm_in]:
        return "The list might not be sorted because the left most element can not be bigger than the rightmost element"


    else:
        while lm_in < rm_in:
            left_part_rm = lm_in + (rm_in - lm_in) // 2
            
            if arr[left_part_rm] == x:
                return left_part_rm 
                
            elif arr[left_part_rm] > x:
                rm_in = lm_in
            
            else:
                lm_in = rm_in
                
        
        return "The element is not in the list"




#Possible indices when len(arr)=2:     0, 1
#Don't forget we are only manipulation indices
#Possible values when len(arr) = 2: [0,0], [0,1], [1,0], [1,1]
#THe indices can not be equal or the rightmost index can not be less than the left most as;ldkj tan ian 
#THe journey into reliability 
#We are manipulating indices to get the left most item 


array =[0,1]
result = binary_search(array, 0, len(array) - 1, 1)


print(result)

my_list = np.random.randint(0,100, 10)
x = np.arange(0,10, 1)

print(x)

plt.bar(x,my_list, width=0.5,)
