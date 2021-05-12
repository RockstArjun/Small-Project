import time
def age_finder():
    num=1
    year=time.strftime("%Y")
    print(f"This Is The Present Year {year}")
    while(num==True):
        age=int(input("Enter your Year of birth:- "))
        if age>=999:
            b=int(year)-age
            print(f"Your Age Is {b}")
        else:
            print("This Is too Much As Your Age. Please try again!")
        again=str(input("Do You Want To Find Your Age Again(y or n):- "))
        if again=="y":
            num=+1
        else:
            break 
print(age_finder())
