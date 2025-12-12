import random
kelime_secenekleri = ["Bilgisayar", "Telefon", "Yazılım", "Matematik"]
kelime = random.choice(kelime_secenekleri).lower()
tahmin_edilen = ["_"] * len(kelime)
can = 7
print("Adam Asmaca oyununa hoş geldiniz. Toplamda 3 yanlış harf hakkınız bulunmaktadır. Lütfen sadece 1 harf giriniz!")
print("".join(tahmin_edilen))
while "_" in tahmin_edilen and can > 0 :
    harf = input("Bir harf gir : ").lower()

    if harf in kelime:
        for i, h in enumerate(kelime):
            if harf==h:
                tahmin_edilen[i] = harf
        print("Doğru tahmin :) ")
    else:
        can-=1
        print("Yanlış harf girdiniz. Kalan canın : ", can)

    print("".join(tahmin_edilen))

if can==0:
    print("Oyunu kaybettiniz. Doğru kelime : ", kelime)
else:
    print("Oyunu kazandınız . ", kelime)

