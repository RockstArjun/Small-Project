# Name:- Arjun Chauhan
# Instagram Handle:- @rockstarjun.py

import random
import time
def player1():
    n2=1
    mini=int(input("Enter The minimum value:- "))
    maxi=int(input("Enetr The Maximum value:- "))
    n=int(input("Enter How Many Chances You Want:- "))
    num=[]
    for i in range(mini,maxi+1):
        c=i
        num1=num.append(c)
    print(f"You Have To guess Between {mini} to {maxi}\nYou Have {n} chance")
    time.sleep(3)
    
    while(n2==True):
        
        for i in range(1,n+1):
            wish=random.choice(num)
            

            player=int(input("Enter Your Guessing No. :- "))
            
            if wish==player:
                print(f"Your Guess Is Correct! You Won The Game In {i} chances")
                break
            elif wish<player:
                print(f"You Are So Close To The Actual Number!\nTry Again!You Have Only {3-i} chance left\nThe Actual NUmber is {wish}")
            elif wish>player:
                print(f"You Are So Close To The Actual Number!\nTry Again! You Have Only {3-i} chance left\nThe Actual NUmber is {wish}")
                
                
        if i==3:
            break
        else:
            n2=+1
player1()