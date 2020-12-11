#SQLite3 kütüphanesi yükleniyor
import sqlite3

#veritabani.db adında bir SQLite3 veri tabanı dosyası oluşturuluyor.
veritabani = sqlite3.connect('veritabani.db')

#Veri tabanı üzerinde işlemleri gerçekleştirebilmek için bir Cursor objesi oluşturuluyor.
komut = veritabani.cursor()

# Mesajlar tablosundan veri silinmesi
komut.execute("DELETE FROM kisiler WHERE id=1")

# Yapılan işlemlerin kayıt edilmesi
veritabani.commit()

for kayitlar in komut.execute('SELECT * FROM kisiler'):
        print(kayitlar)

# Veri tabanı bağlantısı kapatılıyor
veritabani.close()