from tkinter import Tk, Label, Button

class uygulamaPencerem:
    def __init__(self, anaSayfa):
        self.anaSayfa = anaSayfa
        anaSayfa.title("test")

        self.etiket = Label(anaSayfa, text="Test")
        self.etiket.pack()

        self.islemButonu = Button(anaSayfa, text="İşlemi Uygula", command=self.yazdir)
        self.islemButonu.pack()

        self.kapatButonu = Button(anaSayfa, text="Kapat", command=anaSayfa.quit)
        self.kapatButonu.pack()

    def yazdir(self):
        print("Merhaba Grafik Arayüz ;)")

root = Tk()
yeniPencere = uygulamaPencerem(root)
root.mainloop()
