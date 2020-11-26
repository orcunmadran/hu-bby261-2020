from tkinter import Tk, Label, Button
from PIL import Image, ImageTk

class uygulamaPencerem:
    def __init__(self, anaSayfa):
        self.anaSayfa = anaSayfa
        anaSayfa.title("test")

        self.etiket = Label(anaSayfa, text="Test")
        self.etiket.pack()

        self.foto = Image.open("bisiklet_01.jpg")
        self.tkimage = ImageTk.PhotoImage(self.foto)
        self.resim = Label(root, image=self.tkimage)
        self.resim.pack()

        self.kapatButonu = Button(anaSayfa, text="Kapat", command=anaSayfa.quit)
        self.kapatButonu.pack()

root = Tk()
yeniPencere = uygulamaPencerem(root)
root.mainloop()
