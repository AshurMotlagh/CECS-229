# Ashur Motlagh
# 018319910
# September (9)

import numpy

print("remainder of id over 3 is: ", 18319910 % 3)
matrix = numpy.array(
    [[12, 5, 3, 74, 52], [23, 41, 12, 41, 23], [17, 36, 9, 8, 11], [19, 23, 14, 9, 11], [8, 2, 29, 37, 28]])
birthdayMat = numpy.array([[11, 32, 26, 28, 17]])

print("12 times matrix: ", numpy.dot(12, matrix))  # A

print("Det of matrix: ", numpy.linalg.det(matrix))  # B

print("Inverse of matrix: ",numpy.linalg.inv(matrix))  # C

print("Transpose of matrix: ", matrix.T)  # D

print("Trace of matrix: ", matrix.trace())  # E

print("Multiply matrix with inverse: ", numpy.dot(matrix, numpy.linalg.inv(matrix)))  # F

print("Multiply matrix with matrix: ", numpy.dot(matrix,matrix))  # G

print("Matrix minus inverse: ", numpy.subtract(matrix, numpy.linalg.inv(matrix)))  # H

eig = numpy.linalg.eig(matrix)  # I
print("Eigan Value: ", eig[0])
print("Eigan Vector: ", eig[1])

print("Second row with month of birth: ", matrix[1] * 9)  # J

print("Thrid column with month of birth: ", matrix[:, 2] * 9)  # K

secRow = matrix[1] * 2  # L
print("Add first row with seconds row then replace: ", numpy.add(matrix[0],secRow))

print("Solve equation Ax=B: ", numpy.multiply((numpy.linalg.inv(matrix)), birthdayMat))  # M

