# Anisort README

**Version 1.0.0** - [Change log](CHANGELOG.md) s

Anisort is a simple sorting program to create a list of item sorted by the user's preference. Originally, it was designed to create a sorted to-watch list of anime but you could probably use it for different items as well. Can't imagine what else you might want to sort besides anime.

---

## Installation
You can run the program either directly by opening the exe or you can launch the Python script from the command line, if you know how to do that. Make sure to run it as a Python 3 script though (-3), the default Py2 option will execute but doesn't work properly.
**Make sure that anime_input.txt is available in the same directory, otherwise the program will error.** If you want to append to an existing list, anime_load.txt needs to be available as well.

## How to Use
Before running the program, you will need to feed it items to sort by adding them to the "anime_input.txt" file. Each item must be separated by a line break.
If you want to add new items to an existing list, the *existing* list should be added to "anime_load.txt" and the *new* items to "anime_input.txt".
If you run the program, you will be asked if you want to sort a new list or (press N to choose) append items to an existing list (press A to choose). In either case, you will then be presented two items and asked to pick your favorite. This will continue until every item has been put into relation with every other and a list of your preferences has been create, at which point this sorted list will be output on screen and you will be asked if you want to save this list to "anime_output.txt". Please note that any existing version of "anime_output.txt" will be overwritten if you decided to save, so copy any list you want to keep to a different file.

## How the sorting works
Essentially, the current item being compared (the subject) is compared to an item in the middle of the existing list (the comparand). Depending on the choice, the list is the split in half and the top or bottom half becomes the new working list and the subject is compared to the item in the middle of that (first quarter or third quarter of the initial list). The list keeps being halfed until only one item remains and the subject is then added before or after that item.

---
## Stuff I Want To Add
- Currently, one comparand will appear twice for every subject. This doesn't really create any problems but is inelegant and needs to be fixed.
- Have the program display a customized warning if the necessary input files are missing instead of just crashing.
- Let the user pick an input file instead of having a hard-coded file name.
- Let the user pick name and location of the output file.
- Create some sort of "title screen"
- Maybe create a GUI
- Either change the buttons used for choosing items to arrow keys or create an option menu where the user gets to choose what buttons to use.

## License and Copyright

(c) Florian Frühwirth, 2019

Licensed under [GNU GPLv3](COPYING)
