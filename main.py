from operation import *
import re
import random
   
if __name__ == "__main__":
    
    while True:
        try:
            choice = int(input("Enter \n1.Register\n2.Log in\n3.Exit\n"))
        except ValueError:
            print("Enter Correct Choice !!!!")
        if choice == 1:
            try:
                register_choice = int(input("Enter\n1.Register as Admin \n2.Register as User \n3.Exit\n"))
            except ValueError:
                print("Enter Correct Choice !!!!")
                
            if register_choice == 1:
                name = input("Enter Your Name : ")
                mobile_no = input("Enter Your Mobile No. : ")
                email_ID = input("Enter Your email-ID : ")
                password = input("Enter Your Password : ")
                address = input("Enter Your Address :")
                
                name_re = re.findall("^[A-Za-z]{2,15}\s[A-Za-z]{2,15}$",name)
                mobile_no_re =re.findall("^[1-9]{1}[0-9]{9}$",mobile_no)
                email_ID_re = re.findall("^[A-z0-9._]+[@]{1}[a-z]+[.]{1}[A-z]+$",email_ID)
                password_re = re.findall("^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%&*?])([A-Za-z\d!@#$%&*?]{8,16}$)",password)
                address_re = re.findall("^[A-Za-z]{6,16}$",address)
                
                
                if name_re and mobile_no_re and email_ID_re and password_re and address_re:
                    register_flag = register(f"admin2.json",name,mobile_no,email_ID,password,address)
                    if register_flag:
                        print("Registered Successfully as Admin !!!")
                    else:
                        print("Registration Failed !!!")
                else:
                    if not name_re:
                        print("Name format is incorrect ")
                        continue
                    if not mobile_no_re:
                        print("mobile no format is incorrect ")
                        continue
                    if not email_ID_re:
                        print("email-ID format is incorrect")
                        continue
                    if not password_re:
                        print("Password format is incorrect")
                        continue
                    if not address_re:
                        print("Password format is incorrect")
                        continue
        
            if register_choice == 2:
                    name = input("Enter Your Name : ")
                    mobile_no = input("Enter Your Mobile No. : ")
                    email_ID = input("Enter Your email-ID : ")
                    password = input("Enter Your Password : ")
                    address = input("Enter Your Address : ")
                    
                    name_re = re.findall("^[A-Za-z]{2,15}\s[A-Za-z]{2,15}$",name)
                    mobile_no_re =re.findall("^[1-9]{1}[0-9]{9}$",mobile_no)
                    email_ID_re = re.findall("^[A-z0-9._]+[@]{1}[a-z]+[.]{1}[A-z]+$",email_ID)
                    password_re = re.findall("^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%&*?])([A-Za-z\d!@#$%&*?]{8,16}$)",password)
                    address_re = re.findall("^[A-Za-z]{6,16}$",address)
                    
                    if name_re and mobile_no_re and email_ID_re and password_re and address_re:
                        register_flag = register(f"user2.json",name,mobile_no,email_ID,password,address)
                        if register_flag:
                            print("Registered Successfully as User !!!")
                        else:
                            print("Registration Failed !!!")
                    else:
                        if not name_re:
                            print("Name format is incorrect ")
                            continue
                        if not mobile_no_re:
                            print("mobile no format is incorrect ")
                            continue
                        if not email_ID_re:
                            print("email-ID format is incorrect")
                            continue
                        if not password_re:
                            print("Password format is incorrect")
                            continue
                        if not address_re:
                            print("Password format is incorrect")
                            continue
            if register_choice == 3:
                print("Thank Your For Connecting !!!")
                exit()
                
        if choice == 2:
            try:
                login_choice = int(input("Enter \n1.Login as Admin \n2.Login as User \n3.Exit\n"))
            except:
                print("Enter Valid Choice !!")
            if login_choice == 1:
                username = input("Enter Your E-mail ID : ")
                password = input("Enter YOur Password : ")
                login_flag = login(f"admin2.json",username,password)
                if login_flag:
                    print("Login Successfull !!")
                    while True:
                        try:
                            admin_choice = int(input("Enter \n1. Add new food items\n2. Edit Food Items \n3. View Food Items. \n4. Remove Food Item\n5. Exit\n"))
                        except:
                            print("Enter Valid Choice")
                            
                        if admin_choice == 1:
                            print("********Add New Food Item*******")
                            foodID = random.randint(10000,20000)
                            name = input("Enter Name  : ")
                            quantity = input("Enter Quantity : ")
                            price = float(input("Enter Price : "))
                            discount = float(input("Enter Discount : "))
                            stock = float(input("Enter Stock : "))
                            
                            add_new_food_item_flag = AddNewFoodItem("fooditem.json",foodID,name,quantity,price,discount,stock)
                            if add_new_food_item_flag:
                                print("Food Item Added Successfully !!")
                            else:
                                print("Food item not added")     
                                
                        if admin_choice == 2:
                            print("*********Edit Food Item***********")
                            foodID = int(input("Enter FoodID : "))
                            edit_food_item_flag = EditFoodItem("fooditem.json",foodID)
                            if edit_food_item_flag:
                                print("Food Item Updated Successfully !!")
                            else:
                                print("Food item could not be updated")     
                                
                        
                        if admin_choice == 3:
                            print("********View Food Item********")
                            food_item = ViewFoodItem("fooditem.json")
                            for i in food_item:
                                print(i)
                            
                        if admin_choice == 4:
                            print("*******Remove Food Item*********")
                            foodID = int(input("Enter FoodID : "))
                            remove_food_item_flag = RemoveFoodItem("fooditem.json",foodID)
                            if remove_food_item_flag:
                                print("Food Item deleted !!")
                            else:
                                print("Food Item not Deleted")     
                        if admin_choice == 5:
                            print("Thank You !!!")
                            exit()
                else:
                    print("Invalid Username or Password !!!")
                                
            if login_choice == 2:
                username = input("Enter Your E-mail ID : ")
                password = input("Enter YOur Password : ")
                login_flag = login(f"user2.json",username,password)
                if login_flag:
                    print("Login Successfull !!")
                    while True:
                        try:
                            user_choice = int(input("Enter \n1. Place New Order\n2. Order History \n3. Update Profile\n4. Exit\n"))
                        except:
                            print("Enter Valid Choice")
          
                        if user_choice == 1:
                            print("*******Available Food Items********* ")
                            UserFoodDisplay("fooditem.json","orderhistory.json",username)
                        if user_choice == 2:
                            print("******Order History********")
                            OrderHistory("orderhistory.json",username)   
                        if user_choice ==3:
                            update_profile_flag = UpdateProfile("user2.json",username) 
                            if update_profile_flag:
                                print("Profile Updated Successfully !!!")
                            else:
                                print("Profile not Updated")                    
                        if user_choice == 4:
                            print("Thank Your !!!")
                            exit()            
                else:
                    print("Invalid Username or Password !!")
                    
            if login_choice == 3:
                print("Thank You !!!")
                exit()                         
        if choice == 3:
            print("Thank You !!!!")
            exit()                   