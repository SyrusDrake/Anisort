# Anisort README

**Version 2.0.0** - [Change log](CHANGELOG.md)

Anisort is a simple sorting program to create a list of item sorted by the user's preference. Originally, it was designed to create a sorted to-watch list of anime but you could probably use it for different items as well. Can't imagine what else you might want to sort besides anime.

---

## Installation
You can run the program either directly by opening the exe or you can launch the Python script from the command line, if you know how to do that. Make sure to run it as a Python 3 script though (-3), the default Py2 option will execute but doesn't work properly.

## How to Use
I think/hope the new GUI version is largely self-explanatory. If you have a new, completely unsorted list of items, choose "new" when prompted. You can then either enter the items by hand or import them from a txt-file. You will then be asked to choose your favorite of pairs until all items are sorted. To do so, you can either click the buttons or use the indicated keyboard keys.  
The Append function lets you add items to an already sorted list. The items you input or load are the NEW items. The existing list will be loaded when you continue.

## How the sorting works
Essentially, the current item being compared (the subject) is compared to an item in the middle of the existing list (the comparand). Depending on the choice, the list is the split in half and the top or bottom half becomes the new working list and the subject is compared to the item in the middle of that (first quarter or third quarter of the initial list). The list keeps being halfed until only one item remains and the subject is then added before or after that item.

---
## Stuff I Want To Add
- Maybe a better GUI
- Auto-save while the user is sorting

## License and Copyright

(c) Florian Frühwirth, 2020

Licensed under [GNU GPLv3](COPYING)
