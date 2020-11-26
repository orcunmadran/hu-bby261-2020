#http://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html

#We can create quite complicated layouts with pack by grouping widgets together in frames and aligning the groups to our liking – but we can avoid a lot of this complexity by using the grid method instead. It allows us to position widgets in a more flexible way, using a grid layout. This is the geometry manager recommended for complex interfaces:

from tkinter import Tk, Label, Button, W
#Add W for grid layout

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.grid(columnspan=2, sticky=W)

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.grid(row=1)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=1, column=1)

    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()

#We place each widget in a cell inside a table by specifying a row and a column – the default row is the first available empty row, and the default column is 0.

#If a widget is smaller than its cell, we can customise how it is aligned using the sticky parameter – the possible values are the cardinal directions (N, S, E and W), which we can combine through addition. By default, the widget is centered both vertically and horizontally, but we can make it stick to a particular side by including it in the sticky parameter. For example, sticky=W will cause the widget to be left-aligned horizontally, and sticky=W+E will cause it to be stretched to fill the whole cell horizontally. We can also specify corners using NE, SW, etc..

#To make a widget span multiple columns or rows, we can use the columnspan and rowspan options – in the example above, we have made the label span two columns so that it takes up the same space horizontally as both of the buttons underneath it.

# NOTE! Never use both pack and grid inside the same window. The algorithms which they use to calculate widget positions are not compatible with each other, and your program will hang forever as tkinter tries unsuccessfully to create a widget layout which satisfies both of them.

#The third geometry manager is place, which allows us to provide explicit sizes and positions for widgets. It is seldom a good idea to use this method for ordinary GUIs – it’s far too inflexible and time consuming to specify an absolute position for every element. There are some specialised cases, however, in which it can come in useful.
