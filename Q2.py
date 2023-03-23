# Q2. Write a program to reverse an array in place? In place means you cannot create a new array.
# You have to update the original array
size = int(input("Enter Size : "))
array = []
for i in range(size):  
    element = int(input("Enter the element : "))
    array.append(element)
print(array)
print(array[::-1])