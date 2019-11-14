# replace()
###################################################################
# kardiz = "memleket"
# print(kardiz.replace("e", ""))
# print(kardiz.replace("e", "", 2))
# print(kardiz.replace("ket", "KET"))

# split(), rsplit(), splitlines()
###################################################################

# kardiz = "İstanbul Büyükşehir Belediyesi"
# print(kardiz.split())
#
# kardiz = input("Kısaltmasını öğrenmek istediğiniz kurum adını girin: ")
# for i in kardiz.split():
#     print(i[0], end="")

# kardiz = "Bolvadin, Kilis, Siverek, İskenderun, İstanbul"
# kardiz = kardiz.split(",")
# print(kardiz)
# for i in kardiz:
#     print(i)
#
# kardiz = "Ankara Büyükşehir Belediyesi"
# print(kardiz.split(" ", 1))
# print(kardiz.split(" ", 2))
# print(kardiz.rsplit(" ", 1))
#
# metin = """Python programlama dili Guido Van Rossum adlı Hollandalı bir programcı
# tarafından 90'lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan, isminin
# Python olmasına bakarak, bu programlama dilinin, adını piton yılanından aldığını
# düşünür. Ancak zannedildiğinin aksine bu programlama dilinin adı piton yılanından
# gelmez. Guido Van Rossum bu programlama dilini, The Monty Python adlı bir İngiliz
# komedi grubunun, Monty Python's Flying Circus adlı gösterisinden esinlenerek
# adlandırmıştır. Ancak her ne kadar gerçek böyle olsa da, Python programlama
# dilinin pek çok yerde bir yılan figürü ile temsil edilmesi neredeyse bir gelenek
# halini almıştır diyebiliriz."""
#
# for i, j in enumerate(metin.splitlines()):
#     print(i + 1, j)


# lover() # upper() # islower(), #isupper()
#########################################################################
# kişi = input("Aradığınız kişinin adı ve soyadı: ")
# kişi = kişi.lower()
# if kişi == "ahmet":
#     print("email: aoz@hmail.com")
#     print("tel : 02121231212")
#     print("şehir: istanbul")
# elif kişi == "mehmet":
#     print("email: msoz@zmail.com")
#     print("tel : 03121231212")
#     print("şehir: ankara")
# elif kişi == "mahmut":
#     print("email: mgoz@jmail.com")
#     print("tel : 02161231212")
#     print("şehir: istanbul")
# else:
#     print("Aradığınız kişi veritabanında yok!")
#
# kardiz = "kalem"
# print(kardiz.upper())
# kardiz = "istihza"
# print(kardiz.islower())
# kardiz = 'Oguzhan'
# print(kardiz.islower())
# print(kardiz.isupper())

# endswith() startswith()
#########################################################################
# kardiz = "istihza"
# print(kardiz.endswith("a"))
#
# d1 = "python.ogg"
# d2 = "tkinter.mp3"
# d3 = "pygtk.ogg"
# d4 = "movie.avi"
# d5 = "sarki.mp3"
# d6 = "filanca.ogg"
# d7 = "falanca.mp3"
# d8 = "dosya.avi"
# d9 = "perl.ogg"
# d10 = "c.avi"
# d11 = "c++.mp3"
# for i in d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11:
#     if i.endswith(".mp3"):
#         print(i)

# kardiz = "python"
# print(kardiz.startswith("p"))


# capitalize() title() swapcase()
#########################################################################
# a = "python programlama dili"
# print(a.capitalize())
# print(a.title())
#
# kardiz = "on iki ada"
# for kelime in kardiz.split():
#     if kelime.startswith("i"):
#         kelime = "İ" + kelime[1:]
#     kelime = kelime.title()
#     print(kelime, end=" ")

# kardiz = "pYtHoN"
# print(kardiz.swapcase())


# strip(), lstrip(), rstrip()
#########################################################################
# kardiz = " istihza "
# print(kardiz)
# print(kardiz.strip())


# metin = """
# > Python programlama dili Guido Van Rossum adlı Hollandalı bir programcı tarafından
# > 90'lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan, isminin Python
# > olmasına bakarak, bu programlama dilinin, adını piton yılanından aldığını düşünür.
# > Ancak zannedildiğinin aksine bu programlama dilinin adı piton yılanından gelmez.
# > Guido Van Rossum bu programlama dilini, The Monty Python adlı bir İngiliz komedi
# > grubunun, Monty Python's Flying Circus adlı gösterisinden esinlenerek adlandırmıştır.
# > Ancak her ne kadar gerçek böyle olsa da, Python programlama dilinin pek çok yerde
# > bir yılan figürü ile temsil edilmesi neredeyse bir gelenek halini almıştır diyebiliriz.
# """
# for i in metin.splitlines():
#     print(i.strip("> "))


# kardiz = 'kazak'
# print(kardiz.lstrip('k'))
# print(kardiz.rstrip('k'))

# join()
#########################################################################
# kardiz = "Beşiktaş Jimnastik Kulübü"
# parcala = kardiz.split()
# print(parcala)
# print(' '.join(parcala))

# count()
#########################################################################
# sehir = "Kahramanmaraş"
# print(sehir.count('a'))
#
# kelime = input("Herhangi bir kelime: ")
# sayac = ""
# for harf in kelime:
#     if harf not in sayac:
#         sayac += harf
# print("sayaç içeriği: ", sayac)
# for harf in sayac:
#     print(f"{harf} harfi {kelime} kelimesinde {kelime.count(harf)} kez geçiyor!")

#########################################################################
#########################################################################

