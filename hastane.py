class Hastane():
    def __init__(self, city):
   
        self.city = city
        

    def run(self):
    
        print("\nİstediğiniz Şehire Ait Numaraya Basınız:")
        for i, hospital in enumerate(self.city):
            print(f"{i+1}. {hospital['name']}")

        hospital_index = int(input()) - 1
        selected_city = self.city[hospital_index]

    
        print(f"\n{selected_city['name']} Şehrindeki Hastaneler:")
        for i, hastane in enumerate(selected_city['hastaneler']):
            print(f"{i+1}. {hastane}")

   
        hastane_index = int(input()) - 1
        selected_hastane = selected_city['hastaneler'][hastane_index]
        
        print(f"\nHastane:{selected_hastane}\n ")
        
        
city = [
    {'name': 'Adana', 'hastaneler': ['Adana Şehir Hastanesi', 'Adana Yüreğir Devlet Hastanesi', 'Adana Çukurova Devlet Hastanesi']},
    {'name': 'Antalya', 'hastaneler': ['Antalya Eğitim Ve Araştırma Hastanesi', 'Antalya Gazipaşa Devlet Hastanesi', 'Antalya Kaş Devlet Hastanesi']},
    {'name': 'Ankara', 'hastaneler': ['Ankara Eğitim Ve Araştırma Hastanesi', 'Ankara Mamak Devlet Hastanesi', 'Ankara Polatlı Duatepe Devlet Hastanesi']},
    {'name': 'Bursa', 'hastaneler': ['Bursa Şehir Hastanesi', 'Bursa İnegöl Devlet Hastanesi', 'Bursa Yüksek İhtisas Eğitim Ve Araştırma Hastanesi']},
    {'name': 'Eskişehir', 'hastaneler': ['Eskişehir Şehir Hastanesi', 'Eskişehir Çifteler Devlet Hastanesi', 'Eskişehir Sivrihisar Devlet Hastanesi']},
    {'name': 'Hatay', 'hastaneler': ['Hatay Dörtyol Devlet Hastanesi', 'Hatay Dörtyol Devlet Hastanesi', 'Hatay İskenderun Devlet Hastanesi']},
    {'name': 'İstanbul', 'hastaneler': ['Başakşehir Çam Ve Sakura Şehir Hastanesi', 'İstanbul Eğitim Ve Araştırma Hastanesi', 'Taksim Eğitim Ve Araşırma Hastanesi']},
    {'name': 'İzmir', 'hastaneler': ['İzmir Atatürk Eğitim Ve Araştırma Hastanesi', 'İzmir Foça Devlet Hastanesi', 'İzmir Menemen Devlet Hastanesi']},
    {'name': 'Kayseri', 'hastaneler': ['Kayseri Devlet Hastanesi', 'Kayseri Şehir Hastanesi', 'Kayseri Pınarbaşı İlçe Hastanesi']},
    {'name': 'Osmaniye', 'hastaneler': ['Osmaniye Devlet Hastanesi', 'Osmaniye Düziçi Devlet Hastanesi', 'Osmaniye Kadirli Devlet Hastanesi']},
    
]