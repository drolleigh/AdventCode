#  Dylan Rolleigh
#  Day: 4
#  This class contains methods for checking number of
#  fields and the key values of existing fields

import numpy as np
import pandas as pd

class MyPassportClass:
    def __init__(self, entry):
        self.entry = entry
        self.passport = []
        self.fields = {}
        self.required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        self.num_valid = 0

    def sort_pairs(self, entry):
        print('TEST in sort pairs what is entry', entry)
        for line_item in entry:
            print('TEST in for loop in sort pairs')
            pairs = line_item.split(' ')
            k, v = pairs.split(':')
            self.fields[k.strip()] = v.strip()
            print('IN SORTED PAIRS kv FIELDS', self.fields)
            self.passport.append(self.fields)
        return(self.passport)


    # def num_valid(self, entry):
    #     for pair in entry.split(' '):
    #         k, v = pair.split(':')
    #         self.fields[k.strip()] = v.strip()
    #         self.passport.append(self.fields)
    #         print('passport_keyvalues', self.passport)

        #  COMMENTED OUT SO I CAN TEST THE ABOVE WORK
        # for key_pair in self.passport():
        #     for key in self.required_keys:
        #         if key not in key_pair.key():
        #             break
        #         else:

    # def field_checker(self, passport):


########## CANT GET MY CLASS TO IMPORT INTO MAIN SO THIS IS TESTING WORK-AROUND
def pp_reader():
    with open('../day4_input_test.txt', "r") as text_file:
        pp_raw = text_file.readlines()
    return pp_raw


# entry = pp_reader()
# passports = []

for line in pp_reader():
    entry = []
    if line is not '\n':
        entry.append(line)
        print('ENTRY before sending to class', entry)
    else:
        this_passport = MyPassportClass(entry)
        sorted_pairs = this_passport.sort_pairs(entry)
        print('SORTED PAIRS', sorted_pairs)

        # print('THIS PASSSPORT', this_passport)
        # passport_keyValues = pc.num_valid()
        # print('this_passport', passport_keyValues)
        # if this_passport.is_valid():
            # num_valid += 1






