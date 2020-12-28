# Dylan's AOC Day 6

def main():
    collection_union = set('')  # set of all the questions that have been answered `yes` by at least 1 person in the group
    collection_intersect = set('') # set of all the questions that have been answered `yes` by everyone in the group
    part1_total = 0 # variable to hold answer for part 1
    part2_total = 0 # variable to hold answer for part 2
    with open('day6_input.txt', "r") as file:
        lines = file.read().splitlines()
        if lines[-1]: # if last line is not an empty line, append with an empty one.
            lines.append('')
        for line in lines:
            # If both sets are empty, we know that we are starting with a new group. 
            # Start the collection with the first line in group rather than empty set (b/c the intersection of an empty set with any set is empty)
            if not collection_union and not collection_intersect and line: 
                collection_intersect = set(line)
            elif line: # update the intersection with current line, only if the current line isn't empty
                collection_intersect.intersection_update(line)

            collection_union.update(line) # find the union of the set with the current line

            if not line: # if line is empty or is the last one
                part1_total += len(collection_union) # number of unique elements among all sets in this collection
                part2_total += len(collection_intersect) # number of common elements among all sets in this collection
                collection_union = set('')
                collection_intersect = set('')
    print('Part 1: {:d}'.format(part1_total))
    print('Part 2: {:d}'.format(part2_total))

if __name__ == "__main__":
    main()
