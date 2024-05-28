import json
import random

def get_coordinates():

    with open('data.json') as json_file:
        data = json.load(json_file)
        json_file.close()
    lista = list(data.items())

    first = [random.choice(lista)]
    second =[random.choice(lista)]
    while second == first:
        second =[random.choice(lista)]
    third =[random.choice(lista)]
    while third==first or third==second:
        third =[random.choice(lista)]
    
    coordinates = {
        'country1': first[0][0],
        'c1x': first[0][1]['x'],
        'c1y': first[0][1]['y'],
        'country2': second[0][0],
        'c2x': second[0][1]['x'],
        'c2y': second[0][1]['y'],
        'country3': third[0][0],
        'c3x': third[0][1]['x'],
        'c3y': third[0][1]['y'],
    }
    return coordinates
    ''' 
    x1 = {'x1':first[0][1]['x']}
    y1 = {'y1':first[0][1]['y']}
    x2 = {'x2':second[0][1]['x']}
    y2 = {'y2':second[0][1]['y']}
    pais1 = {'p1': first[0][0]}
    pais2 = {'p2': second[0][0]}
    data = {}
    pais = {}
    data.update(x1)
    data.update(y1)
    data.update(x2)
    data.update(y2)
    pais.update(pais1)
    pais.update(pais2)

    print(data, pais)
    '''