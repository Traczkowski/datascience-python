# import dog as d
from models.dog import *

# from IPython import embed
# embed()

names = ['sam', 'fido', 'lassy']
dogs = [Dog(n, i + 3) for i, n in enumerate(names)]

print(dogs)
print('the first dogs name is:', dogs[0].name)

combo = dogs[0] + dogs[1]
print('combo is', combo)

from IPython import embed
embed()
