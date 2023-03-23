# Q7. Write a program to check if all the brackets are closed in a given code snippet.
lst = []
def BalancedBrackets(expr):
    lst = []
    for char in expr:
        if char in ["(", "{", "["]:
            lst.append(char)
        else:
            if not lst:
                return False
            current_char = lst.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
    if lst:
        return False
    return True
expr = "{()}[]"
if BalancedBrackets(expr):
    print("Balanced")
else:
    print("Not Balanced")