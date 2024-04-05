import requests
from config import PATH_TO_SERVER, TOKEN, GET_UNIVERSE, TRAVEL


headers = {
    "X-Auth-Token" : f"{TOKEN}"
}

headers2 ={
    "X-Auth-Token" : f"{TOKEN}",
    "Content-Type": "application/json",
}

movet_movet = {
  "planets": [
    "PinkMirror"
  ]
}


def get_universe():
    data = requests.get(PATH_TO_SERVER+GET_UNIVERSE, headers=headers, json=movet_movet)
    print(data.text)


def make_move():
    move_data = requests.post(PATH_TO_SERVER+TRAVEL, headers=headers2, json=movet_movet)
    print(move_data.text)


def tetris_logic():
    pass


make_move()
#get_universe()
