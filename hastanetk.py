import tkinter as tk
from tkinter.ttk import Combobox

form =tk.Tk()
form.geometry("700x700+500+100")
form.title("Hastane Randevu Sistemi")
form.config(bg="light grey")
x=tk.StringVar()
x1=tk.StringVar()
x2=tk.StringVar()
x3=tk.StringVar()
x4=tk.StringVar()
x5=tk.StringVar()
entr1=tk.StringVar()
entr2=tk.StringVar()
entr3=tk.StringVar()
entr4=tk.StringVar()
entr5=tk.StringVar()
baslik=tk.Label(text="Hastane Randevu Sistemine Hoşgeldiniz",fg="black",bg="dark grey",font="Times 17 italic").pack()

llb_ad=tk.Label(form,text="Adınız:",bg="grey",font="Times 12 italic").place(x=10,y=40)
llb_soyad=tk.Label(form,text="Soyadınız:",bg="grey",font="Times 12 italic").place(x=10,y=60)
llb_mail=tk.Label(form,text="Mail Adresiniz:",bg="grey",font="Times 12 italic").place(x=10,y=80)
llb_tc=tk.Label(form,text="TC Numaranızı Giriniz:",bg="grey",font="Times 12 italic").place(x=10,y=100)
llb_tel=tk.Label(form,text="Telefon Numaranızı Giriniz:",bg="grey",font="Times 12 italic").place(x=10,y=120)
llb_sehir=tk.Label(form,text="Şehir Seçiminizi Yapınız:",bg="grey",font="Times 12 italic").place(x=10,y=140)
llb_hastane=tk.Label(form,text="Hastane Seçiminizi Yapınız:",bg="grey",font="Times 12 italic").place(x=10,y=160)
llb_klinik=tk.Label(form,text="Klinik Seçiminizi Yapınız:",bg="grey",font="Times 12 italic").place(x=10,y=180)
llb_gun=tk.Label(form,text="Gün Seçiminizi Yapınız:",bg="grey",font="Times 12 italic").place(x=10,y=200)
llb_doktor=tk.Label(form,text="Doktor Seçimizi Yapınız:",bg="grey",font="Times 12 italic").place(x=10,y=220)
llb_saat=tk.Label(form,text="Saat Seçiminizi Yapınız:",bg="grey",font="Times 12 italic").place(x=10,y=240)
entry_ad=tk.Entry(textvariable=entr1).place(x=200,y=40)
entry_soyad=tk.Entry(textvariable=entr2).place(x=200,y=60)
entry_mail=tk.Entry(textvariable=entr3).place(x=200,y=80)
entry_tc=tk.Entry(textvariable=entr4).place(x=200,y=100)
entry_tel=tk.Entry(textvariable=entr5).place(x=200,y=120)
sehir=["Adana","Antalya","Ankara","Bursa","Eskişehir","Hatay","İstanbul","İzmir","Kayseri","Osmaniye"]
kutu=Combobox(form,values=sehir,height=5,textvariable=x).place(x=200,y=140)

hastane=['Adana Şehir Hastanesi', 'Adana Yüreğir Devlet Hastanesi', 'Adana Çukurova Devlet Hastanesi','Antalya Eğitim Ve Araştırma Hastanesi', 'Antalya Gazipaşa Devlet Hastanesi', 'Antalya Kaş Devlet Hastanesi','Ankara Eğitim Ve Araştırma Hastanesi', 'Ankara Mamak Devlet Hastanesi', 'Ankara Polatlı Duatepe Devlet Hastanesi','Bursa Şehir Hastanesi', 'Bursa İnegöl Devlet Hastanesi', 'Bursa Yüksek İhtisas Eğitim Ve Araştırma Hastanesi','Eskişehir Şehir Hastanesi', 'Eskişehir Çifteler Devlet Hastanesi', 'Eskişehir Sivrihisar Devlet Hastanesi','Hatay Dörtyol Devlet Hastanesi', 'Hatay Dörtyol Devlet Hastanesi', 'Hatay İskenderun Devlet Hastanesi','Başakşehir Çam Ve Sakura Şehir Hastanesi', 'İstanbul Eğitim Ve Araştırma Hastanesi', 'Taksim Eğitim Ve Araşırma Hastanesi','İzmir Atatürk Eğitim Ve Araştırma Hastanesi', 'İzmir Foça Devlet Hastanesi', 'İzmir Menemen Devlet Hastanesi','Kayseri Devlet Hastanesi', 'Kayseri Şehir Hastanesi', 'Kayseri Pınarbaşı İlçe Hastanesi','Osmaniye Devlet Hastanesi', 'Osmaniye Düziçi Devlet Hastanesi', 'Osmaniye Kadirli Devlet Hastanesi']
kutu1=Combobox(form,values=hastane,height=5,textvariable=x1).place(x=200,y=160)
klinik=["Genel Cerrahi","Beyin Ve Sinir Cerrahi","Fizyoterapi","Çocuk Cerrahi","Göğüs Hastalıkları","Göz Hastalıkları","Dahiliye","Kalp Ve Damar Cerrahisi","Diş", "Kulak Burun Boğaz", "Nöroloji", "Kadın Doğum"]
kutu2=Combobox(form,values=klinik,height=5,textvariable=x2).place(x=200,y=180)
gun=["Pazartesi","Salı","Çarşamba","Perşembe","Cuma"]
kutu5=Combobox(form,values=gun,height=5,textvariable=x5).place(x=200,y=200)
doktor=["Emin Doğan","Nuri Hacıçavuşoğlu","Alaeddin Uçan","Mehmet Yılmaz", "Ahmet Uzun", "Ayşe Kaplan", "Edanur Doğan", "Ela Humeyra Hacıçavuşoğlu", "Sedanur Doğan", "Ömer Faruk Doğan", "Mehmet Doğan", "Zeynep Ay"]
kutu3=Combobox(form,values=doktor,height=5,textvariable=x3).place(x=200,y=220)
saat=["(9:00)","(9:30)","(10:00)","(10:30)","(11:00)","(11:30)","(13:00)","(13:30)","(14:00)","(14:30)","(15:00)","(15:30)","(16:00)","(16:30)"]
kutu4=Combobox(form,values=saat,height=5,textvariable=x4).place(x=200,y=240)

