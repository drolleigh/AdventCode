# Author: Dylan Rolleigh
# Day: 1

import numpy as np
import pandas as pd
import csv

# Read data in from .csv
results = []
with open("day1_input_2.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        results.append(row)
print(results)
# Convert list to array
data = np.zeros(len(results))
for i in range(len(results)):
    number = results[i]
    data[i] = number[0]

print(data)

# Find pairs that sum to 2020
for i in range(len(data)):
    for j in range(i+1, len(data), 1):
        if data[i] + data[j] == 2020:
            print(data[i], data[j])
            times2 = data[i]*data[j]
            print('times2 = ', times2)

# Find triples that add to 2020
for i in range(len(data)):
    for j in range(i+1, len(data), 1):
        for k in range(i+2, len(data), 1):
            if data[i] + data[j] + data[k] == 2020:
                print(data[i], data[j], data[k])
                times3 = data[i]*data[j]*data[k]
                print('times3 =', times3)







