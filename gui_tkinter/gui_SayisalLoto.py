from random import randint
from tkinter import Tk, Label, Button, Entry

class sayisalLoto:
    def __init__(self, anasayfa):
        self.anasayfa = anasayfa
        anasayfa.title("Şanslı numaralarını öğren!")

        self.baslik = Label(anasayfa, text="---::: Şanslı Numaraların :::---")
        self.baslik.config(font=("Arial", 22))
        self.baslik.pack()

        self.numaralar = Entry(anasayfa, text="Numaralar oluşturuluyor...")
        self.numaralar.config(width=50)
        self.numaralar.pack()

        self.yeniden = Button(anasayfa, text="Yeni numara oluştur..!", command=self.numaraOlustur)
        self.yeniden.pack()

        self.kapat = Button(anasayfa, text="Kapat", command=anasayfa.quit)
        self.kapat.pack()

    def numaraOlustur(self):
        i = 0
        self.numaralar.delete(0, 'end')
        secilenler = [0, 0, 0, 0, 0, 0]
        while i < len(secilenler):
            secilen = randint(1, 49)
            if secilen not in secilenler:
                secilenler[i] = secilen
                i += 1
        sansliNumaralar = str((sorted(secilenler)))
        self.numaralar.insert(0, sansliNumaralar)

root = Tk()
sayisalLotom = sayisalLoto(root)
sayisalLotom.numaraOlustur()
root.mainloop()
