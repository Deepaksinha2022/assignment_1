# Q3. Write a program to check if two strings are a rotation of each other?

str1 = input("Enter 1st string : ")
str2 = input("Enter 2nd string : ")
if len(str1) == len(str2):
    lst1 = []
    for i in str1:
        lst1.append(ord(i))
    lst2 = []
    for j in str2:
        lst2.append(ord(j))
    if sum(lst1) == sum(lst2):
        print("Strings are rotation to each other")
    else:
        print("Strings are not a rotation to each other")
else:
        print("Strings are not a rotation to each other")