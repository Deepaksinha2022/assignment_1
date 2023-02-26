# TASK 1

# class point():

#     def __init__(self,x,y,z):
#         self.x=x
#         self.y=y
#         self.z=z
    
#     def sqSum(self):
#         return (self.x)**2+(self.y)**2+(self.z)**2
   
# user_input1=int(input("Enter 1st number : "))  
# user_input2=int(input("Enter 2nd number : "))
# user_input3=int(input("Enter 3rd number : "))  
# obj_point=point(user_input1,user_input2,user_input3)
# result=obj_point.sqSum()
# print(f"Sum of square of the numbers is : {result}")

# TASK 2

# class calculator():
    
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
    
#     def add(self):
#         sum=self.num1+self.num2
#         print(f" Sum of the numbers is : {sum}")
        
#     def subtract(self):
#         sub=self.num1-self.num2
#         print(f" Difference  of the numbers is : {sub}")
        
#     def multiply(self):
#         mul=self.num1*self.num2
#         print(f" Product of the numbers is : {mul}")
              
#     def divide(self):
#         div=self.num1/self.num2
#         print(f" Result of Division is : {div}")

# num1=int(input("Enter 1st number : "))
# num2=int(input("Enter 2nd number : "))   
# cal_obj=calculator(num1,num2)
# cal_obj.add()
# cal_obj.subtract()
# cal_obj.multiply()
# cal_obj.divide()

# TASK 3

# class Student:

#     def set_name(self,__name):
#         self.__name=__name
    
#     def get_name(self):
#         print("Name : ",self.__name)
    
#     def set_Rollnumber(self,__rollnumber):
#         self.__rollnumber=__rollnumber
    
#     def get_Rollnumber(self):
#         print("Roll Number : ",self.__rollnumber)
    
    
# obj=Student()

# obj.set_name("Deepak")
# obj.get_name()
# obj.set_Rollnumber(10)
# obj.get_Rollnumber()
    
      
    
# TASK 4

# class account:  
    
#     def __init__(self,title=None,balance=0):
#         self.title=title
#         self.balance=balance


# class SavingsAccounts(account):
    
#     def __init__(self,title=None,balance=0,interest_rate=0):
#         super().__init__(title=None,balance=0)
#         self.interest_rate=interest_rate
        

# obj_account=account("Ashish",5000)
# obj_savingaccount=SavingsAccounts("Ashish",5000,5)


    

# TASK 5

# class account:  
    
#     def __init__(self,title=None,balance=0):
#         self.title=title
#         self.balance=balance

#     def get_balance(self):
#         return self.balance
    
#     def deposit(self,amount):
#         self.balance=self.balance+amount
        
#     def withdrawal(self,amount):
#         self.balance=self.balance-amount

# class SavingsAccounts(account):
    
#     def __init__(self,title=None,balance=0,int_rate=0):
#         super().__init__(title,balance)
#         self.int_rate=int_rate
        
        
#     def interestamount(self):
#         return (self.balance*self.int_rate)/100
        

# obj_account=account("Ashish",5000)
# obj_account.deposit(2000)
# print("current balance is : ",obj_account.get_balance())
# obj_account.withdrawal(200)
# print("current balance is : ",obj_account.get_balance())
# obj_savingaccount=SavingsAccounts("Ashish",2000,5)
# print(obj_savingaccount.interestamount())