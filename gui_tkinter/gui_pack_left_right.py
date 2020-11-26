#http://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html

from tkinter import Tk, Label, Button, LEFT, RIGHT
#Add LEFT, RIGHT

#The GUI in the previous example has a relatively simple layout: we arranged the three widgets in a single column inside the window. To do this, we used the pack method, which is one of the three different geometry managers available in tkinter. We have to use one of the available geometry managers to specify a position for each of our widgets, otherwise the widget will not appear in our window.

#By default, pack arranges widgets vertically inside their parent container, from the top down, but we can change the alignment to the bottom, left or right by using the optional side parameter. We can mix different alignments in the same container, but this may not work very well for complex layouts. It should work reasonably well in our simple case, however:

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()
        self.greet_button.pack(side=LEFT)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()
        self.close_button.pack(side=RIGHT)

    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
