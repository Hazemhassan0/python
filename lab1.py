#- write a program that prints hello world
print("hello world")

#- application to take a number in binary form from the user, and print it as a decimal
binary_int = input("enter binary number:").strip()
while True:
    valid = True
    for char in binary_int:
        if char != '0' and char != '1':
            valid = False
            break
    if valid:
        break
    binary_int = input("Invalid input. Enter a binary number:")

decimal_op = int(binary_int, 2)
    
print(decimal_op)


#  write a function that takes a number as an argument and if the number
# 		divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if is is
# 		divisible by both return "FizzBuzz"

def FizzBuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FIZZBUZZ"
    elif num % 3 == 0 :
        return "FIZZ"
    elif num % 5 == 0 :
        return "buzz"
    else:
        return 0
    
num = int(input("enter num for fizzbuzz: "))
print(FizzBuzz(num))
#- Ask the user to enter the radius of a circle print its calculated area and circumference
raduis = float(input("enter radius: "))
import math
area = raduis*raduis*math.pi
circumference =2*raduis*math.pi
print(f"area :{area}")
print(f"circumference : {circumference}")
#- Ask the user for his name then confirm that he has entered his name (not an empty string/integers). then proceed to ask him for his email and print all this data

name = input("What's your name? ")

while not name.isalpha():
    print("Please enter a valid name (not empty or nums).")
    name = input("What's your name? ")


email = input("What's your email? ")
while '@' not in email:
    print("Please enter a valid email")
    email = input("What's your email? ")


print(f"Name: {name}")
print(f"Email: {email}")



#- Write a program that prints the number of times the substring 'iti' occurs in a  string

itis = input("enter iti string: ")
count = itis.count("iti")
print(count)
