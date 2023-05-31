

class On_muayene:
    print("\n******* Lütfen Sorulara Cevap Verin *******\n")
    sikayetler = open("sikayetler.txt","r")
    sikayetler2 = open("sikayetler2.txt","w")
    sikayet = sikayetler.read()
    lines = sikayet.split("\n")
    for item in lines:
        giris = input(f"{item} (Evet/Hayır):").capitalize()
        while lines:
            if giris == "Evet" or giris == "Hayır":
                sikayetler2.write(f"{item} {giris} \n")
                break
            else:
                print("\nGeçersiz karakter girdiniz !! \n")
                giris = input(f"{item} (Evet/Hayır):").capitalize()
                sikayetler2.write(f"{item} {giris} \n")
                break
        
    sikayetler.close()
    sikayetler2.close()

    class Sikayet_Ozeti():
        
        s1 = open("sikayetler2.txt","r")
        s1 = s1.read()
        print("\n******* Şikayet Özeti *******\n")
        print(s1)
        
            
        class Onerilen_Branslar():
            with open("sikayetler2.txt","r") as file:
                line_count = 0
                lines = []
                for line in file:
                    line_count += 1
                    if "Evet" in line:
                        lines.append(line_count)
                print("***Önerilen Branşlar***\n")
                for line in lines:
                    if 2 in lines:
                        print("1.Kulak Burun Boğaz")
                        break
                    elif 1 in lines or 3 in lines and 4 in lines or 5 in lines or 6 in lines:
                        print("1.Beyin ve Sinir Cerrahisi")
                        print("2.Fizyoterapi")
                        print("3.Nöroloji")
                        break
                    elif 7 in lines or 8 in lines and 9 in lines or 11 in lines:
                        print("1.Dahiliye")
                        break
                    elif 4 in lines and 10 in lines :
                        print("1.Kardiyoloji")
                        print("2.Kalp Ve Damar Cerrahisi") 
                        print("3.Göğüs Hastalıkları")
                        break
                    elif 12 in lines and 1 in lines:
                        print("Göz Hastalıkları")
                        break                    
                    elif 13 in lines:
                        print("1.Ağız, Diş ve Çene Cerrahisi")
                        break
                if len(lines) == 0: 
                    print("*Herhangi Bir Branş Önerilemedi*")
                        
            class Randevu_Olustur:
                def __init__(self,randevu_olustur):
                    """ Randevu_Olustur class constructor

                        Args:
                        randevu_olustur (str): Randevu Oluşturma
                        
                    """
                    self._randevu_olustur = randevu_olustur
                
                @property
                def randevu_olustur(self):
                    return self._randevu_olustur
                
                @randevu_olustur.setter
                def get_randevu_olustur(self):
                    return self._randevu_olustur

                randevu = input("\nRANDEVU ALMAK İSTİYOR MUSUNUZ ? (EVET/HAYIR):")
                randevu = randevu.swapcase()

                def run_main():
                    exec(open("main.py").read())
                import subprocess
                if "EVET" == randevu:
                    print("\n*********RANDEVU SİSTTEMİNE YÖNLENDİRİLİYORSUNUZ*********\n")
                    subprocess.call(["python", "main.py"])

                elif "HAYIR" == randevu:
                    print("\n*********Ön Muayne Bitti*********")

                else:
                    print("\nGeçersiz Karakter Girdiniz !!\n\n")