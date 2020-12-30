# Dylan's AOC Day 7

# Read file into a list with each element representing a rule
def main():
    with open('day7_input.txt', "r") as file:
        lines = file.read().splitlines()
    print('lines', lines)

    # Add colors that directly hold shiny gold
    gold_container = []
    gold_container_old = []
    for line in lines:
        bags_held = line.split('contain')[1]  # Prevents rules that start with shiny gold from being counted
        print('bag_held', bags_held)
        if 'shiny gold' in bags_held:
            color_holds_gold = line.split()[0] + ' ' + line.split()[1]  # grabs first two words in line
            gold_container.append(color_holds_gold)

    # While loop for adding colors that contain colors that contain shiny gold
    counter = 0
    while gold_container > gold_container_old:
        gold_container_old = gold_container
        for color in gold_container:
            for line in lines:
                bags_held = line.split('contain')[1]
                if color in bags_held:
                    color_holds_gold = line.split()[0] + ' ' + line.split()[1]
                    if color_holds_gold not in gold_container:
                        gold_container.append(color_holds_gold)

    print('gold container', gold_container)
    print('Number of colors that can hold shiny gold = ', len(gold_container))

# String form: '[color_1] bags contain [int] [color_2] bags, [int] [color_3] bags . . . [int] [color_n] bags.'
# color form: adjective[space]color
# Question: These strings are very long. Is using the split() function the best
# option, or could it possibly become tedious to debug? Also, I am not sure
# at the moment how to write the loop so that it will read the entire string
# no matter the length of the rule. Maybe it keeps splitting out the color_n
# until it reaches '.'???

# Loop for reading each rule: This first loop is looking for any
# color_1 that directly contains 'shiny gold'. Create a list, named gold_containers,
# which is a list of colors that can contain 'shiny gold' bags. Append color_1's to
# gold_containers. This means I will need to have temporary variables that store
# color_1 and all following split out color_n's. Then, any color_1+1 I will need to
# == 'shiny gold', if true, then gold_containers.append(color_1).

# Next, loop back through the rules to see if color_2 through color_n for each rule
# matches any item in the gold_containers list. If it does, then append that rule's
# color_1 to the gold_containers. Final answer = len(gold_containers).

if __name__ == "__main__":
    main()


