class Dosya():
    def __init__(self):
        with open('metin.txt', 'r', encoding='utf-8') as file:
            dosya_icerigi = file.read()
            kelimeler  = dosya_icerigi.split()
            self.sade_kelimeler = list()
            for i in kelimeler:
                k = ""
                for j in i:
                    if(j.isalpha()):
                        k += j
                self.sade_kelimeler.append(k)

    def tum_kelimeler(self):
        kelimeler_kumesi = set()
        for i in self.sade_kelimeler:
            kelimeler_kumesi.add(i)
        print('tum kelimeler')
        for i in kelimeler_kumesi:
            print(i)
            print("***************************************")

    def kelime_frekansi(self):
        kelime_sozluk = dict()
        for i in self.sade_kelimeler:
            if(i in kelime_sozluk):
                kelime_sozluk[i] += 1
            else:
                kelime_sozluk[i] = 1
        for kelime,sayi in kelime_sozluk.items():
            print(f'{kelime} kelimesi {sayi} defa geciyor')
            print("-"*(len(kelime) + len(' kelimesi ') + len(str(sayi)) + len(' defa geciyor')))


dosya = Dosya()

dosya.kelime_frekansi()

