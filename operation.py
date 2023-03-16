import json
def register(filename,name,mobile_no,email_ID,password,address):
    
    details = {"Name": name,"Mobile Number":mobile_no,"E-mail ID": email_ID,"Password":password,"Address":address}
        
    file = open(filename,"r+")
    try:
        data = json.load(file)
        if data:
            if details not in data:
                file.append(details)
                file.seek(0)
                file.truncate()
                json.dump(data,file)
                file.close()
                return True
        else:
            return False
    except json.decoder.JSONDecodeError:
        lst=[]
        lst.append(details)
        json.dump(lst,file)
        file.close
        return True
    
    except Exception as ex:
        print("Exception in register function ",ex)
        return False
    
    finally:
        file.close()
        
    return False

def login(filename,username,password):
    
    file = open(filename,"r+")
    try:
        data = json.load(file)
        for i in data:
            if i["E-mail ID"] == username and i["Password"] == password:
                return True
            else:
                return False 
    except Exception as ex:
        print("Exception in Login ",ex)
    return False

def AddNewFoodItem(filename,foodID,name,quantity,price,discount,stock):
    
    file = open(filename,"r+")
    details = {"Food ID":foodID,"Name":name,"Quantity":quantity,"Price":price,"Discount":discount,"Stock":stock}
    try:
        data=json.load(file)
        if data:
            if details not in data:
                data.append(details)
                file.seek(0)
                file.truncate()
                json.dump(data,file)
                return True
        else:
            return False
    except json.decoder.JSONDecodeError:
        lst=[]
        lst.append(details)
        json.dump(lst,file)
        file.close
        return True
    
    except Exception as ex:
        print("Exception in register function ",ex)
        return False
    
    finally:
        file.close()
        
    return False
    
    
def EditFoodItem(filename,foodID):
    file = open(filename,"r+")
    data = json.load(file)
    for i in range(len(data)):
        if data[i]["Food ID"] == foodID:
            name = input("Enter Name  : ")
            quantity = input("Enter Quantity : ")
            price = float(input("Enter Price :"))
            discount = float(input("Enter Discount : "))
            stock = float(input("Enter Stock : "))
            data[i]["Name"] = name
            data[i]["Quantity"] = quantity
            data[i]["Price"] = price
            data[i]["Discount"] = discount
            data[i]["Stock"] = stock
            file.seek(0)
            file.truncate()
            json.dump(data,file)
            file.close()
            return True
    return False
        
def ViewFoodItem(filename):
    file = open(filename,"r+")
    data = json.load(file)
    return data

def RemoveFoodItem(filename,foodID):
    
    file = open(filename,"r+")
    data = json.load(file)
    for i in range(len(data)):
        if data[i]["Food ID"] == foodID:
            data.pop(i)
            file.seek(0)
            file.truncate()
            json.dump(data,file)
            file.close
            return True
    return False
            
def UserFoodDisplay(filename1,filename2,username):
    
    file = open(filename1,"r+")
    data = json.load(file)
    for i in range(len(data)):
        print(f"""{i} {data[i]["Name"]} ({data[i]["Quantity"]}) [{data[i]["Price"]}]""")
    print()
    user_input = list(map(int,input("Enter serial no of Food Items to Place an order : ").split()))
    print(f"List of Selected Items : ")
    order_lst = []
    for i in user_input:
        print(f"""{i} {data[i]["Name"]}""")
        order_lst.append(data[i]["Name"])
    print()
    total_order_price = 0
    for i in user_input:
        total_order_price += data[i]["Price"]
    print("Total Price for Your Selected Item is Rupees ",total_order_price)
    order_input = int(input("Enter\n1. To Place Order \n2. Exit\n"))
    order_details = {username:[order_lst,total_order_price]}
    if order_input == 1:
        print("Order Placed !!!")
        file1 = open(filename2,"r+")
        try:
            data1=json.load(file1)
            if data1:
                if order_details not in data:
                    data1.append(order_details)
                    file1.seek(0)
                    file1.truncate()
                    json.dump(data1,file1)
                    return True
            else:
                return False
        except json.decoder.JSONDecodeError:
            lst1=[]
            lst1.append(order_details)
            json.dump(lst1,file1)
            file1.close
            return True  
    if order_input == 2:
        print("Thank You !!!")
        exit()   
        
    file.close()    
    
def OrderHistory(filename,username):
    file = open(filename,"r+")
    data = json.load(file)
    for i in range(len(data)):
        print(data[i][username])
        print()       
    file.close()
            
def UpdateProfile(filename,username):
    file = open(filename,"r+")
    data = json.load(file)
    for i in range(len(data)):
        if data[i]["E-mail ID"] == username:
            name = input("Enter Your Name : ")
            mobile_no = input("Enter Your Mobile No. : ")
            email_ID = input("Enter Your email-ID : ")
            password = input("Enter Your Password : ")
            address = input("Enter Your Address : ")
            data[i]["Name"] = name
            data[i]["Mobile Number"] = mobile_no
            data[i]["E-mail ID"] = email_ID
            data[i]["Password"] = password
            data[i]["Address"] = address
            file.seek(0)
            file.truncate()
            json.dump(data,file)
            file.close()
            return True
    return False
   
    
                