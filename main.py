from hasta import Hasta
from doktor import Doktor
from hastane import Hastane
from klinik import Klinik
from gun import Gun
from saat import Saat


h1 = Hasta()


print("\n-----------Hoşgeldiniz-----------\n")
h1.set_isim(input("Lütfen isminizi girin: "))
h1.set_soyisim(input("Lütfen Soyisminizi Giriniz: "))
h1.set_tc(int(input("Lütfen Tc Numaranızı Giriniz: ")))
h1.set_mail(input("Lütfen Mail Adresinizi Giriniz: "))
h1.set_tel(int(input("Lütfen Telefon Numaranızı Giriniz: ")))


city = [
    {'name': 'Adana', 'hastaneler': ['Adana Şehir Hastanesi', 'Adana Yüreğir Devlet Hastanesi', 'Adana Çukurova Devlet Hastanesi']},
    {'name': 'Antalya', 'hastaneler': ['Antalya Eğitim Ve Araştırma Hastanesi', 'Antalya Gazipaşa Devlet Hastanesi', 'Antalya Kaş Devlet Hastanesi']},
    {'name': 'Ankara', 'hastaneler': ['Ankara Eğitim Ve Araştırma Hastanesi', 'Ankara Mamak Devlet Hastanesi', 'Ankara Polatlı Duatepe Devlet Hastanesi']},
    {'name': 'Bursa', 'hastaneler': ['Bursa Şehir Hastanesi', 'Bursa İnegöl Devlet Hastanesi', 'Bursa Yüksek İhtisas Eğitim Ve Araştırma Hastanesi']},
    {'name': 'Eskişehir', 'hastaneler': ['Eskişehir Şehir Hastanesi', 'Eskişehir Çifteler Devlet Hastanesi', 'Eskişehir Sivrihisar Devlet Hastanesi']},
    {'name': 'Hatay', 'hastaneler': ['Hatay Dörtyol Devlet Hastanesi', 'Hatay İskenderun Devlet Hastanesi']},
    {'name': 'İstanbul', 'hastaneler': ['Başakşehir Çam Ve Sakura Şehir Hastanesi', 'İstanbul Eğitim Ve Araştırma Hastanesi', 'Taksim Eğitim Ve Araşırma Hastanesi']},
    {'name': 'İzmir', 'hastaneler': ['İzmir Atatürk Eğitim Ve Araştırma Hastanesi', 'İzmir Foça Devlet Hastanesi', 'İzmir Menemen Devlet Hastanesi']},
    {'name': 'Kayseri', 'hastaneler': ['Kayseri Devlet Hastanesi', 'Kayseri Şehir Hastanesi', 'Kayseri Pınarbaşı İlçe Hastanesi']},
    {'name': 'Osmaniye', 'hastaneler': ['Osmaniye Devlet Hastanesi', 'Osmaniye Düziçi Devlet Hastanesi', 'Osmaniye Kadirli Devlet Hastanesi']},
    
]
        

selection1 = Hastane(city)
selection1.run()

klnk1 = Klinik()
klnk1.select_clinic()

dktr1 = Doktor()
dktr1.select_doctor()

gun1=Gun()
gun1.select_gun()

saat1=Saat()
saat1.select_saat()


print(f"\n-------------HASTANE RANDEVU SİSTEMİNE HOŞGELDİNİZ----------\n")
print(f"Hastanın İsmi:{h1.get_isim()}")
print(f"Hastanın Soyismi:{h1.get_soyisim()}")
print(f"Hastanın TC Numarası:{h1.get_tc()}")
print(f"Hastanın Mail Adresi:{h1.get_mail()}")
print(f"Hastanın Telefon Numarası:{h1.get_tel()}")
print(f"Klinik: {klnk1.selection}")
print(f"Doktorunuz: {dktr1.selection}")
print(f"Gün: {gun1.selection}")
print(f"Saat:{saat1.selection}")
print("\n--------------RANDEVUNUZ BAŞARIYLA OLUŞTURULDU---------------\n\n")