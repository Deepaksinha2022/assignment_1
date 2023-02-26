# Assignment 1 - Question 2
# Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.
import json

capital={"Sikkim":"Gangtok","Assam":"Gauhati","Nagaland":"Kohima","Tripura":"Agartala",
         "Meghalaya":"Cherapunji","Arunachal Pradesh":"Itanagar","Manipur":"Imphal"}


with open (r"G:\\DS301222\\python\\python\\Assignment.py\\caiptal.json","w") as file:
    json.dump(capital,file)