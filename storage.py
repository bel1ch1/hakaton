"""Storage functions. DO NOT FORGET TO CALL UpdateStorage() !!!"""

import garbage



STORAGE = []
def StoreGarbage(__pGarbs:dict[str, list[list[int]]], __sGarbs:dict[str, list[list[int]]], __capacityX:int, __capacityY:int):
    """Fills ship storage with garbage.
    * `__pGarbs`: garbage located on the planet
    * `__sGarbs`: garbage located on the ship (!) is edited (!)
    * `__capacityX`: ship's storage capacity's width
    * `__capacityY`: ship's storage capacity's height
    """

    connections_field = [
        [
            0 + (1 if x == 0 or x == __capacityX-1 else 0)
              + (1 if y == 0 or y == __capacityY-1 else 0)
            for y in range(__capacityY)
        ] 
        for x in range(__capacityX)
    ]

    # fill conditions_field with ship's garbage
    def _CutConnections(_garb):
        for _tile in _garb:
            connections_field[_tile[0]][_tile[1]] += 5
            if _tile[0] > 0: connections_field[_tile[0] - 1][_tile[1]] += 1
            if _tile[1] > 0: connections_field[_tile[0]][_tile[1] - 1] += 1
            if _tile[0] < __capacityX - 1: connections_field[_tile[0] + 1][_tile[1]] += 1
            if _tile[1] < __capacityY - 1: connections_field[_tile[0]][_tile[1] + 1] += 1

    for _garb in __sGarbs.values():
        _CutConnections(_garb)

    # sort garb
    # TODO

    # find best position for each garb
    _placed_trash = {}
    for _name, _garb in __pGarbs.items():

        _garbBestLocationX=0
        _garbBestLocationY=0
        _garbBestLocationR=0
        _garbBestLocationW=-1
        _garbBest=_garb

        _garbW = max([_tile[0] for _tile in _garb])
        _garbH = max([_tile[1] for _tile in _garb])

        for _rotI in range(4):
            _garb = garbage.RotateGarbage(_garb)

            for _xI in range(    __capacityX - (_garbW if _rotI % 2 != 0 else _garbH)):
                for _yI in range(__capacityY - (_garbH if _rotI % 2 != 0 else _garbW)):
                    _garbI = garbage.MoveGarbage(_garb, _xI, _yI)
                    _wI = 0
                    _valid_position = True
                    for _tile in _garbI:
                        if (connections_field[_tile[0]][_tile[1]] > 4):
                            _valid_position = False
                            break
                        else:
                            _wI += connections_field[_tile[0]][_tile[1]]

                    if _valid_position and _wI > _garbBestLocationW:
                        _garbBestLocationX=_xI
                        _garbBestLocationY=_yI
                        _garbBestLocationR=_rotI
                        _garbBestLocationW=_wI
                        _garbBest=_garbI

        # if possible to position 
        if _garbBestLocationW == -1: 
            print("CANNOT STORE GARBAGE")
            continue

        # add garb in best position
        _placed_trash[_name] = _garbBest
        _CutConnections(_garbBest)
    return _placed_trash
