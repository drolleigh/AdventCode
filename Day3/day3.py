# Author: Dylan Rolleigh
# Day: 3

import numpy as np

def map_reader():
    with open('day3_input_test.txt', "r") as text_file:
        policy = text_file.readlines()
    return policy

map = map_reader()
# print(map)

row = 11
col = 11
pattern_rpt = 3
total_col = col*pattern_rpt


matrix = []
for sub in map:
    matrix.append(list(sub))
for i in range(len(matrix)):
    matrix_temp = matrix[i]
    matrix_temp.pop()
    matrix[i] = matrix_temp

map_matrix = np.zeros((row, total_col), dtype=str) # creates empty matrix to fill with map

for i in range(row):
    matrix_row = matrix[i]*pattern_rpt
    for j in range(total_col):
        map_matrix[i, j] = matrix_row[j]
print('WINNER = ', map_matrix)

for i in range