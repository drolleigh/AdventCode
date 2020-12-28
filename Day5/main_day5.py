#  Day 5 class and main

import numpy as np

class SeatReaderClass:
    def __init__(self, line):
        self.line = line
        self.seat = 128
        self.row_fronthalf = [0, 63]
        self.row_backhalf = [64, 127]
        self.col_fronthalf = [0, 3]
        self.col_backhalf = [4, 7]
        self.bisect_front = []
        self.bisect_back = []
        self.my_row = -1
        self.my_col = -1

    def bisect(self, range):
        range_front = range[0]
        range_back = range[1]
        middle = ((range_back - range_front) + 1)/2
        bisect_front = [range_front, range_front + middle-1]
        bisect_back = [range_front + middle, range_back]

        return bisect_front, bisect_back

    def seat_calc(self):
        """
         This method takes a binary seat description line
        and finds the row and column index with number
        of rows and columns starting at zero.
        """
        row_bisection = [0, 0]
        for letter in self.line[0:6]:
            if letter == 'F':
                row_bisection = self.bisect(self.row_fronthalf)
            elif letter == 'B':
                row_bisection = self.bisect(self.row_backhalf)
            self.row_fronthalf = row_bisection[0]
            self.row_backhalf = row_bisection[1]
        if self.line[6] == 'F':
            self.my_row = row_bisection[0][0]
        elif self.line[6] == 'B':
            self.my_row = row_bisection[1][0]

        col_bisection = [0, 0]
        for letter in self.line[7:9]:
            if letter == 'L':
                col_bisection = self.bisect(self.col_fronthalf)
            elif letter == 'R':
                col_bisection = self.bisect(self.col_backhalf)
            self.col_fronthalf = col_bisection[0]
            self.col_backhalf = col_bisection[1]
        if self.line[9] == 'L':
            self.my_col = col_bisection[0][0]
        elif self.line[9] == 'R':
            self.my_col = col_bisection[1][0] # Now picking one number from array, in the method!!!

        return self.my_row, self.my_col

#######  Entry into main #######
def s_reader():
    with open('day5_input.txt', "r") as text_file:
        s_raw = text_file.readlines()

    return s_raw


num_rows = 128
num_columns = 8
seats = np.ones([num_rows, num_columns])


def main():
    lines = s_reader()
    # print('seats raw', lines)
    max_id = 0

    for line in lines:
        not_my_seat_calc = SeatReaderClass(line)  # returns a tuple (row, col)
        not_my_seat = not_my_seat_calc.seat_calc()
        not_my_row = int(not_my_seat[0])  # Why did I have to convert to integer?
        not_my_col = int(not_my_seat[1])
        this_id = not_my_row * 8 + not_my_col
        if this_id > max_id:
            max_id = this_id

        seats[[not_my_row], [not_my_col]] = 0  # This switches the NOT seat to a 0

    print('MAX ID', max_id)

    for rw in range(num_rows):
        for cl in range(num_columns):
            if seats[[rw], [cl]] == 1:
                my_row = rw
                my_cl = cl
                seat_id = my_row * 8 + my_cl
                print('My unique seat ID = ', seat_id)  # Note, seats = [0:69] and [827:1023] are not filled on plane.


if __name__ == "__main__":
    main()