# 1. HAFTA ÖDEVLER
# 1-
# Input ile kullanıcıdan bir kelime yazmasını isteyip, bu kelimeyi altı çizili ve etrafı desenli bir şekilde printleyin.

kelime = input('bir kelime yazin:')
print(f"""
{'*'*(len(kelime)+6)}
*  {kelime}  *
*  {'-'*len(kelime)}  *
{'*'*(len(kelime)+6)}
""")


# 2-
# Kullanıcıdan input ile km cinsinden mesafe bilgisi alıp, bu bilgiyi mile dönüştürün ve sonucu ekrana printleyin.

# km = input('km cinsinden bir sayi giriniz')
# mil = 0.621371192 * float(km)
# print(f'girdiginiz km nin mil olarak karsiligi {mil} mildir')


# 3-
# Oğrenci not ortalama programi
# Icerik:
# Kullanicidan input ile ad-soyad, vize, final ve ders takip bilgilerini alip bu degerleri
# yuzdelik oranlarina gore hesaplayin ve yil sonu notunu cikarin.
# Yontem:
# -Sinav puanlari ve ders takip puani 0-100 arasidir.
# -Bir öğrencinin gitmesi gereken toplam ders sayısı 20’dir. Kaçırılan her ders için 5 puan kırılacaktır.
# (Orn: 3 ders kaciran bir ogrencinin ders takip puani: 100-(3x5)=85 )
# Oranlar :
# - Vize Notu ( 30%)
# - Final Notu (50%)
# - Ders takip (20%)
# Sonuc:
# 	0.	Output olarak ogrencinin yil sonu puanini ekrana pritleyin.
# 	0.	Ogrenci ad-soyad, vize-final-ders takip bilgilerini ve hesapladiginiz yil sonu puanini
# 	“ogrenciNotHesaplama” isimli bir dosyaya kaydedin.

# adiSoyadi = input('ad-soyad:')
# vize = float(input('vize:'))
# final = float(input('final:'))
# kacanDers =float(input('20 dersten kac ders kacirdiniz:'))
# dersTakibi = 100-(kacanDers * 5 )
# yilSonuNotu = 0.3*vize + 0.5*final + 0.2*dersTakibi
# f = open('ogrenciNotHesaplama', 'w')
# print(f'{adiSoyadi} olan ogrencinin yil sonu notu {yilSonuNotu} dur')
# print(f'{adiSoyadi} olan ogrencinin yil sonu notu {yilSonuNotu} dur', file=f)
# f.close()


# 4-
# Faiz hesaplama programi
# Kullanicidan gerekli bilgileri alip faiz tutarini hesaplayin.
# Bu programi calistirabilmeniz icin asagida belirtilen bilgileri input yardimi ile kullanicidan almaniz gerekmektedir.
# 	⁃	Ana para
# 	⁃	Faiz suresi (yil)
# 	⁃	Faiz orani
# Faiz hesaplama formulu: Ana para x faiz suresi x faiz orani / 100
# Sonuc:
# Gerekli islemleri yaptiktan sonra output olarak toplam faiz tutarini, aylik ve gunluk ortalama faiz tutarini,
# toplam para miktarini (faiz+ana para);
#   1) print ile ekrana yazin,
#   2) ”faizHesaplama” isimli bir dosyaya
#       kaydedin.
#
# anapara = float(input('Ana Para miktarini giriniz:'))
# faizsuresi = float(input('Faiz Suresini yil olarak giriniz:'))
# faizorani = float(input('Fazi oranini giriniz:'))
# faiz = anapara * faizsuresi * faizorani / 100
# aylikortfaiz = faiz / 12
# gunlukortfaiz = '{:04.2f}'.format(faiz / 365)
# toplampara = faiz + anapara
# print(f'Ana parasi {anapara} Euro olan parayi yillik %{faizorani} ile bankaya yatirirsak'
#       f' {faizsuresi} yillik surede toplam para {toplampara} olurken '
#       f'Aylik ortalama faiz {aylikortfaiz} ve gunluk ortalama faiz {gunlukortfaiz} dir')
# f = open('faizHesaplama', 'w')
# print(f'Ana parasi {anapara} Euro olan parayi yillik %{faizorani} ile bankaya yatirirsak'
#       f' {faizsuresi} yillik surede toplam para {toplampara} olurken '
#       f'Aylik ortalama faiz {aylikortfaiz} ve gunluk ortalama faiz {gunlukortfaiz} dir', file=f)
# f.close()


# 5-
# Aylik masraf programi
# Icerik:
# Aylık giderleri ve bu giderlerin aylik gelire oranini hesaplayan bir program yapmanız istenmektedir.
# Yontem:
# Asagida belirtilen harcama kalemlerini ve aylik geliri kullanicidan input ile alip gerekli hesaplamalari yapin
# Harcama kalemleri:
# -mutfak,
# -egitim,
# -giyim,
# -ulasim.
# Sonuc:
# 1-Kullanicinin aylik toplam masrafini ve bu masrafin aylik gelirine oranini ekrana printleyin.
# 2- Ayni sonucu “aylikmasraf” isimli bir dosyaya kaydedin.
# gelir = float(input('aylik gelirinizi giriniz:'))
# mutfak = float(input('mutfak giderini giriniz:'))
# egitim = float(input('egitim giderini giriniz:'))
# giyim = float(input('giyim giderini giriniz:'))
# ulasim = float(input('ulasim giderini giriniz:'))
# toplammasraf = mutfak + egitim + giyim + ulasim
# gelirgiderorani = '{:04.2f}'.format(gelir / toplammasraf)
# print(f'bilgileri girilen kisinin toplam masrafi {toplammasraf} olup '
#       f'gelirinin gidere orani {gelirgiderorani}dir')
# f = open('aylikmasraf', 'w')
# print(f'bilgileri girilen kisinin toplam masrafi {toplammasraf} olup '
#       f'gelirinin gidere orani {gelirgiderorani}dir', file=f)


# 6-
# Asagidaki ciktiyi 3 farkli yontem ile printleyin.
# Python’un kurucusu Guido Van Rossum, Hollanda’nin Amsterdam’daki
# "Universiteit Van Amsterdam" okulundan  1982’de mezun olmuşur'
# print("""
# Python’un kurucusu Guido Van Rossum, Hollanda’nin Amsterdam’daki
# "Universiteit Van Amsterdam" okulundan  1982’de mezun olmuşur'
# """)
# print('Python’un kurucusu Guido Van Rossum, Hollanda’nin Amsterdam’daki\n'
#       '"Universiteit Van Amsterdam" okulundan  1982’de mezun olmuşur\'')

# print("Python’un kurucusu Guido Van Rossum, Hollanda’nin Amsterdam’daki\n"
#       "\"Universiteit Van Amsterdam\" okulundan  1982’de mezun olmuşur\'")