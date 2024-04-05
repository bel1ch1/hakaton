import requests
from config import PATH_TO_SERVER, TOKEN, GET_UNIVERSE, TRAVEL, COLLECT


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


movet_movet = {
  "planets": [
    "V2VPTYB55",
    "Gaylord"
  ]
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
    print(data.text)


def make_move():
    move_data = requests.post(PATH_TO_SERVER+TRAVEL, headers=headers2, json=movet_movet)
    print(move_data.text)


def tetris_logic():
    collect = requests.post(PATH_TO_SERVER+COLLECT, headers=headers3, json=collect_garb)
    print(collect.text)


#get_universe()
make_move()
#tetris_logic()
