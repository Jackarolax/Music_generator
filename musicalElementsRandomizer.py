from itertools import combinations_with_replacement
from musicalElements import *


def buildSubset(list1, list2):
    subsetlist = []
    list2copy = list(list2)
    for elem in list1:
        if elem in list2copy:
            subsetlist.append(elem)
            list2copy.remove(elem)
    return(subsetlist)

allElementsCopy = list(allElements)
compatibleWith3Beat = list(oneBeatElements + twoBeatElements + fourBeatElements + sixBeatElements)
compatibleWith8Beat = list(oneBeatElements + twoBeatElements + fourBeatElements + eightBeatElements)



def randomSecondmusicalElement(firstElement):
    # firstElement has to be a chord element
    if firstElement in oneBeatElements + twoBeatElements:
        secondElement = choice(allElementsCopy)
        allElementsCopy.remove(secondElement)

    elif firstElement in threeBeatElements or sixBeatElements:
        secondElement = choice(compatibleWith3Beat)
        compatibleWith3Beat.remove(secondElement)

    elif firstElement in fourBeatElements + eightBeatElements:
        secondElement = choice(compatibleWith8Beat)
        compatibleWith8Beat.remove(secondElement)

    return(secondElement)
        
def returnWithParameters(musicalElements, barNum):
    if len(musicalElements) == 2:
        firstElement = musicalElements[0]
        secondElement = musicalElements[1]
    elif len(musicalElements) == 1:
        firstElement = musicalElements[0]
        secondElement = none
    else:
        raise Exception('musicalElements has to contain either 1 or 2 elements')

    if firstElement in oneBeatElements:
        firstElement(['0'], barNum, 'l', 'nearest')

    elif firstElement in twoBeatElements:
        firstElement(['0']*2, barNum, 'l', 'nearest')
    
    elif firstElement in threeBeatElements:
        firstElement(['0']*3, barNum, 'l', 'nearest')

    elif firstElement in fourBeatElements:
        firstElement(['0']*4, barNum, 'l', 'nearest')

    elif firstElement in sixBeatElements:
        firstElement(['0']*6, barNum, 'l', 'nearest')

    elif firstElement in eightBeatElements:
        firstElement(['0']*8, barNum, 'l', 'nearest')


    if secondElement in oneBeatElements:
        secondElement(['0'], barNum, 'r', 'nearest')

    elif secondElement in twoBeatElements:
        secondElement(['0']*2, barNum, 'r', 'nearest')
    
    elif secondElement in threeBeatElements:
        secondElement(['0']*3, barNum, 'r', 'nearest')

    elif secondElement in fourBeatElements:
        secondElement(['0']*4, barNum, 'r', 'nearest')

    elif secondElement in eightBeatElements:
        secondElement(['0']*8, barNum, 'r', 'nearest')

