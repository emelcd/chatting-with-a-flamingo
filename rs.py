import requests
import json
from bs4 import BeautifulSoup
from uuid import uuid4

def write_json(data,filename='data.json'):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

html = requests.get("https://www.filmaffinity.com/es/listtopmovies.php?list_id=200").text

soup = BeautifulSoup(html,'html.parser', from_encoding='utf-8')

for div in soup.findAll('div',{'class':'mc-info-container'}):
    id_m = uuid4()
    title = div.findAll('a')[0].text
    year = div.find('div',{'class':'mc-title'}).text[-6:-2]
    country = div.find('img')['alt']
    points = div.find('div',{'class','avgrat-box'}).text
    director =div.find('div',{'class','mc-director'}).text.strip()
    cast = div.find('div',{'class','mc-cast'}).findAll('a')
    cast = [a.text for a in cast]
    string = f"{title}, dirigida por {director} en {year}. Actores principales {cast}. Tiene una puntuacion de {points}."
    with open('data.json', encoding='utf-8') as json_file:
        data=json.load(json_file)
        temp=data['mov_details']
        x = {
            "id":str(id_m),
            "title":title,
            "year":year,
            "points":points,
            "director":director,
            "cast":cast
        }
        temp.append(x)
    write_json(data)
    print(string)
    

