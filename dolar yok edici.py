import requests
from bs4 import BeautifulSoup
from playsound import playsound
import time
#veri çekme fonksiyonu yaz

def veri_cekici():

    response= requests.get("https://bigpara.hurriyet.com.tr/doviz/dolar/")

    html_icerik= response.content

    soup= BeautifulSoup(html_icerik,"html.parser")
    for i in soup.find_all("span",{"class": "value dw"}):
        dolarin_deger=(float(i.text.replace(",",".")))
        return  dolarin_deger

kullanicinin_deger= float(input("DOLAR kaç TL'yi aşınca bildirim almak istersiniz?\t:"))
sure=float(input("Kaç dakika arayla bildirim almak istersiniz?\t:"))
while True:



    veri_cekici()

    if veri_cekici()>kullanicinin_deger:
        ###################buradaki yere müziğin pathi girin
        playsound("C:/Users/cakma/Downloads/müzik1.mp3")


    time.sleep(sure*60)