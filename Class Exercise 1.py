import math
from math import *

A = 18319910
B = A / 9
firstprimelist = []
firstprimelist2 = []

sin(A)  # 2

1/tan(A)  # 4 cos(A)/sin(A)

log10(A)  # 6

log(A, 7)  # 8

B**(-7)  # 10

(abs(-1)**B) * B  # 12

math.ceil(B)  # 14

math.floor(B)  # 16

max(A, B, 9)  # 18

min(A, B, 9)  # 20

A**(1/5)  # 22

A/B  # 24

for i in range(0,round(5*B)+1):  # 26
    if i > 1:
        for i in range(2, i):
            if (i % i) == 0:
                break
        else:
            firstprimelist.append(i)

if(((-1)**B) == -1): # 28
    True
else:
    False

name = input("What is your name: ")  # 30
id = int(input("What is your ID: "))
print("This is your name ", name, "and your id: ", id)

# The Extra point
for i in range(round(B),round(5*B)+1):
    if i > 1:
        for i in range(2, i):
            if (i % i) == 0:
                break
        else:
            firstprimelist2.append(i)