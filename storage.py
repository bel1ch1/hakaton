"""Storage functions and WFC hashing"""

import json


N = 4



def GarbToHash(__garb):
    new_hash = 0
    for _tile in __garb:
        if (_tile[0] >= N or _tile[1] >= N): 
            print(f"HASHING A BIGGER GARB THAN {N}!!!!")
            return -1
        new_hash += 2**(_tile[0] * N + _tile[1])
    return new_hash



def AAA(__h1, __h2, __d):

    # UP
    if __d == 0: __h2 = __h2 >> N
    # DOWN
    if __d == 1: __h2 = (__h2 << N) & (2**(N*N)-1)
    # RIGHT
    if __d == 2: __h2 = sum((((__h2 >> (N*y)) & (2**(N-1)-1)) << 1) * 2**(N*y) for y in range(N))
    # LEFT
    if __d == 3: __h2 = sum(((((__h2 >> (N*y))) & (2**N-1)) >> 1) * 2**(N*y) for y in range(N))


    # return (__h2)
    return __h1 & __h2 == 0    