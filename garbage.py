"""Functions for fucking with garbage and planets."""


import storage

def IsGarbValid(__garb:list[list[int]], __capacityX:int, __capacityY:int):
    """Checks and returns if Garbage location is valid
    * `__garb`: garbage to validate
    * `__capacityX`: ship's storage capacity's width
    * `__capacityY`: ship's storage capacity's height
    """
    
    for _tile in __garb:
        if _tile[0] < 0: return False
        if _tile[1] < 0: return False
        if _tile[0] >= __capacityX: return False
        if _tile[1] >= __capacityY: return False

    return True



def RotateGarbage(__garb:list[list[int]]):
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
