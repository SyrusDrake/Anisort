#Florian Fuehwirth
#01.11.2018
#[description goes here]

import math

subject = "NIL"
input_file = open("anime_input.txt")
input_array = input_file.read().splitlines()
working_array = []
comparand = 0
place = 0

def save_file(final_array):
    output_file = open("anime_output.txt", "w")
    for line in final_array:
        output_file.write(line)
        output_file.write("\n")
    output_file.close()
    return

choice = input("Welcome. Do you want to sort a (n)ew list or (a)pend to an existing list from \"anime_load.txt\"?")
if choice == "n":
    sorted_array = [input_array.pop(0)]

if choice == "a":
    load_file = open("anime_load.txt")
    sorted_array = load_file.read().splitlines()


while True:
    subject = input_array.pop(0)
    working_array = sorted_array

    save_file(sorted_array)

    while True:
        comparand = math.floor((len(working_array)/2))

        if len(working_array) > 0:
            print ("Do you prefer", subject, "(1) or", working_array[comparand], "(2)")
            choice = input("Choose one: ")

            if choice == "1":
                if len(working_array) > 1:
                    working_array = working_array[0:comparand]

                else:
                    place = sorted_array.index(working_array[comparand])
                    sorted_array.insert(place, subject)
                    break

            if choice == "2":
                if len(working_array) > 1:
                    working_array = working_array[comparand:len(sorted_array)]

                else:
                    place = sorted_array.index(working_array[comparand])+1
                    sorted_array.insert(place, subject)
                    break



    if len(input_array) == 0:
        print("Sorted list is", sorted_array)
        choice = input("Do you want to save the list to a file? y/n")
        if choice == "y":
            save_file(sorted_array)
            break
        if choice == "n":
            break
