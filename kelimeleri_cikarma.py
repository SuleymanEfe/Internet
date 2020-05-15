import requests
import urllib.request
from bs4 import BeautifulSoup as bs
import operator


def sembolleri_temizle(tumkelimeler):
    sembolsuz_kelimeler = []
    semboller = '1234567890-\=!@#$%^&*()_+`~[]{:,.<>/?"qwx|};नेपालीไทยമലയാളം한국어日本語čšবাংলাбеларускаяñ中文ệếїקַבָּלָהفارسی' + chr(775)
    for kelime in tumkelimeler:
        for sembol in semboller:
            if sembol in kelime:
                kelime = kelime.replace(kelime, "")
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

tumkelimeler = []


while True:
  try:
    with open('dosya.txt', 'r') as fin:
        data = fin.read().splitlines(True)
        url = data[0].strip()
    with open('dosya.txt', 'w') as fout:
        fout.writelines(data[1:])
  except:
      print('DOSYANIN ICI BOS')
      break

  r = requests.get(url)
  soup = bs(r.content, 'html.parser')

  for kelimegruplari in soup.find_all('p'):
     icerik = kelimegruplari.text
     kelimeler = icerik.lower().split()

     for kelime in kelimeler:
         tumkelimeler.append(kelime)




tumkelimeler = sembolleri_temizle(tumkelimeler)
kelimesayisi = sozluk_olustur(tumkelimeler)
for anahtar, deger in sorted(kelimesayisi.items(),key= operator.itemgetter(1)):
    print(anahtar, ': ', deger)

