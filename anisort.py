# Florian Frühwirth
# 15.07.2020
# A program to load a list of items, sort it by comparing the user's preference of two items at a time and, if desired, save the sorted list.
# v2.0.0

import tkinter.filedialog
import tkinter as tk
import math


class MainApp:

    def __init__(self, master):
        self.master = master

        # All the necessary variables
        self.input_array = []
        self.sorted_array = []
        self.subject = ''
        self.working_array = []
        self.comparand = 0

        # A list of all pages
        self.pages = [
            WelcomePage,
            SortPage,
            EndPage,
            AppendPage,
            NewPage
        ]

        # All pages get put in this "master frame"
        frame_container = tk.Frame(master)
        frame_container.pack(side='top', fill='both', expand=True)
        frame_container.grid_rowconfigure(0, weight=1)
        frame_container.grid_columnconfigure(0, weight=1)

        self.pagedict = {}

        # Populates a dictionary of all pages. The values are the actual pages
        for p in (self.pages):
            name = p.__name__
            new_frame = p(location=frame_container, controller=self)  # The frame class is called and created
            self.pagedict[name] = new_frame
            new_frame.grid(row=0, column=0, sticky='nswe')

        self.show_frame('WelcomePage')

    def reset(self):
        app.input_array = []
        app.sorted_array = []
        app.subject = ''
        app.working_array = []
        app.comparand = 0
        self.show_frame('WelcomePage')

    # The function to switch pages
    def show_frame(self, page_name):
        frame = self.pagedict[page_name]
        frame.update(frame.controller)
        frame.tkraise()

    def choice1(self):
        if len(self.working_array) > 1:
            self.working_array = self.working_array[0:self.comparand]  # If the subject is preffered, the half of the list ABOVE the comparand is "selected" for further comparison
            self.sort_loop()

        else:   # If only the starting item is present in the list
            place = self.sorted_array.index(self.working_array[self.comparand])
            self.sorted_array.insert(place, self.subject)     # The subject is placed in front of the comparand
            self.main()

    def choice2(self):
        if len(self.working_array) > 2:
            self.working_array = self.working_array[self.comparand:len(self.sorted_array)]  # If comparand is preferred, the half of the list BELOW the comparand is "selected" for further comparison
            self.sort_loop()

        else:   # If only the starting item is present in the list
            self.place = self.sorted_array.index(self.working_array[self.comparand]) + 1
            self.sorted_array.insert(self.place, self.subject)     # The subject is placed behind the comparand
            self.main()

    def main(self):
        if len(self.input_array) > 0:
            self.subject = self.input_array.pop(0)   # The first item of the input array becomes the current subject
            self.working_array = self.sorted_array
            self.sort_loop()
        else:
            self.show_frame('EndPage')

    def sort_loop(self):
        self.comparand = math.floor((len(self.working_array) / 2))  # The item in the middle of the existing list becomes the current comparand

        if len(self.working_array) > 0:  # Makes sure there are items left
            self.pagedict['SortPage'].update(self.pagedict['SortPage'].controller)

        else:
            self.main()

    def save_file(self, array):  # The function which creates the output file
        filename = tkinter.filedialog.asksaveasfilename(filetypes=[('Save file', '*.txt')])
        save_file = open(filename, "w+")
        for line in array:
            save_file.write(line)
            save_file.write("\n")
        save_file.close()


class WelcomePage(tk.Frame):
    def __init__(self, location, controller):
        tk.Frame.__init__(self, location)  # Creates the frame for this page
        self.controller = controller
        self.label = tk.Label(self, text='Welcome!\nDo you want to sort a new list or append to an existing list?')
        self.button1 = tk.Button(self, text='(N)ew', command=lambda: self.new_list(controller))
        self.button2 = tk.Button(self, text='(A)ppend', command=lambda: self.append_list(controller))

        controller.master.bind('n', lambda event: self.new_list(controller))
        controller.master.bind('a', lambda event: self.append_list(controller))

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.label.grid(row=0, columnspan=2, sticky='nsew')
        self.button1.grid(row=1, sticky='nsew', padx=35)
        self.button2.grid(row=1, column=1, sticky='nsew', padx=35)

    def new_list(self, controller):
        self.unbind(controller)
        controller.show_frame('NewPage')

    def append_list(self, controller):
        self.unbind(controller)
        controller.show_frame('AppendPage')

    def unbind(self, controller):
        controller.master.unbind('n')

    def update(self, controller):
        pass



class NewPage(tk.Frame):
    def __init__(self, location, controller):
        tk.Frame.__init__(self, location)
        self.controller = controller
        self.label = tk.Label(self, text='NewPage', height=2)
        self.button1 = tk.Button(self, command=lambda: self.start(controller))
        self.button2 = tk.Button(self, command=self.load)
        self.text = tk.Text(self, height=6)

        self.grid_rowconfigure(1, weight=2)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.label.grid(row=0, columnspan=3, sticky='nsew', pady=10)
        self.text.grid(row=1, columnspan=3, sticky='nsew', pady=10)
        self.button1.grid(row=2, sticky='nsew', padx=35)
        self.button2.grid(row=2, column=1, sticky='nsew', padx=35)

        controller.master.bind('<Alt_L><a>', lambda event: self.start(controller))
        controller.master.bind('<Alt_L><l>', lambda event: self.load())

    def update(self, controller):
        self.text.delete(1.0, tk.END)
        self.label.config(text='Enter items separated by line break.\nItems can be imported from text file.')
        self.button1.config(text='Start', underline=2)
        self.button2.config(text='Load', underline=0)

    def unbind(self, controller):
        controller.master.unbind('<Alt_L><a>')
        controller.master.unbind('<Alt_L><l>')

    def load(self):
        input_file = open(tkinter.filedialog.askopenfilename(filetypes=[('Text', '*.txt')]))
        string = input_file.read()
        self.text.insert(1.0, string)

    def start(self, controller):
        str = self.text.get(1.0, tk.END)
        array = str.split('\n')
        while ('' in array):
            array.remove('')

        if len(array) < 3:
            self.label.config(text='Please provide a list with more than 2 entries', fg='red')
        else:
            app.input_array = array
            app.sorted_array = [app.input_array.pop(0)]     # Puts the first item of the input list into the sorted array
            app.subject = app.input_array.pop(0)
            app.working_array = app.sorted_array
            self.unbind(controller)
            app.show_frame('SortPage')  # Switches page


