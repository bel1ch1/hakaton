import create
import data
import storage


def outship():
    for y in range(data.SHIP["capacityY"]):
        for x in range(data.SHIP["capacityX"]):
            garbage_at_point = len(list(filter(
                lambda g: any([
                    t[0] == x and t[1] == y for t in g
                ]),
                data.SHIP["garbage"].values()
            )))

            print(
                "." if garbage_at_point == 0
                else "#" if garbage_at_point == 1
                else "!"
                , end=""
            )
        print()

data.SHIP["garbage"][create.MakeName()] = create.MakeGarbage()
print(data.SHIP)
outship()


TRASH_AMOUNT = 10

for _name, _garb in storage.StoreGarbage(
    {create.MakeName(): create.MakeGarbage() for _ in range(TRASH_AMOUNT)},
    data.SHIP["garbage"],
    data.SHIP["capacityX"],
    data.SHIP["capacityY"]
).items():
    data.SHIP["garbage"][_name] = _garb
outship()
