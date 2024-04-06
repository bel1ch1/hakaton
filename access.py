import requests
from config import PATH_TO_SERVER, TOKEN, GET_UNIVERSE, TRAVEL, COLLECT
from generate_path import Generate_path
import json


headers = {
    "X-Auth-Token" : f"{TOKEN}",
}

headers2 ={
    "X-Auth-Token" : f"{TOKEN}",
    "Content-Type": "application/json",
}

headers3 = {
    "X-Auth-Token" : f"{TOKEN}",
    "Content-Type" : "application/json",
}



collect_garb = {
"garbage": {
"71B2XMi": [
[
2,
10
],
[
2,
9
],
[
2,
8
],
[
3,
8
]
]
}
}


# <--------------------- Главные функции запросов -------------------------->
def get_universe():
    data = requests.get(PATH_TO_SERVER+GET_UNIVERSE, headers=headers, json=movet_movet)
    return data


def make_move(movet_movet):
    move_data = requests.post(PATH_TO_SERVER+TRAVEL, headers=headers2, json=movet_movet)
    print(move_data.text)


def tetris_logic():
    collect = requests.post(PATH_TO_SERVER+COLLECT, headers=headers3, json=collect_garb)
    print(collect.text)


def generate_movet_movet(current_planet, next_planet):
    movet_movet = {
        "planets": [
        f"{current_planet}",
        f"{next_planet}"
        ]
    }
    return movet_movet


# make_move()
# tetris_logic()

next_planets_way = []
interest_points = []
stok = "Eden"


def for_data_py():
    universe = get_universe()
    if universe.status_code == 200:

        data = universe.json()
        planets = data.get("universe")
        start_pose = data["universe"][0][0]

        for i in range(len(planets)-1):
            if planets[i][1] == start_pose:
                last_planet = start_pose
                next_planet = planets[i][1]
                movet = generate_movet_movet(last_planet, next_planet)
                make_move(movet)



            #next_planets_way.append(planets[i])
    #print(next_planets_way)
