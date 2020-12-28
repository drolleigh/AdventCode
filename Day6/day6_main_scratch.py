#  Dylan's AOC Day 6

class MyAnswerChecker():
    def __init__(self, group):
        self.group = None
        self.persons_ans = 

    def union_counter(self):
        for person in range(self.group):
            self.persons_ans.append(person)


        return union_count



#######  Entry into main #######
def ans_reader():
    with open('day6_input_test.txt', "r") as text_file:
        ans_raw = text_file.readlines()
    if not ans_raw[-1].isspace():  # This enables the last line of input to be stored
        ans_raw.append('\n')

    return ans_raw


def main():
    this_group = []
    ans_raw = ans_reader()
    print('answer', ans_reader())
    for line in ans_raw:
        if not line.isspace():
            this_group.append(line.splitlines()[0])
        elif this_group:
            num_unq_ans = MyAnswerChecker(this_group)
            print('The number of unique answer = ', num_unq_ans.union_counter())  # This is my ANSWER!
            print('this group', this_group)
            this_group = []


if __name__ == "__main__":
    main()