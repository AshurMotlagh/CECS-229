import numpy

print("remainder of id over 3 is: ", 18319910 % 3)
matrix = numpy.array(
    [[12, 5, 3, 74, 52], [23, 41, 12, 41, 23], [17, 36, 9, 8, 11], [19, 23, 14, 9, 11], [8, 2, 29, 37, 28]])

print(numpy.dot(12, matrix))  # A

print(numpy.linalg.det(matrix))  # B

print(numpy.linalg.inv(matrix))  # C

print(matrix.T)  # D

print(matrix.trace())  # E

print(numpy.dot(matrix, numpy.linalg.inv(matrix)))  # F

print(numpy.dot(matrix,matrix))  # G

print(numpy.subtract(matrix, numpy.linalg.inv(matrix)))  # H


print(numpy.linalg.eigvals(matrix))  # J
print(numpy.linalg.eig(matrix))  # J
