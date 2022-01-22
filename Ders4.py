# While Dongusun
# For Dongusunu
# Boolean - True False
"""sayi = int(input("***Lütfen sayı giriniz..."))
toplam = 0
while (sayi != 0):
    sayi = int(input("Lütfen sayi giriniz..."))
    toplam = toplam +sayi
print(toplam)"""

liste = [15, 78, 98, 78, 34, 56, 78, 89, 34, "Girmedi", "Girmedi", 54]

toplam = 0
sinavagiren_ogrenci_sayisi = 0
for ogrenci_notu in liste:
    print("Ogrencinin Notu = ", ogrenci_notu)
    print("Önceki Toplam : ", toplam)
    if ogrenci_notu != "Girmedi":
        toplam = toplam + ogrenci_notu
        sinavagiren_ogrenci_sayisi = sinavagiren_ogrenci_sayisi + 1
    print("Sonraki toplam : ", toplam)



ortalama = toplam / sinavagiren_ogrenci_sayisi
print("Öğrencilerin Ortalamaı = ", ortalama)

for i in range(2000,2022,3): # [0,1,2,3,4,5,6,7,8,9]
    print(i)
#list()
ogrenci_listesi = [["Betul", 20, 56],["Ahmet", 20, 88],["Ayse", 25, 74],["Fatma", 77,12],["Ali", 12, 74]]

for ogrenci_bilgisi in ogrenci_listesi:
    print(ogrenci_bilgisi)
    notu = ogrenci_bilgisi[1] * 0.4 + ogrenci_bilgisi[2] *0.6
    print("Ogrenci Adı : {} Öğrencinin Donem Sonu Notu : {}".format(ogrenci_bilgisi[0], notu))

notu = ogrenci_listesi[0][1] * 0.4 + ogrenci_listesi[0][2] *0.6
print("Ogrenci Adı : {} Öğrencinin Donem Sonu Notu : {}".format(ogrenci_listesi[0][0], notu))

notu = ogrenci_listesi[1][1] * 0.4 + ogrenci_listesi[1][2] *0.6
print("Ogrenci Adı : {} Öğrencinin Donem Sonu Notu : {}".format(ogrenci_listesi[1][0], notu))

notu = ogrenci_listesi[2][1] * 0.4 + ogrenci_listesi[2][2] *0.6
print("Ogrenci Adı : {} Öğrencinin Donem Sonu Notu : {}".format(ogrenci_listesi[2][0], notu))

# Veri Tipi - Dictinary()
sozluk = {{"İsim": "Betul" , "AraSınav": 80, "Final": 88}, {"İsim": "Ayşe", "Final": 92}, {"İsim": "Ahmet", "AraSınav": 25}}

# Veri Tipi - Tuple() (Demet)
tuple1 = (2,8,9)

# Veri Tipi - Set Küme
kume1 = set()
liste = ["Doktor", "Muhendis", "Öğretmen", "Doktor"]
kume2= set(liste)
print(kume2)

a = 1
while (a == 10):
    print(a)
    a= a+1

for i in range(1,10):
    print(i)











