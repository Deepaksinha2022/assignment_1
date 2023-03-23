# Q6. Read about infix, prefix, and postfix expressions.
# Python Program to convert prefix to Infix

def prefixToInfix(prefix):
    arr = []
    i = len(prefix) - 1
    while i >= 0:
        if not isOperator(prefix[i]):
            arr.append(prefix[i])
            i -= 1
        else:
            str = "(" + arr.pop() + prefix[i] + arr.pop() + ")"
            arr.append(str)
            i -= 1     
    return arr.pop()

def isOperator(opr):
    if opr == "*" or opr == "+" or opr == "-" or opr == "/" or opr == "^" or opr == "(" or opr ==  ")":
        return True
    else:
        return False
 
user_input = input("Enter any expression in prefix form ")
print(prefixToInfix(user_input))