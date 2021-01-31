from flask import render_template, url_for, redirect, request
from bridgethegap import app
import requests
from bs4 import BeautifulSoup
import urllib.parse
import json


# Home directory
@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/game")
def game():
    return render_template('game.html')

@app.route("/map")
def layout():
    return render_template('map.html')


@app.route("/process_data", methods=['POST'])
def process_data():
    address = request.form['address']
    # address is the data we got from the text box
    # we want to return a json object of all locations that are needed to show up on the map
    data = processZipCode(address)
    return render_template('map.html', data=data)


def processZipCode(zip):
    data = []
    LIMIT = 50
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
                if title is not None:
                    name = title.text.strip()
                    if len(name) > 0:
                        address = street.text.strip() + ', ' + cityState.text.strip()
                        print(name)
                        LL_url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'
                        response = requests.get(LL_url).json()
                        try:
                            lat = response[0]['lat']
                            lon = response[0]['lon']
                            data.append([name, address, lat, lon])
                            if len(data) == LIMIT:
                                break
                        except:
                            continue
    print(data)
    return data