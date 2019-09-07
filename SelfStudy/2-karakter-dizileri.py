# nesne = "123456789"
# for n in nesne:
#     print(int(n) * 2, end=' ')
####################################################################
# nesne = "123456789"
# for n in nesne:
#     print(n * 2, end=' ')
####################################################################
#
# kardiz = "istihza"
# print(len(kardiz))
# print((kardiz[-1]))
# for i in range(7):
#     print(kardiz[i])
# for karakter in range(len(kardiz)):
#     print(kardiz[karakter])
####################################################################
# isim = input("isminiz: ")
# for i in range(len(isim)):
#     print("isminizin {}. harfi: {}".format(i+1, isim[i]))
###################################################################
##Karakter Dizilerini Dilimlemek
# site = "www.istihza.com"
# print(site[4:11])
# print(site[12:16])
#
# site1 = "www.google.com"
# site2 = "www.istihza.com"
# site3 = "www.yahoo.com"
# site4 = "www.gnu.org"
# for isim in site1, site2, site3, site4:
#     print("site: ", isim[4:-4])
###################################################################
# ata1 = "Akıllı bizi arayıp sormaz deli bacadan akar!"
# ata2 = "Ağa güçlü olunca kul suçlu olur!"
# ata3 = "Avcı ne kadar hile bilirse ayı da o kadar yol bilir!"
# ata4 = "Lafla pilav pişse deniz kadar yağ benden!"
# ata5 = "Zenginin gönlü oluncaya kadar fukaranın canı çıkar!"
#
# for ata in ata1, ata2, ata3, ata4, ata5:
#     print(ata[0:-1] + ".")
#     print(ata[::-1])
###################################################################
# print(*sorted("kitap"),sep='')
# for i in sorted("kitap"):
#     print(i, end="")
# site1 = "www.google.com"
# site2 = "www.istihza.com"
# site3 = "www.yahoo.com"
# site4 = "www.gnu.org"
# for i in site1, site2, site3, site4:
#     print("http://", i, sep="")
###################################################################
# sesli_harfler = "aeıioöuü"
# # sessiz_harfler = "bcçdfgğhjklmnprsştvyz"
# # sesliler = ""
# # sessizler = ""
# # kelime = "istanbul"
# # for i in kelime:
# #     if i in sesli_harfler:
# #         sesliler += i
# #     else:
# #         sessizler += i
# # print("sesli harfler: ", sesliler)
# # print("sessiz harfler: ", sessizler)

###################################################################
# print(dir(str))
# adet = 0
# for i in dir(""):
#     if "_" not in i[0]:
#         adet += 1
#         print(adet, i)
# print(f'toplam {adet} adet metot ile ilgileniyoruz')
###################################################################
# enumerate()
print(*reversed("istihza"), sep='')
print(*enumerate("istihza"))
for i in enumerate('istihza'):
    print(i)
for sıra, metot in enumerate(dir("")):
    print(sıra+1, metot)
###################################################################
###################################################################
###################################################################
