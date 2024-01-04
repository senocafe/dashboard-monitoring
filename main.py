
"""
Aplikasi deteksi gempa terkini
Modularisasi Dengan Function
Modularisasi dengan Package
Import BS4
Import httpx
"""
import gempaterkini

if __name__ == '__main__':
    print('Aplikasi utama')
    result = gempaterkini.ekstraksi_data()
    gempaterkini.tampilkan_data(result)



    