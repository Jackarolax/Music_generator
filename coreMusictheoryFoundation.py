from duodecimal import *


def readAbbreviation(abbreviation):
    if abbreviation == 'm':
        return("minor")
    elif abbreviation == 'M':
        return("major")
    elif abbreviation == 'd':
        return("diminished")


# lists all diatonic chords in the midi format (as duodecimal numbers), if we assume, that the root note has a value of 0
def diatonicChordfoundations(keyCharacteristic): #chordfoundation is a self-made synonym for a scale that is more appropriate in this context
    if keyCharacteristic == "minor":  # minor diatonic chordfoundations
        return([['m', '0', '2', '3', '5', '7', '8', 'A'], 
                ['d', '2', '3', '5', '7', '8', 'A', '10'], 
                ['M', '3', '5', '7', '8', 'A', '10', '12'], 
                ['m', '5', '7', '8', 'A', '10', '12', '13'], 
                ['m', '7', '8', 'A', '10', '12', '13', '15'], 
                ['M', '8', 'A', '10', '12', '13', '15', '17'],
                ['M', 'A', '10', '12', '13', '15', '17', '18']])
    elif keyCharacteristic == "minorDominant5":  # minor diatonic chordfoundations with a major dominant chordfoundation
        return([['m', '0', '2', '3', '5', '7', '8', 'A'], 
                ['d', '2', '3', '5', '7', '8', 'A', '10'], 
                ['M', '3', '5', '7', '8', 'A', '10', '12'], 
                ['m', '5', '7', '8', 'A', '10', '12', '13'], 
                ['M', '7', '8', 'B', '10', '12', '13', '15'], 
                ['M', '8', 'A', '10', '12', '13', '15', '17'], 
                ['M', 'A', '10', '12', '13', '15', '17', '18']])
    elif keyCharacteristic == "major":  # major diatonic chordfoundations
        return([['M', '0', '2', '4', '5', '7', '9', 'B'], 
                ['m', '2', '4', '5', '7', '9', 'B', '10'], 
                ['m', '4', '5', '7', '9', 'B', '10', '12'], 
                ['M', '5', '7', '9', 'B', '10', '12', '14'], 
                ['M', '7', '9', 'B', '10', '12', '14', '15'], 
                ['m', '9', 'B', '10', '12', '14', '15', '17'], 
                ['d', 'B', '10', '12', '14', '15', '17', '19']])
    else:
        raise TypeError(keyCharacteristic, " must be a string")


# Converts the usual way to name notes to the midi format (as duodecimal numbers)
def keynoteInMidiNumber(note):                          
    if note == 'c':
        return('0')
    if note == "c sharp" or note == "d flat":
        return('1')
    if note == 'd':
        return('2')
    if note == "d sharp" or note == "e flat":
        return('3')
    if note == 'e':
        return('4')
    if note == 'f':
        return('5')
    if note == "f sharp" or note == "g flat":
        return('6')
    if note == 'g':
        return('7')
    if note == "g sharp" or note == "a flat":
        return('8')
    if note == 'a':
        return('9')
    if note == "a sharp" or note == "b flat":
        return('A')
    if note == 'b':
        return('B')


def midiNumberToNote(midiNumber, sharp_or_flat):
    if midiNumber[-1] == '0':
        return('c')
    if midiNumber[-1] == "1" and sharp_or_flat == "sharp":
        return('c sharp')
    if midiNumber[-1] == "1" and sharp_or_flat == "flat":
        return('d flat')
    if midiNumber[-1] == '2':
        return('d')
    if midiNumber[-1] == "3" and sharp_or_flat == "sharp":
        return('d sharp')
    if midiNumber[-1] == "3" and sharp_or_flat == "flat":
        return('e flat')
    if midiNumber[-1] == '4':
        return('e')
    if midiNumber[-1] == '5':
        return('f')
    if midiNumber[-1] == "6" and sharp_or_flat == "sharp":
        return('f sharp')
    if midiNumber[-1] == "6" and sharp_or_flat == "flat":
        return('g flat')
    if midiNumber[-1] == '7':
        return('g')
    if midiNumber[-1] == "8" and sharp_or_flat == "sharp":
        return('g sharp')
    if midiNumber[-1] == "8" and sharp_or_flat == "flat":
        return('a flat')
    if midiNumber[-1] == '9':
        return('a')
    if midiNumber[-1] == "A" and sharp_or_flat == "sharp":
        return('a sharp')
    if midiNumber[-1] == "A" and sharp_or_flat == "flat":
        return('b flat')
    if midiNumber[-1] == 'B':
        return('b')

# checks if the scale uses flats or sharps
def check_if_sharp_or_flat(keynote, keyCharacteristic):
    if (keynote + " " + keyCharacteristic) in ["g major", "d major", "a major", "e major", "b major", "f sharp major",
                                               "e minor", "b minor", "f sharp minor", "c sharp minor", "g sharp minor", "d sharp minor",
                                               "e minorDominant5", "b minorDominant5", "f sharp minorDominant5", "c sharp minorDominant5", 
                                               "g sharp minorDominant5", "d sharp minorDominant5", "a minorDominant5"]:
        return("sharp")
    if (keynote + " " + keyCharacteristic) in ["f major", "b flat major", "e flat major", "a flat major", "d flat major", "g flat major",
                                               "d minor", "g minor", "c minor", "f minor", "b flat minor", "e flat minor",
                                               "d minorDominant5", "g minorDominant5", "c minorDominant5", "f minorDominant5", 
                                               "b flat minorDominant5", "e flat minorDominant5"]:
        return("flat")
    if (keynote + " " + keyCharacteristic) in ["c major", "a minor"]:
        return("")
    else:
        raise TypeError(keynote, ' ', keyCharacteristic, " is no a known key")
# The keynote gives the the root note of the key

def identifyKeynoteandCharacteristic(key):
    keyNote = ''
    keyCharacteristic = ''
    spacereached = False    
    reversedkey = reversed(key)
    for letter in reversedkey:
        if letter == ' ' and spacereached == False:
            spacereached = True
            continue
        elif spacereached == False:
            keyCharacteristic = letter + keyCharacteristic
        elif spacereached == True:
            keyNote = letter + keyNote
    return(keyNote, keyCharacteristic)

allkeys = ["c major",
           "g major", "d major", "a major", "e major", "b major", "f sharp major",
           "f major", "b flat major", "e flat major", "a flat major", "d flat major", "g flat major",
           "a minor",
           "e minor", "b minor", "f sharp minor", "c sharp minor", "g sharp minor", "d sharp minor",
           "d minor", "g minor", "c minor", "f minor", "b flat minor", "e flat minor",
           "a minorDominant5",
           "d minorDominant5", "g minorDominant5", "c minorDominant5", "f minorDominant5", "b flat minorDominant5", "e flat minorDominant5",
           "e minorDominant5", "b minorDominant5", "f sharp minorDominant5", "c sharp minorDominant5", "g sharp minorDominant5", "d sharp minorDominant5"
           "a minor",
           "e minor", "b minor", "f sharp minor", "c sharp minor", "g sharp minor", "d sharp minor",
           "d minor", "g minor", "c minor", "f minor", "b flat minor", "e flat minor",
           "a minorDominant5",
           "d minorDominant5", "g minorDominant5", "c minorDominant5", "f minorDominant5", "b flat minorDominant5", "e flat minorDominant5",
           "e minorDominant5", "b minorDominant5", "f sharp minorDominant5", "c sharp minorDominant5", "g sharp minorDominant5", "d sharp minorDominant5"
           ]
           #the minoor keys are duplicated, to make it more likely to choose a minor key

           