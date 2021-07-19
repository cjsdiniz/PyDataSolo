

def balanced(expression):
    # your code goes here
    # for i in range(len(expression)):

    l = []
    for c in expression:
        if c == "(":
            l.insert(0, c)
        elif c == ")":
            if l == []:
                return False
            l.pop(0)
        #print(c, l)
    if l == []:
        return True
    else:
        return False


print(balanced(input()))
