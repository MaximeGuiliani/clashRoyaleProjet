import sys
import requests
import json

########################################
data_player = 0
begining_url = "https://api.clashroyale.com/v1/players/"
end_url = "/upcomingchests?Authorization=Bearer "
html_data_start = "<!DOCTYPE html ><html ><head ><title> mAPxIme </title></head >\
<body ><h1 style='text-align:center'> Welcome to my Clash royale API </h1>"

html_data_end = "</body></html> "
html_body = []
next_chest_index = []
next_chest_name = []

########################################

with open("key.txt") as f:
    my_key = f.read().rstrip("\n")

########################################


def get_data_url(id_player):
    return begining_url + id_player + end_url + my_key


########################################

def create_json(id_player):
    response = requests.get(get_data_url(id_player))
    if response.status_code == 200:
        data_player = response.content.decode("utf-8")
        jsonfile = id_player+'.json'
    with open(jsonfile, 'w') as file:
        file.write(data_player)
        print(data_player)


########################################

def get_chest(id_player):
    next_chest_name.clear()
    next_chest_index.clear()
    jsonfile = id_player+'.json'
    with open(jsonfile) as json_file:
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


def add_data_tohtml():
    html_data = ""
    print('lenght of next chest name ' + str(len(next_chest_name)))
    for i in range(len(next_chest_name)):
        html_data = html_data + \
            str(image_balise(next_chest_name[i])) + \
            str(next_chest_index[i])
    html_body.append(html_data)
########################################


def generate_html():
    for i in range(len(sys.argv)-1):
        create_json(str(sys.argv[i+1]))
        get_chest(str(sys.argv[i+1]))
        add_data_tohtml()
    final_html = html_data_start + \
        html_body[0] + "<br>" + html_body[1] + html_data_end
    with open('index.html', 'w') as html_file:
        html_file.write(final_html)


########################################
generate_html()
