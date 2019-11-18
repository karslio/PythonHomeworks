# print('Python programlama dilinin adı "piton" yılanından gelmez')
# print("İstanbul'un 5 günlük hava durumu tahmini")
# print("""Python programlama dilinin adı "piton" yılanından gelmez""")
# print("""İstanbul'un 5 günlük hava durumu tahmini""")
# print("""
# [H]=========HARMAN========[-][o][x]
# |                                 |
# | Programa Hoşgeldiniz!           |
# | Sürüm 0.8                       |
# | Devam etmek için herhangi       |
# | bir düğmeye basın.              |
# |                                 |
# |=================================|
# """)
# print("""Python programlama dili Guido Van Rossum
# adlı Hollandalı bir programcı tarafından 90'lı
# yılların başında geliştirilmeye başlanmıştır. Çoğu
# insan, isminin "Python" olmasına bakarak, bu programlama
# dilinin, adını piton yılanından aldığını düşünür.
# Ancak zannedildiğinin aksine bu programlama dilinin
# dı piton yılanından gelmez.""")
#
# print('Python', 'Programlama', 'Dili')
#
# print("Python", "PHP", "C++", "C", "Erlang")
#
# print("http://", "www.", "google.", "com", sep=" ")
#
# print("http://", "www.", "google.", "com", sep="")
#
# print("http://www", "google", "com", sep=".")
#
# print("bir", "iki", "üç", "dört", "on dört", sep="mumdur")
#
# print("bir", "iki", "üç", "dört", "on dört", sep=" mumdur ")
#
# print("bir", "iki", "üç", "dört", "on dört", sep=" " + "mumdur" + " ")
#
# print("bir", "iki", "üç", "dört", "on dört", sep=" " "mumdur" " ")
#
# print("birinci satır\nikinci satır\nüçüncü satır")
#
# print("birinci satır", "ikinci satır", "üçüncü satır", sep="\n")
#
# print("Bugün günlerden Salı", end=5 * "\n")
# # end  "\n" olarak calisir
#
# print("bir", "iki", "üç", "dört", "on dört", sep=" mumdur ", end=" mumdur\n")

# f = open('1-print.txt', 'w')
# print("Tahir olmak da ayıp değil", "Zühre olmak da")
# print("Tahir olmak da ayıp değil", "Zühre olmak da", sep=" ", end="\n", file=f)
# f.close()

#
# f = open('1-print.txt', 'w')
# print("Tahir olmak da ayıp değil", "Zühre olmak da", file=f)
# print("Adana", file=f)
# print("Ubuntu", file=f)
# f.close()
#
# print('L', 'i', 'n', 'u', 'x', sep='.')
# print(*"Linux", sep=".")
# print(*"Galatasaray")  # G a l a t a s a r a y
# print(*"TBMM", sep=".")
# # print(*2345 yildizli parametre sayilarla kullanilmaz
#
# # ters taksim
# print('Yarın Adana\'ya gidiyorum.')
# print("\"book\" kelimesi Türkçede \"kitap\" anlamına gelir.")
#
# baslik = "Türkiye'de Özgür Yazılımın Geçmişi"
# print(baslik, '\n', '-' * len(baslik), sep='')
# baslik = "Python Programlama Dili"
# print(baslik, '\n', '-' * len(baslik), sep='')
# baslik = "Alisveris Listesi"
# print(baslik, '\n', '-' * len(baslik), sep='')
#
# print("bir", "iki", "üç", sep="\t")
#
#
# pi = 3.14
# r = 5
# alan = pi * r * r
# print(alan)


# print("Python Programlama Dili")
# print("hardenber'de yasiyorum")
# print('ali', 'veli', sep='-')
# print('bir', 'iki', 'uc', 'dort', 'on dort', sep=' mumdur ', end=' mumdur\n')
#
# print('birincisatir\nikincisatir\nucuncusatir')
# print('birincisatir', 'ikincisatir', 'ucuncusatir', sep='\n')

f = open('yazdir.txt', "w")
print('merhaba hardenberg', file=f,flush=True)
print('merhaba hardenberg', file=f,flush=True)
# f.close()
