class Klinik:
    def __init__(self):
        self.klnk = ["Genel Cerrahi","Beyin Ve Sinir Cerrahi","Fizyoterapi","Çocuk Cerrahi","Göğüs Hastalıkları","Göz Hastalıkları","Dahiliye","Kalp Ve Damar Cerrahisi","Ağız, Diş ve Çene Cerrahasi", "Kulak Burun Boğaz", "Nöroloji", "Kadın Doğum"]
        self.selection = None

    def select_clinic(self):
        
        print("\nHangi Kliniği İstiyorsanız İlgili Numaraya Basınız: ")

        for i, clinic in enumerate(self.klnk):
            print(f"{i+1}. {clinic}")

        selection = int(input())
        self.selection = self.klnk[selection - 1]