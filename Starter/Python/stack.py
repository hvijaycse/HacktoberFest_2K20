ch = 'a'
def pushc(num):
    ar.append(num)
def popc():
    res = ar.pop()
    if(res == '/b'):
        print("End Of Stack")
        return
    return res

ar = ['/b']

while(ch != "e"):
    print("1.Push\n2.Pop")
    op = int(input("Input Your Option:"))
    if(op == 1):
        num = int(input("Enter The Number:"))
        pushc(num)
    elif(op == 2):
        print("Poped input is:")
        print(popc())
    else:
        print("Invalid Input")
    ch = input("An other try(press e to cancel):")
