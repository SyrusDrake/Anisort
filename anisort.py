# Florian Frühwirth
# 21.07.2019
# A program to load a list of items, sort it by comparing the user's preference of two items at a time and, if desired, save the sorted list.
# v1.0.1

import math

# <cf> Variables

subject = "NIL"                                 # The subject is the item that is being compared to the existing list
input_file = open("anime_input.txt")
input_array = input_file.read().splitlines()
working_array = []                              # working_array is empty to start out
comparand = 0                                   # comparand is the item in the existing list that the subject is being compared to
place = 0                                       # The place in the existing list where the new item will be placed

# </cf>


def save_file(final_array):                     # The function which creates the output file
    output_file = open("anime_output.txt", "w")
    for line in final_array:
        output_file.write(line)
        output_file.write("\n")
    output_file.close()
    return


if len(input_array) < 3:
    print("Please provide a list with more than 2 entries")
else:
    choice = input("Welcome. Do you want to sort a (n)ew list or (a)pend to an existing list from \"anime_load.txt\"?")
    if choice == "n":
        sorted_array = [input_array.pop(0)]     # Puts the first item of the input list into the sorted array

    if choice == "a":
        load_file = open("anime_load.txt")
        sorted_array = load_file.read().splitlines()    # Creates an array from the input file

    while True:
        subject = input_array.pop(0)    # The first item of the input array becomes the subject
        working_array = sorted_array

        save_file(sorted_array)

        while True:
            comparand = math.floor((len(working_array) / 2))  # The item in the middle of the existing list becomes the current comparand

            if len(working_array) > 0:  # Makes sure there are items left
                print("Do you prefer", subject, "(1) or", working_array[comparand], "(2)")
                choice = input("Choose one: ")

                if choice == "1":
                    if len(working_array) > 1:
                        working_array = working_array[0:comparand]  # If the subject is preffered, the half of the list ABOVE the comparand is "selected" for further comparison

                    else:   # If only the starting item is present in the list
                        place = sorted_array.index(working_array[comparand])
                        sorted_array.insert(place, subject)     # The subject is placed in front of the comparand
                        break

                if choice == "2":
                    if len(working_array) > 1:
                        working_array = working_array[comparand:len(sorted_array)]  # If comparand is preffered, the half of the list BELOW the comparand is "selected" for further comparison

                    else:   # If only the starting item is present in the list
                        place = sorted_array.index(working_array[comparand]) + 1
                        sorted_array.insert(place, subject)     # The subject is placed behind the comparand
                        break

        if len(input_array) == 0:   # If all items have been checked
            print("Sorted list is", sorted_array)   # The sorted array is output
            choice = input("Do you want to save the list to a file? y/n")
            if choice == "y":
                save_file(sorted_array)
                break
            if choice == "n":
                break
