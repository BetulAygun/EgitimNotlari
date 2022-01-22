# Veri Tipleri - int (tamsayı)
# yas = 56

import math

# Veri Tipleri - float (ondalıklı sayı)
kilo = 60.5
print(type(kilo))

# Veri Tipleri - String (Metin)
isim = "Ganite"
dogum_yeri = "Ankara"
kilo = 80
print(type(kilo))

#Veri Tipleri - Liste
kilolar = [80, 60.5, 82, 55.6]

#Dönüştürme İşlemleri - Veri Tipleri
metin = 15.5
print(int(metin), float(metin), str(metin))

print("Bu kişinin isimi {}, Doğduğu yer {} ve kilosu {} dır.".format(isim, dogum_yeri, kilo))

#ekrandanalinanbilgi_boy = input("Lütfen boyunuzu giriniz >>> ")
#ekrandanalinanbilgi_kilo = input("Lütfen kilonuzu giriniz >>> ")

#Operatörler
#Çarpma * , + , -, /, **
# vucut_kitle_indeksi = ekrandanalinanbilgi_boy / (ekrandanalinanbilgi_kilo**3)
# print("Bu kişinin vucut kitle indeksi = {}".format(vucut_kitle_indeksi))

sayi1= 25
sayi2= 3
print(sayi1**sayi2)
print(math.sqrt(sayi1))

#Veri Tipleri - Mantık - (Boolean- Bool) Doğru- Yanlış (True, False)
sonuc = True
# Mantık Operasyonlarında AND (VE), OR (VEYA)
# True AND True --> True Dışındakilerin hepsi False dönüyor
# False OR False --> False Dışındakilerin hepsi True dönecek.

#Veri Tipi - Liste - list()
#İndeks - 0'dan başlar
liste_notlar = [20, 98, 45, 45, 55, 67, 78, 84, 76, 87]
print(type(liste_notlar))
print("Birinci öğrencimin notu = ", liste_notlar[0])
print("Son öğrencimin notu = ", liste_notlar[-1], liste_notlar[9])
print(sorted(liste_notlar, reverse= True))

print(len(liste_notlar))
print(sum(liste_notlar) / len(liste_notlar))

tercih_listesi = ["Cumartesi", "Pazar", "Cumartesi", "Cumartesi", "Pazartesi"]
print(tercih_listesi.count("Pazar"))
liste_notlar.append(99)
print(liste_notlar)
liste_notlar.pop(5)
liste_notlar.remove(45)
print(liste_notlar)

liste_ogrenci_not = ["Betul Aygun", 80, "Ayse Tutar", 82, "Ahmet Aydın", 56]
print(liste_ogrenci_not[0::2])
print(liste_ogrenci_not[1::2])
liste_icine_liste = [["Betul Aygun", 80],["Ayse Tutar", 82], ["Ahmet Aydın", 56]]
print(liste_icine_liste[-1][0].split()[0])

#If (Eğer) koşulu nasıl yazılır.
liste_notlar = [20, 98, 45, 45, 55, 67, 78, 84, 76, 87]
ogrenci_notu = 45

if (ogrenci_notu >= 80):
    print("Tebrikler...")
    deger = input("Durumdan memnun musun? = ")
    print(deger)
elif (ogrenci_notu >= 50):
    print("Geçtin...")
else:
    print("Kaldın..")


































