# Q4. Write a program to print the first non-repeated character from a string?
user_str =input("Enter any string : ")
for i in user_str:
    if (user_str.find(i, (user_str.find(i)+1))) == -1:
            print("First non-repeating character is", i)
            break