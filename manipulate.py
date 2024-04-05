"""Functions for fucking with garbage and planets."""



def RotateGarbage(__garb):
    """Rotates garbage clockwise once.
    
    * `__garb`: garbage to rotate
    """

    # find size of this garbage
    garb_width = 0
    garb_height = 0
    for _tile in __garb:
        if _tile[0] > garb_width:  garb_width = _tile[0]
        if _tile[1] > garb_height: garb_height = _tile[1]

    # rotate
    manipulated_garb = [
        [
            _tile[1],
            garb_width-_tile[0]
        ]
        for _tile in __garb
    ]

    # return
    return manipulated_garb



def MoveGarbage(__garb:list[list[int]], __x:int, __y:int):
    """Moves garbage in direction.
    
    * `__garb`: garbage to move
    * `__x`: distance to move in x axis
    * `__y`: distance to move in y axis
    """

    # move
    manipulated_garb = [
        [
            _tile[0] + __x,
            _tile[1] + __y
        ]
        for _tile in __garb
    ]

    # return
    return manipulated_garb