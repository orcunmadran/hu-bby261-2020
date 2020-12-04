#SQLite3 kütüphanesi yükleniyor
import sqlite3

#veritabani.db adında bir SQLite3 veri tabanı dosyası oluşturuluyor.
veritabani = sqlite3.connect('veritabani.db')

#Veri tabanı üzerinde işlemleri gerçekleştirebilmek için bir Cursor objesi oluşturuluyor.
komut = veritabani.cursor()

#Veri tabanındaki mesajlar tablosu sorgulanıyor ve sonuçlar ekrana yazdırılıyor.
for kayitlar in komut.execute('SELECT * FROM mesajlar'):
        print(kayitlar)

# Veri tabanı bağlantısı kapatılıyor
veritabani.close()