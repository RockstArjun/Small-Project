# Name:- ARJUN CHAUHAN
# Instagram handle:- @rockstarjun.py

def next_palindrome(n):
    n = n+1
    while not is_palindrome(n):
        n += 1
    return n


def is_palindrome(n):
    return str(n) == str(n)[::-1]


if __name__ == "__main__":
    n = int(input("How Many Palindrome Number You Want:- "))
    numbers = []
    for i in range(1,n+1):
        number = int(input(f"Enter the {i} number:- "))
        numbers.append(number)

    for i in range(n):
        print(f"Next palindrome for {numbers[i]} is {next_palindrome(numbers[i])}")
