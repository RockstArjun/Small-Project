import time
print("Use small c for Celcius")
print("Use small f For Fahrenheit")
print("Use small k For Kelvin")
time.sleep(5)
def temp_convrt():
    num=1
    while(num==True):
        
        wish=str(input("From Which temp. To Which temp. you want to convert:- "))
        if wish=="c to f":
            Cel=float(input("Enter The Temprature In Celcius:- "))
            f=(Cel*1.8)+32
            print(f"Your Temprature In Fahrenheit Is {f}")
        elif wish=="c to k":
            Cel=float(input("Enter The Temprature In Celcius:- "))
            k=Cel+273.15
            print(f"Your Temprature In Fahrenheit Is {k}")
        elif wish=="k to c":
            kel=float(input("Enter The Temprature In Kelvin:- "))
            ke=kel-273.15
            print(f"Your Temprature In Fahrenheit Is {ke}")
        elif wish=="k to f":
            kel=float(input("Enter The Temprature In Kelvin:- "))
            ka=(kel-273.15)*1.8+32
            print(f"Your Temprature In Fahrenheit Is {ka}")
        elif wish=="f to c":
            fer=float(input("Enter The Temprature In Fahrenheit:- "))
            fe=(fer-32)*(0.55555555555)
            print(f"Your Temprature In Fahrenheit Is {fe}")
        elif wish=="f to k":
            fer=float(input("Enter The Temprature In Fahrenheit:- "))
            fa=(fer-32)*(0.55555555555)+273.15
            print(f"Your Temprature In Fahrenheit Is {fa}")
        again=str(input("Do You Want To Convert Again(y or n):- "))
        if again=="y":
            num=+1
        else:
            break
print(temp_convrt())