class AppendPage(tk.Frame):
    def __init__(self, location, controller):
        tk.Frame.__init__(self, location)
        self.controller = controller
        self.label = tk.Label(self, text='AppendPage', height=2)
        self.button1 = tk.Button(self, command=lambda: self.append(controller))
        self.button2 = tk.Button(self, command=self.load)
        self.text = tk.Text(self, height=6)

        self.grid_rowconfigure(1, weight=2)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.label.grid(row=0, columnspan=3, sticky='nsew', pady=10)
        self.text.grid(row=1, columnspan=3, sticky='nsew', pady=10)
        self.button1.grid(row=2, sticky='nsew', padx=35)
        self.button2.grid(row=2, column=1, sticky='nsew', padx=35)

        controller.master.bind('<Alt_L><a>', lambda event: self.append())
        controller.master.bind('<Alt_L><l>', lambda event: self.load())

    def update(self, controller):
        self.text.delete(1.0, tk.END)
        self.label.config(text='Enter NEW items, separated by line break.\nExisting list will be loaded when clicking "append".')
        self.button1.config(text='Append', underline=0)
        self.button2.config(text='Load', underline=0)

    def unbind(self, controller):
        controller.master.unbind('<Alt_L><a>')
        controller.master.unbind('<Alt_L><l>')

    def load(self):
        input_file = open(tkinter.filedialog.askopenfilename(filetypes=[('Text', '*.txt')]))
        string = input_file.read()
        self.text.insert(1.0, string)

    def append(self, controller):
        str = self.text.get(1.0, tk.END)
        array = str.split('\n')
        while ('' in array):
            array.remove('')
        input_file = open(tkinter.filedialog.askopenfilename(filetypes=[('Text', '*.txt')]))
        append_array = input_file.read().splitlines()

        if len(array+append_array) < 3:
            self.label.config(text='Please provide a list with more than 2 entries', fg='red')
        else:
            app.input_array = array
            app.sorted_array = append_array     # Puts the first item of the input list into the sorted array
            app.subject = app.input_array.pop(0)
            app.working_array = app.sorted_array
            app.comparand = math.floor((len(app.working_array) / 2))
            self.unbind(controller)
            app.show_frame('SortPage')  # Switches page


class SortPage(tk.Frame):

    def __init__(self, location, controller):
        tk.Frame.__init__(self, location)
        self.controller = controller
        self.label = tk.Label(self, text='SortPage')
        self.button1 = tk.Button(self)
        self.button2 = tk.Button(self)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.label.grid(row=0, columnspan=2, sticky='nsew')
        self.button1.grid(row=1, sticky='nsew', padx=35)
        self.button2.grid(row=1, column=1, sticky='nsew', padx=35)

        controller.master.bind('a', lambda event: app.choice1())
        controller.master.bind('l', lambda event: app.choice2())

    def update(self, controller):
        self.label.config(text='Which do you prefer?')
        self.button1.config(text=f'{app.subject} (A)', command=self.test)
        self.button2.config(text=f'{app.working_array[app.comparand]} (L)', command=app.choice2)

    def test(self):
        app.choice1()


class EndPage(tk.Frame):
    def __init__(self, location, controller):
        tk.Frame.__init__(self, location)
        self.controller = controller
        self.label = tk.Label(self, text='EndPage', height=2)
        self.button1 = tk.Button(self)
        self.button2 = tk.Button(self)
        self.button3 = tk.Button(self)
        self.text = tk.Text(self, height=6)

        self.grid_rowconfigure(1, weight=2)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.label.grid(row=0, columnspan=3, sticky='nsew', pady=10)
        self.text.grid(row=1, columnspan=3, sticky='nsew', pady=10)
        self.button1.grid(row=2, sticky='nsew', padx=35)
        self.button2.grid(row=2, column=1, sticky='nsew', padx=35)
        self.button3.grid(row=2, column=2, sticky='nsew', padx=35)

        controller.master.bind('<Alt_L><y>', lambda event: app.save_file(app.sorted_array))
        controller.master.bind('<Alt_L><n>', lambda event: root.quit())
        controller.master.bind('<Alt_L><r>', lambda event: app.reset())

    def update(self, controller):
        controller.master.unbind('a')
        controller.master.unbind('l')
        self.text.delete(1.0, tk.END)
        for items in app.sorted_array:
            self.text.insert(tk.END, items + '\n')
        self.label.config(text='Do you want to save the sorted list?')
        self.button1.config(text='Yes', underline=0, command=lambda: app.save_file(app.sorted_array))
        self.button2.config(text='No', underline=0, command=root.quit)
        self.button3.config(text='Restart', underline=0, command=lambda: app.reset())


root = tk.Tk()
root.geometry('500x500+1400+400')
root.title('Anisort')
app = MainApp(root)
root.mainloop()
