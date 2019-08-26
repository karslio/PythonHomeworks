# 1.ODEV: BURCUN NE?
# 	Kullanicidan dogum gununu ve ayini isteyin, program hangi burc oldugunu soylesin.

# Koç Burcu : 21 Mart - 20 Nisan
# Boğa Burcu : 21 Nisan - 21 Mayıs
# İkizler Burcu : 22 Mayıs - 22 Haziran
# Yengeç Burcu : 23 Haziran - 22 Temmuz
# Aslan Burcu : 23 Temmuz - 22 Ağustos
# Başak Burcu : 23 Ağustos - 22 Eylül
# Terazi Burcu : 23 Eylül - 22 Ekim
# Akrep Burcu : 23 Ekim - 21 Kasım
# Yay Burcu : 22 Kasım - 21 Aralık
# Oğlak Burcu : 22 Aralık - 21 Ocak
# Kova Burcu : 22 Ocak - 19 Şubat
# Balık Burcu : 20 Şubat - 20 Mart

gun = int(input('dogdugunuz gunu girebilir misiniz:'))
ay = (input('dogdugunuz ayi girebilir misiniz:'))

if ay == 'mart' and gun >= 21 or ay == 'nisan' and gun <= 20:
    print('Koc Burcu')
elif ay == 'nisan' and gun >= 21 or ay == 'mayis' and gun <= 21:
    print('Boğa Burcu')
elif ay == 'mayis' and gun >= 22 or ay == 'haziran' and gun <= 22:
    print('İkizler Burcu')
elif ay == 'haziran' and gun >= 23 or ay == 'temmuz' and gun <= 22:
    print('Yengeç Burcu')
elif ay == 'temmuz' and gun >= 23 or ay == 'agustos' and gun <= 22:
    print('Aslan Burcu')
elif ay == 'agustos' and gun >= 23 or ay == 'eylul' and gun <= 22:
    print('Başak Burcu')
elif ay == 'eylul' and gun >= 23 or ay == 'ekim' and gun <= 22:
    print('Terazi Burcu')
elif ay == 'ekim' and gun >= 23 or ay == 'kasim' and gun <= 21:
    print('Akrep Burcu')
elif ay == 'kasim' and gun >= 22 or ay == 'aralik' and gun <= 21:
    print('Yay Burcu')
elif ay == 'aralik' and gun >= 22 or ay == 'ocak' and gun <= 21:
    print('Oğlak Burcu')
elif ay == 'ocak' and gun >= 22 or ay == 'subat' and gun <= 19:
    print('Kova Burcu')
elif ay == 'subat' and gun >= 20 or ay == 'mart' and gun <= 21:
    print('Balık Burcu')
else:
    print('girdiginiz degerleri kontrol ediniz')


# 2.ODEV: UZAKLIK BIRIMI DONUSUMU
# Kullanicadan 2 input alinacak:
# 1-km-mil donusumu mu yapmak istiyor, mil-km donusumu mu yapmak istiyor.
# 2-donusturmek istedigi birimin uzunlugu kactir?
# Donusum yapilacak birimler mil ve kilometre olacak.

deger = float(input('bir deger giriniz:'))
print("""
*************************
islemi seciniz
kmTomil = 1
milTokm = 2
*************************
""")
kmTomil = '{:04.2f}'.format(deger*0.621371192)
milTokm = '{:04.2f}'.format(deger*1.609)
islem = int(input('yapmak istediginiz islem ?'))
if islem == 1:
    print(f'{deger} km {kmTomil} mildir')
elif islem == 2:
    print(f'{deger} mil {milTokm} kmdir')
else:
    print('girdiginiz degeri kontrol ediniz')

# 3.ODEV: PAROLA KARAKTER KONTROLU
# Kullanicidan 3-18 karakter arasinda bir username olusturmasini isteyin. Eger usernamede rakam varsa,
# rakam kullanamayacagina dair gerekli uyariyi yapin. Sonrasinda kullanicidan 6 ile 12 karakter araliginda
# bir parola olusturmasini isteyin. Olusturulan parolanin 6dan kisa ya da uzun olmasi
# durumlarinda gerekli uyarilari yapin.
# Iki durumun sartlari da saglaniyorsa username ve parolayi hem ekrana printleyin hem de bir dosyaya kaydedin.


while True:
    s = input("username olarak 3-18 karakter arasinda bir deger giriniz: ")
    if any(i.isdigit() for i in s):
        print("username de sayi kullanamazsin")
    elif len(s) <= 3 or len(s) >= 18:
        print('username  3 ile 18 karekter olabilir')
    else:
        print('username basili bir sekilde olusturuldu')
        while True:
            p = input('parola olarak  6 ile 12 araliginda karekter giriniz')
            if len(p) < 6 or len(p) > 18:
                print('lutfen paraloyi istenen sartlarda olusturun')
            else:
                print(f'username\t:{s}\nparola\t\t:{p}')
                break
    break


# 4.ODEV: SAYI TAHMIN OYUNU
# Bir degiskene 1-10 arasinda bir sayi atayin.Kullanicidan bu sayiyi tahmin etmesini isteyin.
# Kullanici 5 denemede bilirse 1 yildiz kazansin, 3 denemede bilirse 2 yildiz kazansin, 1 denemede bilirse
# 3 yildiz kazansin.

sayi = 7
count = 0
while count < 6:
    tahmin = int(input('1 ile 10 arasiindaki sayiyi tahmin ediniz'))
    if tahmin == sayi and count <= 1:
        print('sayiyi bildiniz ***')
        break
    elif tahmin == sayi and count <= 3:
        print('sayiyi bildiniz **')
        break
    elif tahmin == sayi and count <= 5:
        print('sayiyi bildiniz *')
        break
    else:
        if tahmin < sayi:
            print('daha buyuk bir sayi dene')
            count += 1
        else:
            print('daha kucuk bir sayi dene')
            count += 1
        if count >= 5:
            print('hakkiniz bitmistir')
            break


# 5.ODEV: ATM
# Kullanicinin hesabinda 1000 € olsun. Kullaniciya hangi islemi yapmak istedigini sorun.
# Kullanicinin yapabilecegi islemler:
# 1-bakiye kontrolu
# 2-para yatirma
# 3-para cekme
# Kulkanicinin secimine gore gerekli islemleri /sorulari devam ettirin ve hesabi guncelleyin
# Kullanici hesabinda olan paradan fazla para cekmek isterse uyarin ve islemi yapamayacagini soyleyin.

bakiye = 1000

print("""
# 1-bakiye kontrolu
# 2-para yatirma
# 3-para cekme
# cikmak icin q ya basiniz
""")
while True:
    islem = input('islemi seciniz')
    if islem == 'q':
        print('yine bekleriz')
        break
    elif islem == '1':
        print(f'Bakiyeniz {bakiye} Euro dur')
    elif islem == '2':
        yatanMiktar = int(input('yatirilacak miktari girin:'))
        print(f'Bakiyeniz {bakiye + yatanMiktar} Euro olmustur')
    elif islem == '3':
        cekilenMiktar = int(input('Cekilecek miktari giriniz'))
        if cekilenMiktar > bakiye:
            print('bakiye yetersiz')
        else:
            bakiye = bakiye - cekilenMiktar
            print(f'Bakiyeniz {bakiye} Euro kalmistir')
    else:
        print('gecersiz islem')
