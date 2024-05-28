import json


with open('data.json') as json_file:
    data = json.load(json_file)
    json_file.close()


while True:
    print("Pais: ")
    pais = input()
    if pais == 'exit':
        break
    print("X: ")
    x = input()
    print("Y: ")
    y = input()
    try:
        x = int(x)
        y = int(y)
    except:
        break

    data[pais] = {}
    data[pais]["x"] = x
    data[pais]["y"] = y


with open("data.json", "w") as json_file:
    json.dump(data, json_file)