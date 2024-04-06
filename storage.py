"""Storage functions. DO NOT FORGET TO CALL UpdateStorage() !!!"""

import garbage



STORAGE = []

STORAGE_GARB_WEIGHT_AREA = 1
STORAGE_GARB_WEIGHT_DIMENSIONS = -1
def StoreGarbage(__pGarbs:dict[str, list[list[int]]], __sGarbs:dict[str, list[list[int]]], __capacityX:int, __capacityY:int):
    """Fills ship storage with garbage.

    Arguments:
    * `__pGarbs`: garbage located on the planet
    * `__sGarbs`: garbage located on the ship
    * `__capacityX`: ship's storage capacity's width
    * `__capacityY`: ship's storage capacity's height

    Returns two values:
    * Dictionary of placed garbs
    * Is all garbage taken form the planet?
    """

    # make field of "how many adjacent tiles are occupied"
    # also, if tile is occupied itself, it's value is >4
    connections_field = [
        [
            0 + (1 if x == 0 or x == __capacityX-1 else 0)
              + (1 if y == 0 or y == __capacityY-1 else 0)
            for y in range(__capacityY)
        ] 
        for x in range(__capacityX)
    ]

    # keeps track of how much space left on the ship
    _shipCapacityLeft = __capacityX * __capacityY

    # function used for
    def _CutConnections(_garb):

        # decrease current ship's capacity
        _shipCapacityLeft.__sub__(len(_garb))

        # cut nonnections
        for _tile in _garb:
            connections_field[_tile[0]][_tile[1]] += 5
            if _tile[0] > 0: connections_field[_tile[0] - 1][_tile[1]] += 1
            if _tile[1] > 0: connections_field[_tile[0]][_tile[1] - 1] += 1
            if _tile[0] < __capacityX - 1: connections_field[_tile[0] + 1][_tile[1]] += 1
            if _tile[1] < __capacityY - 1: connections_field[_tile[0]][_tile[1] + 1] += 1


    # fill conditions_field with ship's garbage 
    for _garb in __sGarbs.values():
        _CutConnections(_garb)

    # sort garb
    __pGarbs = {
        k: v for k, v in sorted(
            __pGarbs.items(), 
            key=lambda _item: 
                len(_item[1]) * STORAGE_GARB_WEIGHT_AREA
                + max([_tile[0] for _tile in _garb]) * STORAGE_GARB_WEIGHT_DIMENSIONS
                + max([_tile[1] for _tile in _garb]) * STORAGE_GARB_WEIGHT_DIMENSIONS
        )
    }

    # find best position for each garb
    _placed_trash = {}
    _is_all_placed = True
    for _name, _garb in __pGarbs.items():

        _garbBestWeight=-1
        _garbBest=[]

        # get garbage size
        _garbW = max([_tile[0] for _tile in _garb])
        _garbH = max([_tile[1] for _tile in _garb])

        # find best position and rotation
        if _shipCapacityLeft >= len(_garb):

            # check rotations
            for _current_rot in range(4):

                # rotate
                _garb = garbage.RotateGarbage(_garb)

                # check positions
                # substation is used to prevent placing garb out of the ship
                for _currentX in range(    __capacityX - (_garbW if _current_rot % 2 != 0 else _garbH)):
                    for _currentY in range(__capacityY - (_garbH if _current_rot % 2 != 0 else _garbW)):
                        
                        # move
                        _currentGarb = garbage.MoveGarbage(_garb, _currentX, _currentY)

                        # get weight of this position
                        _currentWeight = 0
                        _valid_position = True
                        for _tile in _currentGarb:

                            # check for intersections with already placed garbs
                            if (connections_field[_tile[0]][_tile[1]] > 4):
                                _valid_position = False
                                break
                            
                            # get weight form tile
                            _currentWeight += connections_field[_tile[0]][_tile[1]]

                        # check if better
                        if _valid_position and _currentWeight > _garbBestWeight:
                            _garbBestWeight=_currentWeight
                            _garbBest=_currentGarb

        # check if position is found 
        if _garbBestWeight == -1: 
            _is_all_placed = False
            continue

        # save best garbage
        _placed_trash[_name] = _garbBest
        _CutConnections(_garbBest)

    # return
    return (_placed_trash, _is_all_placed)
