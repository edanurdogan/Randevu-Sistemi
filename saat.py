class Saat:
    
    def __init__(self):
        self.saat=["(9:00)","(9:30)","(10:00)","(10:30)","(11:00)","(11:30)","(13:00)","(13:30)","(14:00)","(14:30)","(15:00)","(15:30)","(16:00)","(16:30)"]
        self.selection=None
        
    def select_saat(self):

        print("\nSaat Seçiminizi Yapınız:")
        
        for i,clock in enumerate(self.saat):
            print(f"{i+1}.{clock}")
        
        selection=int(input())
        self.selection=self.saat[selection - 1]