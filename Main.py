from TelefonRehberi import *

k = TelefonRehberi()

print("""
|------------------------------------------------|
|   Telefon Rehberi Uygulamasına Hoş Geldiniz    |
|------------------------------------------------|
""")

while True:

    print("""
    |----------------------------|
    | Seçim ediniz:              |
    |                            |
    |   1.Kayıtları Listele      |
    |   2.Kayıt Ara              |
    |   3.Kayıt Ekle             |
    |   4.Kayıt Sil              |
    |   5.Çıkış                  |
    |                            |                           
    |----------------------------|
    """)

    secim = input("Seçim ediniz: ")

    if secim == "1":
        k.kaytlariListele()
    elif secim == "2":
        isim = input("Aranacak kişinin ismini giriniz: ")
        k.kayitAra(isim)

    elif secim == "3":
        k.kayitEkle()

    elif secim == "4":
        kisi = input("Silmek istediğiniz kişinin adını giriniz: ")

        k.kayitSil(kisi)

    elif secim == "5":
        baglanti.close()
        break

    else:
        print("Yalnış seçim. Lütfen doğru seçim ediniz.")