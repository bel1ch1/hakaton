"""Functions to emulate GET responses form the server"""



import random


MAKENAME_ALPHABET = "1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
MAKENAME_NAME_LENGTH_WEIGHTS = {
    3: 3,
    4: 4,
    5: 5,
    6: 4,
    7: 3,
    8: 2,
    9: 1,
}
MAKENAME_NAME_HASH = []
def MakeName():
    new_name = ""

    while new_name == "" or new_name in MAKENAME_NAME_HASH:
        tile_length = random.choices(
            list(MAKENAME_NAME_LENGTH_WEIGHTS.keys()), 
            list(MAKENAME_NAME_LENGTH_WEIGHTS.values())
        )[0]

        while len(new_name) < tile_length:
            new_name += random.choice(MAKENAME_ALPHABET)

    MAKENAME_NAME_HASH.append(new_name)
    return new_name
    
    


MAKEGARBAGE_SEGMENT_AMOUNT_WEIGHTS = {
    3: 3,
    4: 3,
    5: 2,
    6: 1
}
def MakeGarbage():
    new_garbage = [ [0,0] ]

    tile_amount = random.choices(
        list(MAKEGARBAGE_SEGMENT_AMOUNT_WEIGHTS.keys()), 
        list(MAKEGARBAGE_SEGMENT_AMOUNT_WEIGHTS.values())
    )[0]

    minx, miny = 0, 0
    while len(new_garbage) < tile_amount:
        from_tile = random.choice(list(new_garbage))

        new_direction = random.randint(0, 3)
        new_tile = [
                from_tile[0] + (-1 if new_direction == 0 else 1 if new_direction == 1 else 0),
                from_tile[1] + (-1 if new_direction == 2 else 1 if new_direction == 3 else 0)
            ]
        
        if new_tile[0] < minx: minx = new_tile[0]
        if new_tile[1] < miny: miny = new_tile[1]
        
        if new_tile not in new_garbage:
            new_garbage.append(new_tile)
    
    new_garbage = list(map(
        lambda t: [
            t[0] - minx, 
            t[1] - miny
        ],
        new_garbage
    ))

    return new_garbage