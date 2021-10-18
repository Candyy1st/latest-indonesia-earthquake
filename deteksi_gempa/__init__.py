import requests
from bs4 import BeautifulSoup

class deteksi_gempa:
    def __init__(self):
        self.description = 'To get the atest earthquake in Indonesia from BMKG.go.id'
        self.result = None

    def ekstraksi_data(self):

        try:
            content = requests.get('https://bmkg.go.id')
        except Exception:
            return None

        if content.status_code == 200:
            soup = BeautifulSoup(content.text, 'html.parser')

            waktu = soup.find('span', {'class': 'waktu'})
            waktu = waktu.text.split(', ')
            tanggal = waktu[0]
            waktu = waktu[1]

            result = soup.find('ul', {'class': 'list-unstyled'})
            result = result.findChildren('li')

            i = 0
            magnitudo = None
            kedalaman = None
            ls = None
            bt = None
            dirasakan = None

            for res in result:
                if i == 1:
                    magnitudo = res.text
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


            hasil = dict()
            hasil['tanggal'] = tanggal
            hasil['waktu'] = waktu
            hasil['magnitudo'] = magnitudo
            hasil['kedalaman'] = kedalaman
            hasil['koordinat'] = {'ls': ls, 'bt': bt}
            hasil['lokasi'] = lokasi
            hasil['dirasakan'] = dirasakan
            self.result = hasil
        else:
            return None



    def tampilkan_data(self):
        if self.result is None:
            print('Tidak bisa menemukan data gempa terkini')
            return
        print('Gempa Terakhir berdasarkan BMKG')
        print(f"Tanggal {self.result['tanggal']}")
        print(f"Waktu {self.result['waktu']}")
        print(f"Magnitudo {self.result['magnitudo']}")
        print(f"Kedalaman {self.result['kedalaman']}")
        print(f"Koordinat : LS={self.result['koordinat']['ls']}, BT={self.result['koordinat']['bt']}")
        print(f"Lokasi {self.result['lokasi']}")
        print(f"{self.result['dirasakan']}")

    def run(self):
        self.ekstraksi_data()
        self.tampilkan_data()


if __name__ == '__main__':
    gempa = deteksi_gempa()
    print('decription package :', gempa.description)
    # gempa.ekstraksi_data()
    # gempa.tampilkan_data()
