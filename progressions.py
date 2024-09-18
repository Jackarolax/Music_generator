

#all functions return progressions and all progressions are meant to be repeated

def majorBasic():
    return('1455')

def majorSimple():
    return('1515')

def majorPopular():
    return('6415')


def minorSomeoneLikeYou():
    return('1634')

def minorBasic():
    return('1637')

def minorDJGotUsFallinInLoveAgain():
    return('1766')

def minorBeliever():
    return('1167')

def minorPopular():
    return('1367')

def minorWellerman():
    return('6341')

def minorHighEnough():
    return('6411')

def minorAmelie():
    return('1357')


def minorDominant57rings():
    return('1645')

def minorDominant5BadGuy():
    return('1455')

def minorDominant5ThereforeIAm():
    return('1155')

def minorDominant5Havana():
    return('1655')

def minorDominant5Basic():
    return('1365')

def minorDominant5Warriors():
    return('1765')

def minorDominant5TakeMeToChurch():
    return('1531')

repeatingMajorProgressions = []
repeatingMinorProgressions = []
repeatingMinorDominant5Progressions = []


for functionStringProgression in dir():
    if not functionStringProgression[0] == '_':
        if 'minorDominant5' in functionStringProgression:
            repeatingMinorDominant5Progressions.append(globals()[functionStringProgression])

        elif 'minor' in functionStringProgression:
            repeatingMinorProgressions.append(globals()[functionStringProgression])

        elif 'major' in functionStringProgression:
            repeatingMajorProgressions.append(globals()[functionStringProgression])




