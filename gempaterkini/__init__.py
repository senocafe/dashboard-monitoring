"""
Aplikasi deteksi gempa terkini
Modularisasi Dengan Function
"""
import httpx
import requests
from bs4 import BeautifulSoup

def ekstraksi_data():

    try:
        content = httpx.get('https://www.bmkg.go.id')
        #print(content.status_code)
    except Exception:
        return None

    if content.status_code == 200:
        #print(content.text)
        soup = BeautifulSoup(content.text,'html.parser')
        result = soup.find('span', {'class': 'waktu'})
        result = result.text.split(', ')
        tanggal = result[0]
        waktu = result[1]

        result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        i = 0
        magnitude = None
        kedalaman = None
        ls = None
        bt = None
        lokasi = None
        dirasakan = None

        for res in result:
            #print(i, res)
            if i == 1:
                magnitude = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text
            i = i + 1


        #print(soup.prettify())

        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        hasil['magnitudo'] = magnitude
        hasil['kedalaman'] = kedalaman
        hasil['koordinat'] = {'ls': ls, 'bt':bt}
        hasil['lokasi'] = lokasi
        hasil['dirasakan'] = dirasakan

        return hasil
    else:
        return None


def tampilkan_data(result):
    if result is None:
        print('Tidak bisa menampilkan data gempa terkini')
        return
    print('Gempa Terakhir berdasarkan BMKG Indonesia')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Koordinat: LS={result['koordinat']['ls']}, BT={result['koordinat']['bt']} ")
    print(f"Lokasi {result['lokasi']}")
    print(f"Dirasakan {result['dirasakan']}")


if __name__ == '__main__':
    print('Ini adalah package gempaterkini')
    print('Hai')