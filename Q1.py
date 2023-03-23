# Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?  
import array as arr
size = int(input("Enter Size : "))
data = arr.array('i',[])
for i in range(size):  
    element = int(input("Enter the element : "))
    data.append(element)
user_input = int(input("Enter any number : "))
for i in range(len(data)):
    for j in range(i+1,len(data)):
        if data[i] + data[j] == user_input:
            print(f"({data[i]},{data[j]})")  