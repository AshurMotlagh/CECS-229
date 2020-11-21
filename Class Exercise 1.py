# Ashur Motlagh
# 018319910

import math
from math import *

A = 18319910
B = A % 9
C = A / 9
primelist = []
extraCreditPrimeNumbers = []

print(sin(A))  # 2

print(1/tan(A))  # 4 cos(A)/sin(A)

print(log10(A))  # 6

print(log(A, 7))  # 8

print(B**(-7))  # 10

print((abs(-1)**B) * B)  # 12

print(math.ceil(C))  # 14

print(math.floor(C))  # 16

print(max(A, B, 9))  # 18

print(min(A, B, 9))  # 20

print(A**(1/5))  # 22

print(A/B)  # 24

for i in range(int(B), int(5 * B)):
    if i > 1:
        for j in range(2,i):
            if (i % j) == 0:
                break
        else:
            primelist.append(i)
print(primelist)


if(((-1)**B) == -1): # 28
    print("this is true")
else:
    print("this is false")

name = input("What is your name: ")  # 30
id = int(input("What is your ID: "))
print("This is your name ", name, "and your id: ", id)

# The Extra point
num = int(input("Enter a number: "))
for i in range(num, 5 * num):
    if i > 1:
        for j in range(2,i):
            if (i % j) == 0:
                break
        else:
            extraCreditPrimeNumbers.append(i)
print(extraCreditPrimeNumbers)
print(len(extraCreditPrimeNumbers))
