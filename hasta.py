class Hasta:
    def __init__(self):
        self.__isim = ""
        self.__soyisim = ""
        self.__tc = 0
        self.__mail = ""
        self.__tel = 0
   
    def set_isim(self,isim):
        self.__isim=isim
    
    def get_isim(self):
        return self.__isim
    
    def set_soyisim(self,soyisim):
        self.__soyisim=soyisim
        
    def get_soyisim(self):
        return self.__soyisim
    
    def set_tc(self,tc):
        self.__tc=tc
        
    def get_tc(self):
        return self.__tc
    
    def set_mail(self,mail):
        self.__mail=mail
    
    def get_mail(self):
        return self.__mail
    
    def set_tel(self,tel):
        self.__tel=tel
        
    def get_tel(self):
        return self.__tel