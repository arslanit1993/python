#THe question is what are the tools we need in order to get the left_part_rightmost every time 
#What happens to your tools over recursion
#Recursion is one of your tools
#There is no mid, there is left part, left_most_element
def binary_search(arr, lm, rm, x):
    while lm <= rm:
        left_part_lm = lm + (rm - lm) // 2
        
        if arr[left_part_lm] == x:
            return left_part_lm

        elif arr[left_part_lm] > x:
            rm = left_part_lm - 1

        else:
            lm = left_part_lm + 1

    return -1

array = [i for i in range(0,80,3)]

for i in array:        
    result = binary_search(array, 0, len(array)-1, i)
    
    if result == -1:
        print(f"The value,{i}, is out of range")

    else:
        print(f"The value, {i}, is at index, {result} ")
    





        
