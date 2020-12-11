#SQLite3 kütüphanesi yükleniyor
import sqlite3

#veritabani.db adında bir SQLite3 veri tabanı dosyası oluşturuluyor.
veritabani = sqlite3.connect('veritabani.db')

#Veri tabanı üzerinde işlemleri gerçekleştirebilmek için bir Cursor objesi oluşturuluyor.
komut = veritabani.cursor()

# Veri tabanı içinde mesajlar adlı tablonun oluşturulması
komut.execute('''
              CREATE TABLE IF NOT EXISTS kisiler
             (id INTEGER PRIMARY KEY AUTOINCREMENT, ad text NOT NULL, soyad text NOT NULL, eposta text NOT NULL)
             ''')

# Yapılan işlemlerin kayıt edilmesi
veritabani.commit()

#Veri tabanındaki tabloları görüntüle
for tablolar in komut.execute('SELECT * FROM sqlite_master'):
        print(tablolar)

# Veri tabanı bağlantısı kapatılıyor
# Commit edilmeyen tüm değişiklikler silinecektir ve kayıt edilmeyecektir.
veritabani.close()