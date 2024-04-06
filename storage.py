"""Storage functions. DO NOT FORGET TO CALL UpdateStorage() !!!"""

import data



STORAGE = []
def StoreGarbage(__pGarbs:dict[str, list[list[int]]], __sGarbs:dict[str, list[list[int]]], __capacityX:int, __capacityY:int):
    """Fills ship storage with garbage.
    * `__pGarbs`: garbage located on the planet
    * `__sGarbs`: garbage located on the ship (!) is edited (!)
    * `__capacityX`: ship's storage capacity's width
    * `__capacityY`: ship's storage capacity's height
    """

    connections_field = [[0 for y in range(__capacityY)] for x in range(__capacityX)]

    # fill conditions_field with ship's garbage
    for _garb in __sGarbs.values():
        for _tile in _garb:
            connections_field[_tile[0]][_tile[1]] += 5
            if _tile[0] > 0: connections_field[_tile[0] - 1][_tile[1]] += 1
            if _tile[1] > 0: connections_field[_tile[0]][_tile[1] - 1] += 1
            if _tile[0] < __capacityX - 1: connections_field[_tile[0] + 1][_tile[1]] += 1
            if _tile[1] < __capacityY - 1: connections_field[_tile[0]][_tile[1] + 1] += 1

    for y in range(__capacityY):
        for x in range(__capacityX):
            print(connections_field[x][y], end='\t')
        print()

