import random
import time

# made by YAVUZ YARKIN OKULAR
class anahtar():
    def __init__(self, araba_durum="Durdur", araç_pil="100", pil="0", araç_yakıt="60", yakıt=""):
        self.araba_durum = araba_durum
        self.araç_pil = araç_pil
        self.pil = pil
        self.araç_yakıt = araç_yakıt
        self.yakıt = yakıt

    def arabaÇalıştır(self):
        if(self.araba_durum == "Çalıştır"):
            print("Arabanız  zaten Çalışıyor..")
        else:
            print("Arabanız Çalıştırılıyor..")
            self.araba_durum = "Çalıştır"

    def arabaDurdur(self):
        if(self.araba_durum == "Durdur"):
            print("Arabanız durduruluyor.")
        else:
            print("Arabanız Çalıştırılıyor..")
            self.araba_durum = "Çalıştır"

            

    def araçPil(self):
        pil = random.randint(0, len(self.araç_pil))
        self.pil = self.araç_pil(pil)
        print("Pil Durumunuz:")
        time.sleep(2)
        print(self.pil)

    def araçYakıt(self):
        yakıt = random.randint(0, len(self.araç_yakıt))
        self.yakıt = self.araç_yakıt(yakıt)
        print("Pil Durumunuz:")
        time.sleep(2)
        print(self.yakıt)

    def __str__(self):
        return "Pil durumu:{}\n Yakıt Durumu:{} ".format(self.pil, self.yakıt)


class anahtar2():
    def __init__(self, araçpark="Park Halinde", ayna_durum="Açık"):
        self.araçpark = araçpark
        self.ayna_durum = ayna_durum

    def araçParktanÇıkar(self):
        if (self.araçpark == "Park halinde"):
            print("Arabanız zaten park halinde")
        else:
            print("Aracınız park edili")
            self.araçpark = "Parktan Çıkar"

    def araçParkEt(self):
        if self.araçpark == "Parktan çıkartılmış":
            print("Arabanız zaten park halinde")
        else:
            print("Arabanız park ediliyor..")
            time.sleep(1)
            self.araçpark = "Park Halinde"

    def araçAynaAçık(self):
        if self.ayna_durum == "Açık":
            print("Aynalarınız zaten açık durumda")
        else:
            print("Aynanız kapatılıyor..")
            time.sleep(1)
            self.ayna_durum = "Kapat"

    def araçAynaKapalı(self):
        if self.ayna_durum == "Kapalı":
            print("Aynalarınız Kapatılıyor..")
            time.sleep(1)
        else:
            print("Aynalarınız Açılıyor..")
            time.sleep(1)
            self.ayna_durum = "Açık"


class iklimlendirme():
    def __init__(self, klima="Kapalı"):
        self.klima = klima

    def klimaKapalı(self):
        if self.klima == "Kapalı":
            print("Klimanız zaten kapalı")
        else:
            print("Klimanız açılıyor")
            time.sleep(1)
            self.klima = "Açık"

    def klimaAçık(self):
        if self.klima:
            print("Klimanız zaten açık ")
        else:
            print("Klimanız kapatılıyor..")
            time.sleep(1)
            self.klima = "Kapalı"


class araçBilgileri():
    def __init(self, araçKm="100000", kmBilgi="0"):
        self.araçKm = araçKm
        self.kmBilgi = kmBilgi

    def araçKiloMetre(self):
        kilomtere = random.randint(0, len(self.araçKm))
        self.kmBilgi = self.araçKm(kilomtere)
        print("Kilometre Değeriniz:{}".format(self.kmBilgi))


anahtar = anahtar()
anahtar2 = anahtar2()
iklimlendirme = iklimlendirme()
bilgi = araçBilgileri()
print("""*** Uzaktan Araç Kontrol Uygulaması***
1.Araba Çalıştır
2.Araba Durdur
3.Pil Durumu
4.Yakıt Durumu
5.Otomatik Park Et
6.Parktan Çıkar
7.Aynaları Aç
8.Aynaları kapat
9.Klima Aç
10.Klima Kapat
11.Kilometre bilgisi öğrenme

Menüden Çıkmak için 'q' a basınız.


""")

while True:
    işlem = input("Yapmak istediğiniz işlemi seçiniz:")

    if işlem == "1":
        anahtar.arabaÇalıştır()

    elif işlem == "2":
        anahtar.arabaDurdur()

    elif işlem == "3":
        anahtar.araçPil()
    elif işlem == "4":
        anahtar.araçYakıt()
    elif işlem == "5":
        anahtar2.araçParkEt()
    elif işlem == "6":
        anahtar2.araçParktanÇıkar()
    elif işlem == "7":
        anahtar2.araçAynaKapalı()
    elif işlem == "8":
        anahtar2.araçAynaAçık()
    elif işlem == "9":
        iklimlendirme.klimaKapalı()
    elif işlem == "10":
        iklimlendirme.klimaAçık()

    elif işlem == "11":
        bilgi.araçKiloMetre()

    else:
        print("Çıkış yapılıyor...")
        time.sleep(1)
    break
