#Write your function here
def double_index(lst, index):
    if lst[index]:
        lst[index] *= 2
        return lst
    else:
        return lst

#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 3))

#Remove start and end from a list

def middle_element(lst):
    
