# Author: Dylan Rolleigh
# Day: 2

import numpy as np
import pandas as pd
import csv

# Read text file of strings
def check_keyword():
    with open('day2_input_copy.txt', "r") as text_file:
        words = text_file.readlines()
    return words

# Create password list
password_list = check_keyword()

####### Part 1 #######
valid_passwords = 0
for i in range(len(password_list)):
    password_temp = password_list[i]
    if password_temp is not "\n":
        split_limits = password_temp.split(' ')[0] # Save 'lowlimit-uplimit' string
        lowlimit = int(split_limits.split('-')[0]) # Save 'lowlimit' as int
        uplimit = int(split_limits.split('-')[1]) # Save 'uplimit' as int
        split_letter = password_temp.split(':')[0]
        letter = split_letter.split(' ')[1] # Save letter
        word = password_temp.split(' ')[2] # sAve password string
        occur = word.count(letter)
        if occur >= lowlimit and occur <= uplimit:
            valid_passwords = valid_passwords + 1
    else:
        pass
print(valid_passwords)

####### Part 2 #######
valid_passwords = 0
for i in range(len(password_list)):
    password_temp = password_list[i]
    if password_temp is not "\n":
        split_pos = password_temp.split(' ')[0] # Save 'lowlimit-uplimit' string
        index1 = int(split_pos.split('-')[0]) # Save 'lowlimit' as int
        index2 = int(split_pos.split('-')[1]) # Save 'uplimit' as int
        split_letter = password_temp.split(':')[0]
        letter = split_letter.split(' ')[1]
        word = password_temp.split(' ')[2]
        check1 = 0
        check2 = 0
        if word[index1-1] == letter:
            check1 = 1
        if word[index2-1] == letter:
            check2 = 1
        sum_check = check1 + check2
        if sum_check == 1:
            valid_passwords = valid_passwords + 1
    else:
        pass
print(valid_passwords)

