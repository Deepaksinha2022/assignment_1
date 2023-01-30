# Python function to find the sum of the elements of an list 
def sum_lst(lst=[],sum=0):
    size=int(input("enter the size : "))
    for i in range(size):
        element_lst=int(input("enter the elements of the list : "))
        lst.append(element_lst)
    print("The list is : ",lst)
    for j in lst:
        sum=sum+j
    print("Sum of the elements of the list is : ",sum)
    return lst,sum

summation=sum_lst()


        
    