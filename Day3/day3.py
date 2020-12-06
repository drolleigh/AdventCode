# Author: Dylan Rolleigh
# Day: 3

import numpy as np

def map_reader():
    with open('day3_input.txt', "r") as text_file:
        policy = text_file.readlines()
    return policy

map = map_reader()
# print(map)

# Build map in matrix form and pop off '/n'
matrix = []
for sub in map:
    matrix.append(list(sub))
for i in range(len(matrix)):
    matrix_temp = matrix[i]
    matrix_temp.pop()
    matrix[i] = matrix_temp

# Dimension of pattern
# row = 11
# col = 11
row = 323
col = 31

# Step sizes
step_right = 1
step_down = 2

# Calculate matrix size
total_step_right = step_right*row
pattern_rpt = -(-total_step_right // col)
total_col = col*pattern_rpt

# creates empty matrix to fill with map elements
map_matrix = np.zeros((row, total_col), dtype=str)

# Fill empty matrix of string zeroes with elements from map
for i in range(row):
    matrix_row = matrix[i]*pattern_rpt
    for j in range(total_col):
        map_matrix[i, j] = matrix_row[j]
# print('map_matrix = ', map_matrix)

# Check elements in map matrix for # when using step sizes
trees = 0
j = step_right
for i in range(step_down, row, step_down):
    map_matrix_line = map_matrix[i]
    # print('i',i)
    # print('map_matrix_line', map_matrix_line)
    # print('map_matrix_line[j]', map_matrix_line[j])
    if map_matrix_line[j] == '#':
        trees = trees + 1
    j = j + step_right
    # print('j', j)

print('trees', trees)
answer = 70*220*63*76*29
print('answer', answer)
