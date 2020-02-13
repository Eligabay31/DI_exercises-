import random
from starwarsday3 import Jedi, Sith

eli = Jedi("eli")
jason = Jedi("jason")
david = Jedi("david")
avi = Sith("avi")
ariel = Sith("ariel")
zury = Sith("zury")

eli.fight(avi)
jason.fight(ariel)
david.fight(zury)

fight = 0


jedi = [eli, jason, david]
sith = [avi, ariel, zury]

while sith:
    jedis = random.choice(jedi)
    siths = random.choice(sith)

    if siths.fight(jedis):
        siths.train()


    else:
        jedis.train()
        sith.remove(siths)
        fight += 1
        print(fight)








