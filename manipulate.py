"""Functions for fucking with garbage and planets"""



def RotateGarbage(__garb):

    # find size of this garbage
    garb_width = 0
    garb_height = 0
    for _tile in __garb:
        if _tile[0] > garb_width:  garb_width = _tile[0]
        if _tile[1] > garb_height: garb_height = _tile[1]

    # rotate and return
    return [
        [
            _tile[1],
            garb_width-_tile[0]
        ]
        for _tile in __garb
    ]