def randevu():
    
    label_bilgi=tk.Label(form,text="Randevu Bilgileri",bg="grey",font="Times 16 italic").place(x=10,y=320)
    llb_ad=tk.Label(form,text="Hastanın Adı:",bg="grey",font="Times 12 italic").place(x=10,y=340)
    llb_soyad=tk.Label(form,text="Hastanın Soyadı:",bg="grey",font="Times 12 italic").place(x=10,y=360)
    llb_mail=tk.Label(form,text="Hastanın Mail Adresi:",bg="grey",font="Times 12 italic").place(x=10,y=380)
    llb_tc=tk.Label(form,text="Hastanın TC Numarası:",bg="grey",font="Times 12 italic").place(x=10,y=400)
    llb_tel=tk.Label(form,text="Hastanın Telefon Numarası:",bg="grey",font="Times 12 italic").place(x=10,y=420)
    llb_sehir=tk.Label(form,text="Seçtiğiniz Şehir:",bg="grey",font="Times 12 italic").place(x=10,y=440)
    llb_hastane=tk.Label(form,text="Seçtğiniz Hastane:",bg="grey",font="Times 12 italic").place(x=10,y=460)
    llb_klinik=tk.Label(form,text="Seçtiğiniz Klinik:",bg="grey",font="Times 12 italic").place(x=10,y=480)
    llb_gun=tk.Label(form,text="Seçtiğiniz Gün:",bg="grey",font="Times 12 italic").place(x=10,y=500)
    llb_doktor=tk.Label(form,text="Seçtiğiniz Doktor:",bg="grey",font="Times 12 italic").place(x=10,y=520)
    llb_saat=tk.Label(form,text="Seçtiğiniz Saat:",bg="grey",font="Times 12 italic").place(x=10,y=540)
    
    llb_ad=tk.Label(form,text=entr1.get()).place(x=200,y=340)
    llb_soyad=tk.Label(form,text=entr2.get()).place(x=200,y=360)
    llb_mail=tk.Label(form,text=entr3.get()).place(x=200,y=380)
    llb_tc=tk.Label(form,text=entr4.get()).place(x=200,y=400)
    llb_tel=tk.Label(form,text=entr5.get()).place(x=200,y=420)
    
    kutu=tk.Label(form,text=x.get()).place(x=200,y=440)
    kutu1=tk.Label(form,text=x1.get()).place(x=200,y=460)
    kutu2=tk.Label(form,text=x2.get()).place(x=200,y=480)
    kutu5=tk.Label(form,text=x5.get()).place(x=200,y=500)
    kutu3=tk.Label(form,text=x3.get()).place(x=200,y=520)
    kutu4=tk.Label(form,text=x4.get()).place(x=200,y=540)
    
    
    label_son=tk.Label(form,text="RANDEVUNUZ BAŞARIYLA OLUŞTURULDU",font="Times 18 ").place(x=10,y=580)

def iptalet():
    form.quit()
    
randevu=tk.Button(form,text="Randevu Al",activebackground="green",command=randevu).place(x=100,y=280)
iptal=tk.Button(form,text="İptal Et",activebackground="red",command=iptalet).place(x=200,y=280)




form.mainloop()
