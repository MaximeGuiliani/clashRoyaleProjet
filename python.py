import requests
import json

########################################
data_player = 0
begining_url = "https://api.clashroyale.com/v1/players/"
id_player = "%232GPUV2Y0"
end_url = "/upcomingchests?Authorization=Bearer "
html_data = "<!DOCTYPE html ><html ><head ><title > mAPxIme </title ></head >\
<body ><h1> Welcome to my Clash royale API </h1 ><p> My next chest </p>"

next_chest_index = []
next_chest_name = []

########################################

with open("key.txt") as f:
    my_key = f.read().rstrip("\n")

########################################


def get_data_url(id_player):
    return begining_url + id_player + end_url + my_key


########################################
response = requests.get(get_data_url(id_player))


if response.status_code == 200:
    data_player = response.content.decode("utf-8")
    with open('maxime_player.json', 'w') as file:
        file.write(data_player)
        print(data_player)

########################################

with open('maxime_player.json') as json_file:
    data = json.load(json_file)
    for i in data['items']:
        next_chest_index.append(i['index'])
        next_chest_name.append(i['name'])

########################################


def image_balise(chest_name):
    if chest_name == "Silver Chest":
        return'<img src ="https://github.com/RoyaleAPI/cr-api-assets/blob/master/chests/chest-silver.png?raw=true" width=100px height=auto>'

    if chest_name == "Golden Chest":
        return'<img src ="https://github.com/RoyaleAPI/cr-api-assets/blob/master/chests/chest-gold.png?raw=true" width=100px height=auto>'

    if chest_name == "Magical Chest":
        return'<img src ="https://github.com/RoyaleAPI/cr-api-assets/blob/master/chests/chest-magical.png?raw=true" width=100px height=auto>'

    if chest_name == "Mega Lightning Chest":
        return'<img src ="https://github.com/RoyaleAPI/cr-api-assets/blob/master/chests/chest-megalightning.png?raw=true" width=100px height=auto>'

    ####
    if chest_name == "Epic Chest":
        return '<img src ="https://github.com/RoyaleAPI/cr-api-assets/blob/master/chests/chest-epic.png?raw=true" width=100px height=auto>'

    if chest_name == "Legendary Chest":
        return '<img src ="https://github.com/RoyaleAPI/cr-api-assets/blob/master/chests/chest-legendary.png?raw=true" width=100px height=auto>'

    if chest_name == "Giant Chest":
        return '<img src ="https://github.com/RoyaleAPI/cr-api-assets/blob/master/chests/chest-giant.png?raw=true" width=100px height=auto>'

    else:
        return'<img src ="https://github.com/RoyaleAPI/cr-api-assets/blob/master/chests/chest-wooden.png?raw=true" width=100px height=auto>'

########################################


for i in range(len(next_chest_name)):
    html_data = html_data + \
        str(image_balise(next_chest_name[i])) + \
        str(next_chest_index[i])


html_data += "<br>"


html_data = html_data + "</body></html> "


def generate_html():
    with open('index.html', 'w') as html_file:
        html_file.write(html_data)


generate_html()
