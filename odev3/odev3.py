# ODEVLER
# 1-)Kullanıcıdan bir input alınız. Input'taki küçük harfleri büyük harfe dönüştüren bir program yazınız.
# Ör input: Hello World!
# Ör output: HELLO WORLD!

# deger = input('bir deger giriniz:')
# print(deger.upper())

# 2-)Kullanıcıdan bir input alınız. Girmiş olduğu inputta büyük harf sayısı, küçük harf sayısı,
# rakam sayısı ve bunların haricindeki özel karakter sayılarını veren bir program yazınız.

kelime = input("Herhangi bir kelime: ")
buyuk=kucuk=rakam=haric=0
for harf in kelime:
    if(harf.isupper()):
       buyuk+=1
    elif(harf.islower()):
        kucuk+=1
    elif (harf.isdigit()):
        rakam+=1
    else:
        haric+=1
print(f'buyuk harf sayisi {buyuk}\nkucuk harf sayisi {kucuk}\nrakam sayisi {rakam}\ndiger karakter {haric}')

# 3-)Kullanıcıdan bir input alınız. Girmiş olduğu inputtaki rakamların toplamını veren bir program yazınız.
# (Kullanıcı rakam girmek zorunda değil.
# farklı karakter girişi de yapabilir.)
# Örnek input = "art12kl4*"

# kelime = input("Herhangi bir kelime: ")
# toplam=0
# for sayi in kelime:
#     if (sayi.isdigit()):
#         toplam+=int(sayi)
#
# print(f'girdiginiz inputtaki sayilar toplami: {toplam}')

# 4-)Futbolcular dosyasındaki futbolculardan ismi sesli harf ile başlayanları ayrı bir dosyaya yazdırınız.
# f = open('futbolcular', 'r')
# f2 = open('sesliler.txt', 'w')
# sesli = 'aeiou'
# for i in f:
#     if (i[0].lower() in sesli):
#         print(i, end='', file=f2)

# 5-)Futbolcular dosyasındaki futbolcu isimlerini yazdığınız program ile Türkçe karakter içermeyecek bir
# hale getirip yeni bir dosyaya kaydediniz.
f = open('futbolcular', 'r')
ftrans = open('translate.txt', 'w')
kaynak = "şçöğüıŞÇÖĞÜİ"
hedef = "scoguiSCOGUI"
for i in f:
    print(i.translate(str.maketrans(kaynak, hedef)), file=ftrans)
