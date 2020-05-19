import requests
import urllib.request
from bs4 import BeautifulSoup as bs
import operator
import random

def sembolleri_temizle(tumkelimeler):
    sembolsuz_kelimeler = []
    semboller = '1234567890-\=!@#$%^&*()_+`~[]{:,.<>/?"qwx|};नेपालीไทยമലയാളം한국어日本語čšবাংলাбеларускаяñ中文ệếїקַבָּלָהفارسی' + chr(775)
    for kelime in tumkelimeler:
        for sembol in semboller:
            if sembol in kelime:
                kelime = kelime.replace(sembol, "")
        if len(kelime) > 1:
            sembolsuz_kelimeler.append(kelime)
    return sembolsuz_kelimeler

def sozluk_olustur(tumkelimeler):
    kelimesayisi = {}

    for kelime in tumkelimeler:
        if kelime in kelimesayisi:
            kelimesayisi[kelime] += 1
        else:
            kelimesayisi[kelime] = 1
    return kelimesayisi

puanlama = {}
Arama = input('Arama:  ')
puan = 0

while True:

  puan = 0

  try:
    with open('dosya.txt', 'r') as fin:
        data = fin.read().splitlines(True)
        url = data[0].strip()
    with open('dosya.txt', 'w') as fout:
       fout.writelines(data[1:])
  except:
      break

  r = requests.get(url)
  soup = bs(r.content, 'html.parser')

  dosya_Adi = random.randint(1, 1000000)
  dosya = open(str(dosya_Adi) + '.txt', 'w')

  for kelime in soup.text.split():
    dosya.write('{} \n'.format(kelime))
    if Arama.lower() == kelime.lower():
        puan += 1
  if puan > 0:
   puanlama[puan] = url


for puan,url in sorted(puanlama.items()):
    print("Puan: {}, Url: {}".format(puan,url))


