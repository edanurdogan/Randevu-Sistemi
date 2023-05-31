class Doktor:
    def __init__(self):
        self.dct = ["Emin Doğan","Nuri Hacıçavuşoğlu","Alaeddin Uçan","Mehmet Yılmaz", "Ahmet Uzun", "Ayşe Kaplan", "Edanur Doğan", "Ela Hümeyra Hacıçavuşoğlu", "Sedanur Doğan", "Ömer Faruk Doğan", "Mehmet Doğan", "Zeynep Ay"]
        self.selection = None

    def select_doctor(self):

        print("\nHangi Doktoru İstiyorsanız İlgili Numaraya Basınız: ")
        
        for i, city in enumerate(self.dct):
            print(f"{i+1}. {city}")

        selection = int(input())
        self.selection = self.dct[selection - 1]