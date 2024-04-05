import requests
from config import PATH_TO_SERVER, TOKEN


headers = {
    "X-Auth-Token" : f"{TOKEN}"
}

def get_universe():
    data = requests.get(PATH_TO_SERVER+"/player/universe", headers=headers)
    print(data.text)


def make_move():
    pass


def tetris_logic():
    pass
