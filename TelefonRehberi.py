import sqlite3

baglanti = sqlite3.connect("TelefonRehberi.db")
cursor = baglanti.cursor()


class Kisi():
    def __init__(self,isim,soyisim,numara):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara

class TelefonRehberi():

    def __init__(self):
        self.tabloOlustur()

    def tabloOlustur(self):
        cursor.execute("CREATE TABLE IF NOT EXISTS TELREHBERI (Isim TEXT, Soyisim TEXT, Telefon TEXT)")
        baglanti.commit()

        # Burasi Tamam dogru calisiyor


    def kaytlariListele(self):
        cursor.execute("Select * From TELREHBERI")
        veri = cursor.fetchall()

        print("________________________________")
        print("Telefon Rehberindeki Kişiler")
        print("________________________________")


        for i in veri:
            print("__________________________")
            print(f"Ad: {i[0]}\nSoyad: {i[1]}\nNumara: {i[2]}")
            print("__________________________")

        # Burasi Tamam dogru calisiyor

    def kayitAra(self,isim):

        cursor.execute("Select * From TELREHBERI where Isim = ?",(isim,))
        veri = cursor.fetchall()

        for i in veri:
            print("__________________________")
            print(f"Ad: {i[0]}\nSoyad: {i[1]}\nNumara: {i[2]}")
            print("__________________________")

        # Burasi Tamam dogru calisiyor


    def kayitEkle(self):
        isim = input("Isim Giriniz: ")
        soyisim = input("Soyisim Giriniz: ")
        numara = input("Numara Giriniz: ")

        kisi = Kisi(isim,soyisim,numara)

        cursor.execute("INSERT INTO TELREHBERI VALUES(?,?,?)",(kisi.isim,kisi.soyisim,kisi.numara))
        baglanti.commit()

        # Burasi Tamam dogru calisiyor


    def kayitSil(self,isim):
        cursor.execute("Delete From TELREHBERI where Isim = ?",(isim,))
        baglanti.commit()

        # Burasi Tamam dogru calisiyor
