# count numbers of upper and lower case characters

def count_up_lo():
    string=input("Enter any string of your choice : ")
    count_upp=0
    count_low=0
    
    for i in string:
        if ord(i) in range (ord('A'),ord('Z')):
            count_upp+=1
        if ord(i) in range (ord('a'),ord('z')):
            count_low+=1
    print("Upper case character in the entered string is : ",count_upp,"\nLower case character in the entered string is : : ",count_low)
    return count_upp,count_low

count=count_up_lo()