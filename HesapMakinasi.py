import time
#islem veri tipi str
hesap_makinesi_durumu = True
while hesap_makinesi_durumu:
    sayi1 = float(input("1. Sayıyı Giriniz. >"))
    islem = input("Lütfen Yapmak İstediğiniz işlemi giriniz... (Toplama : + Çıkarma:- Çarpma:* Bölme: /)")
#sayi1, sayi2 veri tipi int
    sayi2= float(input("2. Sayıyı Giriniz. >"))

    if (islem == "+"):
        sonuc = sayi1 + sayi2
    elif (islem == "-"):
        sonuc = sayi1 - sayi2
    elif (islem == "*"):
        sonuc = sayi1 * sayi2
    elif (islem == "/"):
        sonuc = sayi1 / sayi2
    else:
        sonuc = "Yanlış bir işlem girdiniz..."

    print("İşlem : {} {} {} = {}".format(sayi1, islem, sayi2, sonuc))

    cıkmak = input("Hesap Makinasından Çıkmak İster misiniz? (Evet/Hayır)")
    if cıkmak == "Evet":
        hesap_makinesi_durumu = False























