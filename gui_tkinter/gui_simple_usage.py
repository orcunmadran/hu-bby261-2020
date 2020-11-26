#http://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html

from tkinter import Tk, Label, Button
#TK main window of our application
#Our application should only have one root
#it is possible to create other windows which are separate from the main window

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        #Window Title

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

        #Button and Label should be self-explanatory. Each of them has a parent widget, which we pass in as the first parameter to the constructor – we have put the label and both buttons inside the main window, so they are the main window’s children in the tree. We use the pack method on each widget to position it inside its parent – we will learn about different kinds of layout later.

    def greet(self):
        print("Greetings!")

root = Tk()
#We are using three widgets: Tk is the class which we use to create the root window – the main window of our application. Our application should only have one root, but it is possible for us to create other windows which are separate from the main window.

my_gui = MyFirstGUI(root)
#There are many ways in which we could organise our application class. In this example, our class doesn’t inherit from any tkinter objects – we use composition to associate our tree of widgets with our class. We could also use inheritance to extend one of the widgets in the tree with our custom functions.

root.mainloop()
#root.mainloop() is a method on the main window which we execute when we want to run our application. This method will loop forever, waiting for events from the user, until the user exits the program – either by closing the window, or by terminating the program with a keyboard interrupt in the console.
