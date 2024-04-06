import requests
from config import PATH_TO_SERVER, TOKEN, GET_UNIVERSE, TRAVEL, COLLECT, RESET, ROUND
import time
from storage import StoreGarbage

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
success = {
    "success": True
}

# <--------------------- Главные функции запросов -------------------------->
def get_universe():
    data = requests.get(PATH_TO_SERVER+GET_UNIVERSE, headers=headers)
    return data


def make_move(movet_movet):
    move_data = requests.post(PATH_TO_SERVER+TRAVEL, headers=headers2, json=movet_movet)
    return move_data.text


def sent_data_collected_garb(data):
    collect = requests.post(PATH_TO_SERVER+COLLECT, headers=headers3, json=data)
    print(collect.text)


def raund_info():
    raund = requests.get(PATH_TO_SERVER+ROUND, headers=headers2)
    return raund.text


def generate_movet_movet(roudrev, i):
    movet_movet = {
        "planets" : [roudrev[i], roudrev[i+1]]
    }
    return movet_movet




# make_move()
# tetris_logic()


roud = []
STOK = "Eden"


def find_stok(stok):
    for i in range(len(planets)-1):
        if planets[i][1] == stok:
            end = planets[i][1]
            #last_planet = planets[i][0]
            return end


def generate_path(end):
    if end == "Earth":
        return roud
    for j in range(len(planets)-1):
        if planets[j][1] == end:
            roud.append(end)
            ends = planets[j][0]
            roud.append(ends)
            return generate_path(ends)


universe = get_universe()
if universe.status_code == 200:

    data = universe.json()
    planets = data.get("universe")
    end = find_stok(STOK)
    generate_path(end)
    roudrev = roud[-2::-1]
    # for i in range(len(roudrev)-1):
    #     mv = generate_movet_movet(roudrev, i)
    #     tetris_logic()
    #     #time.sleep(0.15)
    #     print(mv)
    #     res = make_move(mv)
    #     print(res)
    #restart()
    roud()

    # for i in range(len(planets)-1):
    #     if planets[i][1] == start_pose:
    #         last_planet = start_pose
    #         next_planet = planets[i][1]
    #         movet = generate_movet_movet(last_planet, next_planet)
    #         make_move(movet)



            #next_planets_way.append(planets[i])
    #print(next_planets_way)
# class Generate_path:
#     def __init__(self):
#         pass

#     def find_stok(stok):
#         for i in range(len(planets)):
#             if planets[i][1] == stok:
#                 end = planets[i][1]
#         return end

#     def generate_path(end):
#         for j in range(len(planets)):
#             if planets[i][1] == end:
#                 last_planet = planets[i][0]
