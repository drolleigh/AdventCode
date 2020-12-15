# Author: Dylan Rolleigh
# Day: 4

import numpy as np
import passport_checker as pc

def pp_reader():
    with open('../day4_input_test.txt', "r") as text_file:
        pp_raw = text_file.readlines()
    return pp_raw


pp_raw = pp_reader()  # passport raw data line by ling
# print('pp_raw', pp_raw)
passports = []

# this_passport = pc()
for line in pp_raw:
    entry = []
    if line is not '\n':
        entry.append(line)
        print('ENTRY', entry)
    else:
        this_passport = pc.sort_pairs(entry)
        print('THIS PASSSPORT', this_passport)
        # passport_keyValues = pc.num_valid()
        # print('this_passport', passport_keyValues)
        # if this_passport.is_valid():
            # num_valid += 1
























# def pp_reader():
#     with open('day4_input_test.txt', "r") as text_file:
#         pp_raw = text_file.readlines()
#     return pp_raw
#
# pp_raw = pp_reader()
# # print(pp_raw)
# # pp_list = np.zeros((len(pp_raw), 1), dtype=str)
# # print(pp_list)
# pp_list = []
# j = 0
# for i in range(len(pp_raw)):
#     if pp_raw[i] != '/n':
#         pp_list.append(pp_raw[i])
#         # print('pp_list', pp_list)
#         print('pp_raw', pp_raw[i])
#         # data_string = ' ' + pp_raw[i]
#         # pp_list[j] = pp_raw[i]
#     else:
#         j += 1

# print('pp_list[0]', pp_list[0])
# print('pp_list', pp_list)


# pp_list = []
# pp_lines = str.strip(pp_raw)
# print(pp_lines)
