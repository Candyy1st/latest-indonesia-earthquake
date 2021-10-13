# latest Indonesia Earthquake
this package will get the latest earthquake from BMKG | Meteorological, Climatological, and Geophysical Agency

## How it work?
This package will scrape from [BMKG](https://bmkg.go.id) to get latest quake happened in Indonesia.
This package will use BeautifulSoup4 and Requests, to produce output in the form of JSON that is ready to be used in web or mobile applications.

## How to use
```
from deteksi_gempa import ekstraksi_data, tampilkan_data

if __name__ == '__main__':
    result = ekstraksi_data()
    tampilkan_data(result)
```