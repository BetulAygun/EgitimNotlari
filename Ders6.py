#Fonksiyon

def ilk_fonksiyon():
    print("Tebrikler...")

ilk_fonksiyon()
def vizenotuoranı(vizenotu= 0):
    vize_notu_oranı = vizenotu * 0.4
    return vize_notu_oranı

def finalnotuoranı(finalnotu):
    final_notu_oranı = finalnotu * 0.6
    return final_notu_oranı

ogrenci_notu = vizenotuoranı() + finalnotuoranı(90)
print(ogrenci_notu)

#lambda, map, filter

# = lambda vizenotu = 0, finalnotu = 0: vizenotu * 0.4 + finalnotu*0.6
#print(lambda_fonksiyonu(80,60))

ogrenci_vizenotu= [20,50,66,78,34]
ogrenciler_finalnotu = [34,78,65,43, 12]
print(list(map(lambda vizenotu, finalnotu: vizenotu * 0.4 + finalnotu*0.6 ,
               ogrenci_vizenotu,  ogrenciler_finalnotu)))

#filter
donem_sonu_ortalama = [98,12,45,78,45,78,63,41]
devamsızlık = [2,3,4,5,6,3,4,5]

#print(list(filter(lambda sınav_notu, devam: (sınav_notu < 45 or devam > 5), donem_sonu_ortalama, devamsızlık)))

def kurdonusumu(paraTL):
    return paraTL / 11.8

kur_donusumu = lambda para_TL: para_TL / 11.8



paralar_TL = [10000,12000,58000,78000,96000]
paralar_USD = []
for para in paralar_TL:
    paralar_USD.append(round(kurdonusumu(para)))
#print(paralar_USD)


#print(list(map(lambda para_TL: round(para_TL / 11.8, 3), paralar_TL)))















