# TO DO LIST
# -Yapilacaklar listesi ve yapilanlar listesi seklinde iki bos liste olusturun. Kullanicinin yapabilecegi islemler:
#     *Yapilacaklar listesine gorev ekleme
#         ->append metodu kullanilsin
#     *Yapilacaklar listesinden gorev silme
#         -> del metodu kullanilsin
#     *Yapilacaklar listesindeki gorevi yapilanlar listesine atama
# #         -> pop metodu kullanilsin
#     *Yapilanlar listesini goruntuleme
#     *kullanıcı yapılacaklar listesinin içini boşaltma
#         -> clear metodu kullanılsın
# -Dongu her basa dondugunde yapilacaklar listesi goruntulensin
# -Her iki liste goruntulenirken liste elemanlari numaralandirilarak verilsin
#     ORN:
#         Yapilacaklar Listesi:
#             1- Python odevini yap.
#             2- Alis-veris yapmaya git.
#             3- Ahmet'i ara.
# - Eger yapilacaklar listesi bos ise "Su an yapilacaklar listeniz bos" seklinde bir cikti versin


# for i,j in enumerate(yapilacak):
# print(i+1,'-',j)

yapilacak = []; yapilan = []
print(len(yapilacak))
while True:
    print('gorev ekleme: 1',
          'gorev silme: 2',
          'gorevi yapilanlar listesine atama: 3',
          'Yapilanlar listesini goruntuleme: 4',
          'yapılacaklar listesinin içini boşaltma: 5',
          'programdan cikmak istiyorum: q', sep='\n')
    islem = input('ne yapmak istiyorsunuz')
    if islem == 'q':
        print('programdan cikiliyor')
        break
    elif islem == '1':
        todo = input('eklemek istediginiz gorev nedir :')
        yapilacak.append(todo)
        print('Yapilacaklar Listesi:')
        for i,j in enumerate(yapilacak):
            print(i+1,'-',j)

    elif islem == '2':
        sil = input('silinecek islem nedir')
        yapilacak.remove(sil)
        yapilan.append(sil)
        print('Yapilacaklar Listesi:')
        for i, j in enumerate(yapilacak):
            print(i + 1, '-', j)
        print('Yapilanlar Listesi:')
        for i, j in enumerate(yapilan):
            print(i + 1, '-', j)
    elif islem == '4':
        if len(yapilacak) == 0:
            print('listeniz bos')
        else:
            for i, j in enumerate(yapilacak):
                print(i + 1, '-', j)
    elif islem == '5':
        yapilacak.clear()
    else:
        print('lutfen gecerli bir islem giriniz')
