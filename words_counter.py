# Name:- Arjun Chauhan
# instagram Handle:- @rockstarjun.py

def parawordsearch():
    user=input("Enter The File Location:- ")
    lis=open(user,"rt")
    for i in lis:
        j=i.split(" ")
        length=len(j)
    print(length)
parawordsearch()