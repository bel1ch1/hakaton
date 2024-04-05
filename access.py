import requests
from config import PATH_TO_SERVER, TOKEN, GET_UNIVERSE


headers = {
    "X-Auth-Token" : f"{TOKEN}"
}


def get_universe():
    data = requests.get(PATH_TO_SERVER+GET_UNIVERSE, headers=headers)
    print(data.text)


def make_move():
    requests.post(PATH_TO_SERVER)


def tetris_logic():
    pass


get_universe()
