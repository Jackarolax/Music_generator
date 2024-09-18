from random import *
from musictheoryFoundation import *
from progressions import *





def randomkey():
    key = choice(allkeys)
    keynote = identifyKeynoteandCharacteristic(key)[0]
    keyCharacteristic = identifyKeynoteandCharacteristic(key)[1]
    return(keynote, keyCharacteristic)

def randomprogression(keyCharacteristic):
    if keyCharacteristic == 'major':
        progression = choice(repeatingMajorProgressions)()

    elif keyCharacteristic == 'minor':
        progression = choice(repeatingMinorProgressions)()

    elif keyCharacteristic == 'minorDominant5':
        progression = choice(repeatingMinorDominant5Progressions)()

    return(progression)



def randomprogressionFoundation():
    keynote, keyCharacterisic = randomkey()
    progression = randomprogression(keyCharacterisic)
    progressionFoundation = createChordProgressionfoundation(keynote, keyCharacterisic, progression)
    return(progressionFoundation)
