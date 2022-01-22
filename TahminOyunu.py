import random

oyunun_devam_durumu = True
while oyunun_devam_durumu:
    print("Oyun yeniden başladı...")
    tutulansayi = random.randint(1,100)
    print(tutulansayi)
    tahmin_sayisi = 0
    dongunun_devam_etme_durumu = True

    while dongunun_devam_etme_durumu:
        tahmin_edilen_sayi = int(input("Tahminde bulununuz..."))
        tahmin_sayisi = tahmin_sayisi + 1
        if (tahmin_edilen_sayi == tutulansayi):
            print("Tebrikler. {}. Kerede Doğru Tahmin Ettiniz.".format(tahmin_sayisi))
            dongunun_devam_etme_durumu = False
        elif (tahmin_edilen_sayi < tutulansayi):
            print("Daha büyük bir sayı tahmininde bulununuz.")
        else:
            print("Daha küçük bir sayı tahmininde bulununuz.")

    deger = input("Oyuna devam etmek istiyor musunuz? (Evet/Hayır)")
    if deger == "Hayır":
        oyunun_devam_durumu = False



