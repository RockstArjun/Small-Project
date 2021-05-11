num=1
while(num==True):
    a1 = int(input("Enter first no."))
    a2 = int(input("Enter Second no."))
    op = str(input("Enter the operator:"))
    
    if op== "+":
        print(a1+a2)
    elif op== "-":
        print(a1-a2)
    elif op=="*":
        print(a1*a2)
    elif op=="/" or "%":
        print(a1/a2)
    else:
        print("Invalid Operator")
    es=str(input("You wish to calculate more thing(y/n):- ")) 
    if es=="y":
        num=+1
    else:
        break
