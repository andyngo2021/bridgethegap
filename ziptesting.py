import requests
from bs4 import BeautifulSoup
import urllib.parse


def processZipCode(zip):
    data = []

    url = "https://www.shelterlist.com/zip.php?zip={}&submit=Search".format(zip)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')    
    shelters = soup.find_all(class_='')
    for shelter in shelters:
        street = shelter.find(class_='street')
        if street is not None:
            cityState = shelter.find(class_='cityState')
            if cityState is not None:
                title = shelter.find('a')
                if title is not None and len(title) > 0:
                    name = title.text.strip()
                    address = street.text.strip() + ', ' + cityState.text.strip()
                    # print(f'{name} - {address}')
                    LL_url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'
                    response = requests.get(LL_url).json()
                    try:
                        lat = response[0]['lat']
                        lon = response[0]['lon']
                        data.append({
                            'title':name, 'address':address, 'lat':lat, 'lon':lon
                        })
                    except:
                        pass
    return data
                    





print(processZipCode(92683))