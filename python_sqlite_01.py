#SQLite3 kütüphanesi yükleniyor
import sqlite3

#veritabani.db adında bir SQLite3 veri tabanı dosyası oluşturuluyor.
veritabani = sqlite3.connect('veritabani.db')

#Veri tabanı üzerinde işlemleri gerçekleştirebilmek için bir Cursor objesi oluşturuluyor.
komut = veritabani.cursor()

# Veri tabanı içinde mesajlar adlı tablonun oluşturulması
komut.execute('''
              CREATE TABLE mesajlar
             (ad text, soyad text, eposta text, mesaj text)
             ''')

# Yapılan işlemlerin kayıt edilmesi
veritabani.commit()

# Veri tabanı bağlantısı kapatılıyor
# Commit edilmeyen tüm değişiklikler silinecektir ve kayıt edilmeyecektir.
veritabani.close()