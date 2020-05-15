import requests
from bs4 import BeautifulSoup as bs
import time
import random
import sys
import re



while True:
    _yedek = input('Yedek alinsin mi [e/h]: ').upper()
    print(50 * '-')
    if _yedek == 'E':
        yedek_emoji = '✅'
        _yedek = True
        print(50 * '-')
        break
    elif _yedek == 'H':
        yedek_emoji = '❌'
        _yedek = False
        print(50 * '-')
        break
    else:
        print('Yanlis kullanim lutfen "e" veya "h" yaz.')
        continue

while True:
    _site = input('Baslangic sitesini degistirmek ister misin? [e/h]: ').upper()
    print(50 * '-')
    if _site == 'E':
        site = input('Lutfen degistirmek istedigin sitenin linki yaz. ')
        print(50 * '-')
        try:
            r = requests.get(site)
            if r.status_code == 200:
                break
        except ValueError:
            print('Girdigin link hatali lutfen farkli bir link dene')
            print(50 * '-')
            continue


    elif _site == 'H':
        site = "https://tr.wikipedia.org/wiki/Anasayfa"
        print(50 * '-')
        break

    else:
        print('Yanlis kullanim lutfen "e" veya "h" yaz.')
        print(50 * '-')
        continue

while True:
    print('Yedek alma: ', yedek_emoji , '\nSite: ', site)
    print(50 * '-')
    _baslatma = input('Program bu ayarlar ile baslatilsin mi [e/h] ').upper()
    if _baslatma == 'E':
        print('Program basliyor..')
        print(100 * '-')
        break
    elif _baslatma == 'H':
        print('Program baslatilmiyor. Programdan cikildi.')
        print(100 * '-')
        sys.exit()


dolasilanlar = set()
toplananlar = set()
toplanamayanlar = set()
sayac = 0
_cizgiprint = False


def ozel_print():
    print('\r Basariyla toplanan link sayisi [', len(toplananlar), '] ✅  Hata veren link sayisi [',
          len(toplanamayanlar), '] ❌  Tamamen dolasilan sayfa sayisi [', len(dolasilanlar),
          '] Programin calisma suresi [', int(bitis - baslangic), 'Saniye ]', end="")


baslangic = time.time()

while True:
    try:
        r = requests.get(site)
        soup = bs(r.content, 'html.parser')
        a_lar = soup.find_all('a')
        for link in soup.find_all('a'):
            hrefs = link.get('href')
            try:
                matchObj2 = re.match(r'(^\/wiki\/)', hrefs)
                if matchObj2:
                    hrefs = 'https://tr.wikipedia.org' + hrefs
                matchObj = re.match(r'(^https:\/\/tr\.wikipedia\.org\/)', hrefs)
                if matchObj:
                    r2 = requests.get(hrefs)
                    if r2.status_code == 200:
                        if hrefs in toplananlar:
                            continue
                        else:
                            toplananlar.add(hrefs)
                            dosya = open('dosya.txt', 'a')
                            dosya.write(hrefs)
                            dosya.write('\n')
                            if _yedek:
                                yedek_dosya = open('yedek_dosya.txt', 'a')
                                yedek_dosya.write(hrefs)
                                yedek_dosya.write('\n')
                            bitis = time.time()
                            ozel_print()
                            continue
                    else:
                        # Baglanti basarisiz
                        toplanamayanlar.add(hrefs)
                        bitis = time.time()
                        ozel_print()
                        continue
                else:
                    toplanamayanlar.add(hrefs)
                    bitis = time.time()
                    ozel_print()
                    continue

            except Exception as e:
                toplanamayanlar.add(hrefs)
                continue

    except Exception as e:
        continue



    yeni = toplananlar.pop()
    site = yeni
    dolasilanlar.add(yeni)





