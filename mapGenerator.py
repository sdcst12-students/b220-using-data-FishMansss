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
   
    
    ##Generate Mainworld size 
    x = dice(2)-2
    if x in [5,6,7,8,9,10]:
        size=x
    if x in [0,1]:
        size=x+2
    if x in [2,3,4]:
        size=x+1
    world.update(WorldSize=size)    
    ## / atmosphere
    if size<1:
        atmosphere=0
    else:
        y = dice(2)-7+x
        if y in [0,1,2,3,10,11,12,13,14]:
            atmosphere=y+1
        else:
            atmosphere=y
    world.update(Atmosphere=atmosphere)
    
    ##hydrographics
    x = dice(2)-7+world['WorldSize']
    if world['WorldSize']==-1:
        hydrographics = 0
    else: 
        hydrographics = x
    world.update(Hydrographics=hydrographics)
    
    
    print(world)