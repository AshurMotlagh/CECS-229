# Ashur Motlagh
# 018319910
# September (9)

#  -------------------------------------------- Number 1 ---------------------------------------------------------------
grade = (60 + 18319910) % 33
print("uh ohh someone needs a grade boost: ", grade)

while (True):
    if 90 <= grade <= 100:
        grade += 10
    elif 80 <= grade <= 90:
        grade += 15
    elif 70 <= grade <= 80:
        grade += 20
    elif 60 <= grade <= 70:
        grade += 25
    elif 50 <= grade <= 60:
        grade += 30
    elif 40 <= grade <= 50:
        grade += 35
    elif 30 <= grade <= 40:
        grade += 40
    elif 20 <= grade <= 30:
        grade += 45
    if grade > 100:
        grade -= 1
        if grade == 100:
            break
print("Your new grade is: ", grade)
print()

#  -------------------------------------------- Number 2 ---------------------------------------------------------------
count = 0
sum = 0.0
number = 1

while number != 0:
    number = int(input("Input some integers to calculate their sum and average. Input 0 to exit."))
    sum += number
    count += 1

print("Average and Sum of the above numbers are: ", sum / (count - 1), sum)

#  -------------------------------------------- Number 3 ---------------------------------------------------------------
rows = 12
month = 9
for num in range(rows + 1):
    for i in range(num):
        if num > 9:
            print(month + 6, end=" ")
        else:
            print(num, end=" ")  # print number
    print(" ")
