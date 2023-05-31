class Gun:
    
    def __init__(self):
        self.gun=["Pazartesi","Salı","Çarşamba","Perşembe","Cuma"]
        self.selection=None
        
    def select_gun(self):
        
        print("\nGün Seçiminizi Yapınız:")
        
        for i,clock in enumerate(self.gun):
            print(f"{i+1}.{clock}")
            
        selection=int(input())
        self.selection=self.gun[selection - 1]