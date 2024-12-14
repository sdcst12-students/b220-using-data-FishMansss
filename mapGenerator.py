import random, os
os.system('cls')

def dice(numberOfDie):
    x = random.randint(numberOfDie,(6 * numberOfDie))
    return x

world = {}
for i in range(1):
##starport
    x = dice(2)
    if x ==2 or x ==3 or x==4:
        sp = 'A'
    if x ==5 or x ==6:
        sp = 'B'
    if x  in [7,8]:
        sp = 'C'
    if x ==9:
        sp = 'D'
    if x ==10 or x ==11:
        sp = 'E'
    if x ==12:
        sp = 'X'
    world.update(starport=sp)

    ##check for naval base
    x = dice(2)
    if x<7:
        navalBase=False
    if x>6:
        navalBase=True
    world.update(NavalBase=navalBase)

    ##check for scout base
    x = dice(2)
    if x<7:
        scoutBase=False
    if x>6:
        scoutBase=True
    world.update(ScoutBase=scoutBase)

    ##check for gas giant
    x = dice(2)
    if x<10:
        gasGiant=False
    if x>6:
        gasGiant=True
    world.update(GasGiant=gasGiant)

    ##Generate random name
    x = dice(100)
    name = "lV" + str(x)


    world.update(Name=name)
    print(world)
    
    ##Generate Mainworld size / atmosphere
    x = dice(2)-2
    y = dice(2)-7+x
    if x==0:
        y=0
    