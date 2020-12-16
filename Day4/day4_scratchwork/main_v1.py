import re


class MyPassportClass:

    def __init__(self, entry):
        self.entry = entry
        self.passport = []
        self.fields = {}
        self.required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        self.process_entry()  


    def is_valid(self):
        """
        This method should inspect the key-value pairs created in the
        method `process_entry` and verify whether or not all the key-value pairs
        constitute a valid passport or not.
        """

        # Test whether every element in required_keys is in actual_keys
        actual_keys = set(self.fields.keys())
        required_keys = set(self.required_keys)
        has_required_keys = required_keys <= actual_keys
        if not has_required_keys:
            return False

        # TODO: Complete the following block. 

        # Assume all is valid at first, then as soon as one invalid
        # is detected, whole thing becomes invalid.
        all_valid = True 

        # Now iterate over each key-value pair to check
        for key, value in self.fields.items():
            if key == 'byr':
                this_key_valid = len(str(value)) == 4 and (1920 <= value <= 2002)
                all_valid = all_valid and this_key_valid
            if key == 'iyr':
                this_key_valid = len(str(value)) == 4 and (2010 <= value <= 2020)
                all_valid = all_valid and this_key_valid
            if key == 'eyr':
                this_key_valid = len(str(value)) == 4 and (2020 <= value <= 2030)
                all_valid = all_valid and this_key_valid
            if key == 'hgt':
                if len(str(value)) < 4:
                    all_valid = False
                else:
                    ending = value[-2:]
                    num = int(value[:-2])
                    this_key_valid = (ending == 'in' and (59 <= num <= 76)) or (ending == 'cm' and (150 <= num <= 193))
                    all_valid = all_valid and this_key_valid
            if key == 'hcl':
                re_str = '#[0-9a-f]{6}'
                this_key_valid = re.search(re_str, str(value)) is not None and len(str(value)) == 7
                all_valid = all_valid and this_key_valid
            if key == 'ecl':
                this_key_valid = value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
                all_valid = all_valid and this_key_valid
            if key == 'pid':
                re_str = '[0-9]{9}'
                this_key_valid = re.search(re_str, str(value)) is not None and len(str(value)) == 9
                all_valid = all_valid and this_key_valid
            if key == 'cid':
                this_key_valid = True
                all_valid = all_valid and this_key_valid

        # If all fields are valid, return True
        return all_valid


    def process_entry(self):
        """
        This method should be called upon initialization to do the string
        processing as soon as an instance of MyPassportClass is created. 

        It should take a list of strings `self.entry` and process each string
        into key-value pairs. 

        With the way the attribute are defined in this class, I
        do not have to pass anything into this method, and it doesn't have
        to return anything.
        """

        for line_item in self.entry:
            pairs = line_item.split(' ')
            for pair in pairs:
                if ':' in pair:
                    key, value = pair.split(':')
                    if value.isdigit():
                        self.fields[key] = int(value)
                    else:
                        self.fields[key] = value


def pp_reader():
    with open('../day4_input.txt', "r") as text_file:
        pp_raw = text_file.readlines()
    return pp_raw
    

def main():
    entry = []
    count = 0
    lines = pp_reader()
    for line in lines:
        if not line.isspace() and line is not lines[-1]:
            entry.append(line.splitlines()[0])
        else:
            this_passport = MyPassportClass(entry)
            # print("this_passport.fields = ")
            # print(this_passport.fields)
            # print()
            if this_passport.is_valid():
                count += 1
            entry = []
    print(count)    # Final answer


if __name__ == "__main__":
    main()