from random import *
from coreMusictheoryFoundation import *


def createChordfoundation(keynote, keyCharacteristic, chordFoundationNumber): #chordfoundation is a self-made synonym for a scale that is more appropriate in this context
    # The keyCharacteristic describes, if it is a minor, or a major scale
    # the keynote and keycharacteristic form a key
    # The chordFoundationNumber is a simplified way to describe the interval between the root of the key and the desired chord
    # decrementation to account for the off by 1 error
    chordFoundationNumber = duodecimalInDecimal(chordFoundationNumber) - 1

    sharp_or_flat = check_if_sharp_or_flat(keynote, keyCharacteristic)

    transposingdifference = keynoteInMidiNumber(keynote)

    # builds a chordfoundation in c major/minor
    root = diatonicChordfoundations(keyCharacteristic)[chordFoundationNumber][1]
    second = diatonicChordfoundations(keyCharacteristic)[chordFoundationNumber][2]
    third = diatonicChordfoundations(keyCharacteristic)[chordFoundationNumber][3]
    fourth = diatonicChordfoundations(keyCharacteristic)[chordFoundationNumber][4]
    fifth = diatonicChordfoundations(keyCharacteristic)[chordFoundationNumber][5]
    sixth = diatonicChordfoundations(keyCharacteristic)[chordFoundationNumber][6]
    seventh = diatonicChordfoundations(keyCharacteristic)[chordFoundationNumber][7]
    # transposes the chordfoundation to the desired key
    root = duodecimalAdd(transposingdifference, root)
    second = duodecimalAdd(transposingdifference, second)
    third = duodecimalAdd(transposingdifference, third)
    fourth = duodecimalAdd(transposingdifference, fourth)
    fifth = duodecimalAdd(transposingdifference, fifth)
    sixth = duodecimalAdd(transposingdifference, sixth)
    seventh = duodecimalAdd(transposingdifference, seventh)

    chordCharacteristic = readAbbreviation(
        diatonicChordfoundations(keyCharacteristic)[chordFoundationNumber][0])

    chordName = midiNumberToNote(root, sharp_or_flat) + " " + chordCharacteristic

    return([chordName, root, second, third, fourth, fifth, sixth, seventh])

#extra funtion for the triad because it is the most used type of chord
def triad(chordfoundation):
    root = chordfoundation[1]
    third = chordfoundation[3]
    fifth = chordfoundation[5]
    return([root, third, fifth])

#the function chord builds a chord out of a chordFOundation
def chord(kind, chordfoundation):
    root = chordfoundation[1]
    second = chordfoundation[2]
    third = chordfoundation[3]
    fourth = chordfoundation[4]
    fifth = chordfoundation[5]
    sixth = chordfoundation[6]
    seventh = chordfoundation[7]
    eighth = duodecimalAdd('10', root)
    ninth = duodecimalAdd('10', second)

    if kind == '0':
        return(triad(chordfoundation))
    if kind == '7':
        return([root, third, fifth, seventh])
    if kind == '9':
        return([root, third, fifth, ninth])
    if kind == '79':
        return([root, third, fifth, seventh, ninth])
    if kind == '4':
        return([root, third, fourth, fifth])
    if kind == '6':
        return([root, third, fifth, sixth])
    if kind == 'o':
        return([root, eighth])
    if kind == 'o0':
        return([root, third, fifth, eighth])
    if kind == 'o7':
        return([root, third, fifth, seventh, eighth])
    if kind == 'o9':
        return([root, third, fifth, eighth, ninth])
    if kind == 'o79':
        return([root, third, fifth, seventh, eighth, ninth])
    if kind == 'o4':
        return([root, third, fourth, fifth, eighth])
    if kind == 'o6':
        return([root, third, fifth, sixth, eighth])
    



# The progression is a string of chordFoundationNumbers
def createChordProgressionfoundation(keynote, keyCharacteristic, progression):
    chordProgressionfoundation = []

    for chordFoundationNumber in progression:
        chordProgressionfoundation.append(createChordfoundation(
            keynote, keyCharacteristic, chordFoundationNumber))

    return(chordProgressionfoundation)

def transposition(chordfoundation, tkind): # transposition parses and returns a chordfoundation
    changedchordfoundation = chordfoundation.copy() # it can only parse a chord foundation
    if tkind == 0:                                   #  possible change: parsing a chord instead of a chord foundation
        return(chordfoundation)
    elif tkind < 0 and tkind > -8:
        for i, tone in list(enumerate(chordfoundation))[1 + 7 + tkind:]: #ex. tkind = -3 => list(enumerate(.....))[1 + 4:]
            changedchordfoundation[i] = duodecimalAdd('-10', tone)
    elif tkind > 0 and tkind < 7:
        for i, tone in list(enumerate(chordfoundation))[1:-7 + tkind]:
            changedchordfoundation[i] = duodecimalAdd('10', tone)
    elif tkind == 7:
        for i, tone in list(enumerate(chordfoundation))[1:]:
            changedchordfoundation[i] = duodecimalAdd('10', tone)
    return(changedchordfoundation)

def averageToneInChord(kind, chordfoundation):
    thischord = chord(kind, chordfoundation)
    return(averageDuodecimal(thischord))

def nearestTransposition(kind, firstchordfoundation, chordfoundation): #chooses the Transposition that has the nearest average tone to the previous chord
    averageOfFirstChordfoundation = averageToneInChord(kind, firstchordfoundation) # possible expansion: diffenerent kind of chords in progression
    differencesEnumerated = []
    for i in range(-7,8):
        differencesEnumerated.append((i, averageOfFirstChordfoundation - averageToneInChord(kind, transposition(chordfoundation, i))))
    nearestChord = duodecimalSort(chord(kind, transposition(chordfoundation, differencesSmallestAbs(differencesEnumerated)[0])))
    return(nearestChord)
    
def differencesSmallestAbs(differencesEnumerated):
    smallestAbsList = [differencesEnumerated[0]]
    for i, difference in differencesEnumerated:
        if abs(difference) == smallestAbsList[0][1]:
            smallestAbsList.append((i, difference))
        elif abs(difference) < smallestAbsList[0][1]:
            smallestAbsList = [(i, difference)]
    return(choice(smallestAbsList))
