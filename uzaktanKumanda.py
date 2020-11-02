import random
import random

class anahtar():
        def __init__(self,araba_durum="Durdur",far_durum="Kapalı",araç_pil="0",pil="0",araç_yakıt="0",yakıt="0"):
            self.araba_durum=araba_durum
            self.far_durum=far_durum
            self.araç_pil=araç_pil
            self.pil=pil
            self.araç_yakıt=araç_yakıt
            self.yakıt=yakıt
        def arabaÇalıştır(self):
            if(self.araba_durum=="Çalıştır"):
                print("Arabanız  zaten Çalışıyor..")
            else:
                print("Arabanız Çalıştırılıyor..")
                self.araba_durum="Çalıştır"

        def arabaDurdur(self):
            if(self.araba_durum=="Durdur"):
                print("Arabanız zaten stop edilmiş durumda..")
            else:
                print("Arabanız çalıştırılıyor..")
                self.tv_durum="Çalıştır"
        
        def araç_pil(self):
            pil=random.randint(0,len(self.araç_pil)-1)
            self.pil=self.araç_pil(pil)
            print("Pil Durumunuz:",self.pil)
        def __str__(self):
            return "Arabanın Durumu: {}\n "
        
        def araç_yakıt(self):
            yakıt=random.randint(0,len(self.araç_yakıt)-1)
            self.yakıt=self.araç_yakıt(yakıt)
            print("Pil Durumunuz:",self.yakıt)


anahtar=anahtar()
print("""*** Araç Kontrol Uygulaması***
1.Araba Çalıştır.
2.Araba Durdur.
3.
4.Pil Durumu
5.Yakıt Durumu


""")

while True:
    işlem=input("Yapmak istediğiniz işlemi seçiniz:")

    if işlem=="1":
        anahtar.arabaÇalıştır()
    
    elif işlem=="2":
        anahtar.arabaDurdur()
        