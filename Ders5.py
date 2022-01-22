# Döngüler
# input, print, if, while, for
#boolean - True False
sayi = 0
"""while (sayi == 0):
    print("Döngüdeyim.")
    sayi = int(input("Bir sayi giriniz..."))
    print("Sayi = ", sayi)
    print("Sayının iki katı = ", sayi*2)

print("sayi = ", sayi)"""

for sayidegerleri in range(2000, 2020): # liste 2000 2019
    print(sayidegerleri)
not_liste = [50, 45, 30, 45, 60]
devamsızlık = [3,5,1,0,4]
sonuc_liste = [] #sonuc_liste = list()
for indeks in range(0, len(not_liste)): #0, 1,2,3,4
    print(indeks)

    if (not_liste[indeks] < 45 or devamsızlık[indeks] > 4):
        sonuc_liste.append("Kaldı")
    elif (not_liste[indeks] >= 45 and devamsızlık[indeks] <= 4):
         sonuc_liste.append("Geçti")
    elif(not_liste[indeks] > 45 and devamsızlık[indeks] > 4):
        sonuc_liste.append("Kaldı")
    elif (not_liste[indeks] < 45 or devamsızlık[indeks] <= 4):
        sonuc_liste.append("Kaldı")

print(sonuc_liste)


#Veri Tipleri:
# int, float, str, list ([])
#tuple (demet), set (kume), dict (sözlük)

# Veri Tipi - Tuple() (Demet)
liste = [2,8,9]

tuple1 = (2,8,9,8,"8","metin", 10.5)
print(type(tuple1))
liste[0] = 5
print(tuple1[0:])
print(len(tuple1))
print(tuple1.count("8"))

#Veri Tipi - Kümeler (Set)
kume1 = {3,5,6,1,7,6, "metin", 10.5}
kume2 = {7,4,3,6,7}

print(kume1)
liste = [123,123,124,125,126]
print(list(set(liste)))
print(kume1.difference(kume2))

ogrenci_notlari = [{"İsim": "Betul" , "AraSınav": 80, "Final": 90},
                   {"İsim": "Ayşe", "Final": 92}, {"İsim": "Ahmet", "AraSınav": 25}]




ogrenci_notları = ["Betul",25,80]
donem_sonu_notu = ogrenci_notları[1]*0.4 + ogrenci_notları[2]*0.6

liste_sonuc=[]
for sozluk in ogrenci_notlari:
    print(sozluk)
    donem_sonu_not = 0
    isim = ""
    for anahtar, deger in sozluk.items():
        print(anahtar,deger)
        if (anahtar == "AraSınav"):
            donem_sonu_not = donem_sonu_not + deger * 0.4
        if(anahtar == "Final"):
            donem_sonu_not = donem_sonu_not + deger * 0.6
        if(anahtar == "İsim"):
            isim = deger

    liste_sonuc.append((isim, round(donem_sonu_not)))

print(liste_sonuc)
# Fonksiyon Tanımlama
def ilk_fonksiyon():
    print("Tebrikler...")

def kareal(sayi=0):
    print(sayi**2)

kareal(12)

def üsalma(sayi1=1,sayi2=1):
    return sayi1**sayi2

print(üsalma(4,8))

def not_ortalamasi(notlar = [0,0,0]):
    sonuc = notlar[0] * 0.2 + notlar[1]*0.3 + notlar[2]*0.5
    return sonuc

liste = [[23,0,67],[45,0,89],[12,0,56], [23,45,67],[45,67,89],[12,34,56], [23,45,67],[45,67,89],[12,34,56],[23,45,67],[45,67,89],[12,34,56],]
liste_sonuc = list()
for ogrenci in liste:
    liste_sonuc.append(round(not_ortalamasi(ogrenci)))
print(liste_sonuc)


#not_degeri = not_ortalamasi(50,80,12)
#print(not_degeri)

ogrenci = {"İsim": "Betul" , "AraSınav": 80, "Final": 90}
print(ogrenci.get("İsim", "Bulunamadı"))
print(ogrenci["Final"])

ogrenci["İsim"] = "Ayşe"
print(ogrenci.get("İsim", "Bulunamadı"))
ogrenci.pop("AraSınav")
print(ogrenci)
liste = ["Betul"]



# Oyun Yazma - Tahmin Oyunu Bilgisayar sayi tutacak
import random
rastegelesayi = random.randint(0,100)




def karealma(sayi):
    print(sayi**2)
    return sayi**2



sonuc = (karealma(9) * 5) / 6

print(sonuc)




















