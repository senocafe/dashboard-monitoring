"""
Aplikasi deteksi gempa terkini
Modularisasi Dengan Function
"""


def ekstraksi_data():
    """
    Tanggal: 13 Desember 2023
    Waktu: 00:37:16 WIB
    Magnitudo: 3.9
    Kedalaman: 14 km
    Lokasi: LS=0.73 BT=-119.62
    Pusat Gempa: Pusat gempa berada di Laut 41 Km Barat Daya Donggala
    Dirasakan: Dirasakan (Skala MMI): II-III Palu
    :return:
    """
    hasil = dict()
    hasil['tanggal'] = '13 Desember 2023'
    hasil['waktu'] = '00:37:16 WIB'
    hasil['magnitudo'] = 3.9
    hasil['kedalaman'] = 14
    hasil['lokasi'] = {'ls': 0.73, 'bt':-119.62}
    hasil['pusat'] = 'Pusat gempa berada di Laut 41 Km Barat Daya Donggala'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): II-III Palu'

    return hasil


def tampilkan_data(result):
    print('Gempa Terakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']} KM")
    print(f"Lokasi: LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']} ")
    print(f"Pusat {result['pusat']}")
    print(f"Dirasakan {result['dirasakan']}")



if __name__ == '__main__':
    print('Aplikasi utama')
    result = ekstraksi_data()
    tampilkan_data(result)

    