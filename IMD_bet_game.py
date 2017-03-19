import numpy as np
from random import randint

np_rounds = np.zeros(shape=(500, 100))

default_level_start = 0

for rounds in range(0, 500):
    a_row = np.zeros(shape=(100))
    level = default_level_start  # define the level now for this play
    for play in range(0, 100):
        dice_100_faces = randint(1, 100)
        if dice_100_faces == 1:
            level = 0
            continue
        else:
            dice_6_faces = randint(1, 6)
            if dice_6_faces in [1, 2]:
                level -= 1
            elif dice_6_faces in [3, 4, 5]:
                level += 1
            else:
                while dice_6_faces == 6:
                    dice_6_faces = randint(1, 6)
                    if dice_6_faces in [1, 2]:
                        level -= 1
                    elif dice_6_faces in [3, 4, 5]:
                        level += 1
        if level < 0:
            level = 0
        a_row[play] = level
    np_rounds[rounds] = a_row

# write bets to file
np_rounds.tofile('output.csv',sep=',',format='%10.2f')
