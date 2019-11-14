# ODEV 1: ADAM ASMACA
#   -Onceden belirlenmis bir kelime degiskene atanacak ve kullanicidan bu kelimeyi harf tahminleriyle bilmesi istenecek.
#   -Kullanicinin 6 hamle sansi olacak ve her bir yanlis hamlesinde kalan hamle sayisini gosterin.
#   -Ayrica yine her bir yanlis hamle sonucunda adam asmaca oyunu oynarken cizdigimiz yanlis hamle sonucundaki cizimleri
#   sizde ekranda karakterleri kullanarak gosterin.
#   -Kullanici harf disinda bir karakter girdiginde gerekli uyariyi yapin ve bunu da yanlis hamle olarak saymayin.
#   Oyun devam etsin.
#   -Bir yanlis ve bir dogru hamle yapilmis ornek kod ciktisi:
#
#                            _______
#                           |       |
#                           |       O           5 HAKKINIZ KALDI!!!
#                           |
#                           |
#                          ---
#
#            - a -  -  -  - a -


word = "oguzhan"
turns = 6
guesses = ''
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=' ')
        else:
            print('-', end='')
            failed += 1
    if failed == 0:
        print("You won")
        break
    guess = input("guess a character:")
    if guess not in word:
        turns -=1
        print('wrong')
        print("You have", + turns, 'more guesses')
        if turns == 0:
            print("You Loose")








    # if char == kelime[i] and tahmin[i] == '-':
  #           tahmin.append(char)
  #       elif char != kelime[i] and tahmin[i] = '-':
  #           tahmin.append('-')
  #

# ODEV 2:SAYI TAHMIN OYUNU:
#   Kendiniz 4 basamakli, rakamlari birbirinden farkli ve icerisinde 0 rakaminin yer almadigi bir sayi belirleyin.
#   Kullanicidan bu sayiyi tahmin etmesini isteyin. Yapilan tahmin sonucu kullanicinin, tahminde bulundugu sayidaki
#   rakamlarin degeri ve yeri dogruysa +1, degeri dogru fakat yeri dogru degilse -1 ciktisi verecegiz.
#   Bu sekilde tahminde bulunmaya devam etmesi saglanacak ve sayiyi tam bir sekilde dogru bildiginde
#   gerekli bilgilendirme yapilip oyun bitirilecek.
#    Ornek: sayi = 1234   yapilan tahmin = 9831    ornek output = +1 -1#
#           (Burada "9" ve "8" rakamlari yanlis oldugu icin ciktiya bir etkisi yok. "3" rakaminin yeri dogru oldugu
#           icin +1, "1" rakami sayi icerisinde yer alan fakat yeri yanlis oldugu icin -1 ciktisi verecegiz.)#
#
#           yapilan tahmin = 2134#  ornek output = +2 -2#
#           ("2" ve "1" rakamlari sayi icerisinde yer aldigi fakat yerlerinin yanlis olmasi nedeniyle ikisi icin -1,
#           "3" ve "4" rakamlarinin yerleri de dogru oldugu icin +1 degerleri donecegiz.)#
#
#           yapilan tahmin = 9876   ornek output = +0 -0#
#           yapilan tahmin = 2146   ornek output = +0 -3
#
# sayi = 1234
# var = yok = 0
# while True:
#     tahmin = input('tahmininiz: ')
#     for i in str(sayi):
#         for j in tahmin:
#             if i == j and str(sayi).index(i) == tahmin.index(j):
#                 var += 1
#             elif i == j and str(sayi).index(i) != tahmin.index(j):
#                 yok += 1
#     print(f'output : +{var} -{yok}')
#     var = yok = 0
# #

#
# BONUS ODEV:
#
#   # İki liste tanımlayın.
#   # İlk liste 1'den 10'a kadar sayılardan oluşturun.
#   # İkinci listeyi sırasıyla a'dan başlayarak 10 harf ile oluşturun.
#   # İki liste için de döngü kurup, iki listenin elemanlarının bütün kombinasyonlarından oluşan
#   iki yeni liste oluşturun.
#
#   # 3'er elemanli versiyonunda cıktı olarak bu şekilde bir çıktı beklenmektedir:
#
#   # 1. [1a, 1b, 1c, 2a, 2b, 2c, 3a, 3b, 3c]
#   # 2. [a1, a2, a3, b1, b2, b3, c1, c2, c3]
# list1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# list2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# list3 = []
# list4 = []
#
# for i in list1, list2:
#     print(i)
# for i in list1:
#     print(i, end=' ')
# i = 0
# while i < len(list1):
#     for i in list1:
#         j = 0
#         for j in list2:
#             j += 1
#             print(list1[j])
#             print(list2[j])
#             list3.append(list1[j] + list2[j])
# print(list3)
