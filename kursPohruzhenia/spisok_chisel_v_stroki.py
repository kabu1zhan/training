from functools import partial
def privetstvie(znakomiy,neznakomiy):
    return '{}, {}!'.format(znakomiy,neznakomiy)
name = input()
privet = partial(privetstvie,znakomiy='privet')
zdrastvuyte = partial(privetstvie, neznakomiy='zdrastvuyte')
imena = []
for _ in imena:
    if name in imena:
        print(privet(name))
    else:
        print(zdrastvuyte(name))
        imena.append(name)