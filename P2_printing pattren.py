row=int(input("Enter no. of row:- "))
blen=int(input("Enter 1 or 0:- "))
new=bool(blen)
if new==True:
    for i in range(1,row+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif new==False:
    for i in range(row,0,-1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()