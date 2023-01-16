num1=0
num2=1
num3=0
print("Fibonacci series between 0 and 50 are :",num1,num2,end=' ')
for i in range(2,10):
    num3=num1+num2 
    num1=num2
    num2=num3
    print(num3,end=' ')
  