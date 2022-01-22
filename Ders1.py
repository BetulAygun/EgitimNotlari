
yas = 38 #int
print(type(yas))
kilo = 60.2

isim = "Betül"


print("Kulanıcının Yası  = {}".format(yas))

print(isim, yas, kilo)

""" yas = input("Lütfen Yaşınızı Giriniz: ")

not_ortalaması = 82

print("Kulanıcının Yası  = {}, Kullanıcının Adı = {}".format(yas))
print("Kulanıcının Yası  = {}".format(yas))
yas = 77
print("Kulanıcının Yası  = {}".format(yas)) 
"""

#Veri Tipleri Liste Tuple Dictionary Set Küme
#İndeksler tutar - indeksler 0'dan başlar
ogrenci_notları = [82,78,96,25,65,45]
print(type(ogrenci_notları))
print(ogrenci_notları[0])
print(ogrenci_notları[1])
satir_bilgisi = "   Betül Aygün,1545213,4,3.50"
#String Operasyonları
yeni_liste = satir_bilgisi.split(sep=",")
buyuk_harf = satir_bilgisi.upper()
kucuk_harf = satir_bilgisi.lower()

print(yeni_liste)
print(buyuk_harf)
metin2 = "    Betul  Aygun     "
print(metin2.strip())
print(metin2.replace("u","ü").strip())
mailadresi1 = "betularac@gmail.com"
mailadresi2 = "betulaygunarac@hotmail.com"

print(mailadresi1[0:9])
print(mailadresi2[0:14])
print(mailadresi2.split(sep="@")[0])

notu = int(input("Notunu Gir :"))
if notu < 50:
    print("Kaldı")
else:
    print("Geçti")



























