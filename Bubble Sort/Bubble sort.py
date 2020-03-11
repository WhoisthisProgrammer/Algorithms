# Learn at my first year of Python course.

def bubbleSort(ls):
    for i in range(len(ls)):
        for j in range(0,len(ls)-i-1):
            if ls[j] > ls[j+1]:
                ls[j],ls[j+1] = ls[j+1],ls[j]
    return ls
        


ls = [7,8,5,4,3,6,7,4,57,4,3,234,0]
print("Original List : ",ls)

ls = bubbleSort(ls)
print("The sorted list : ",ls)
