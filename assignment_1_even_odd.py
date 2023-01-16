range_max=int(input("Enter the range : "))
lst=[]
for i in range(range_max):
    series=int((input("Enter numbers upto the range you have entered :")))
    lst.append(series)
count=0
count1=0
for i in lst:
    if i%2==0:
        count+=1
    if not(i%2==0):
        count1+=1
print("Numbers of even number :",count,"\n","Number of odd numbers :",count1)