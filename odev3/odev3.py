# ODEVLER
# 1-)Kullanıcıdan bir input alınız. Input'taki küçük harfleri büyük harfe dönüştüren bir program yazınız.
# Ör input: Hello World!
# Ör output: HELLO WORLD!

# deger = input('bir deger giriniz:')
# print(deger.upper())

# 2-)Kullanıcıdan bir input alınız. Girmiş olduğu inputta büyük harf sayısı, küçük harf sayısı,
# rakam sayısı ve bunların haricindeki
# özel karakter sayılarını veren bir program yazınız.

# s = input("bir deger giriniz:")
# digit = 0
# if any(i.isdigit() for i in s):
#     digit +=1
# print(digit)


while True:
    s = input("Bir sayı girin: ")
    if s == "iptal":
        break
    if len(s) <= 3:
        continue
    print("En fazla üç haneli bir sayı girebilirsiniz.")



# 3-)Kullanıcıdan bir input alınız. Girmiş olduğu inputtaki rakamların toplamını veren bir program yazınız.
# (Kullanıcı rakam girmek zorunda değil.
# farklı karakter girişi de yapabilir.)
# Örnek input = "art12kl4*"

# 4-)Futbolcular dosyasındaki futbolculardan ismi sesli harf ile başlayanları ayrı bir dosyaya yazdırınız.
# 5-)Futbolcular dosyasındaki futbolcu isimlerini yazdığınız program ile Türkçe karakter içermeyecek bir
# hale getirip yeni bir dosyaya kaydediniz.