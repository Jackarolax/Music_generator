from midiutil import MIDIFile
from musictheoryFoundation import *
from progressionFoundationRandomizer import *


intonationsBasic = [0, 2/4]
intonationsOffset8Beats = [0, 3/8, 6/8]


x = 6 #x tells, how many times the chord progression will be repeated
progressionFoundation = randomprogressionFoundation()
progressionlengthsingle = len(progressionFoundation)
progressionFoundation *= x
track = 0
channel = 0
time = 0    # In beats
duration = 1    # In beats
tempo = 36   # In BPM (1 Beat = 1 whole note)
volume = 100  # 0-127, as per the MIDI standard
barNum = 0
measurement = barNum//4

addednotes = [] #addednotes is a list of tupels with times and midinotes


print(progressionFoundation)


MyMIDI = MIDIFile()  # One defaults to format 1 (tempo track is created
# automatically)
MyMIDI.addTempo(track, time, tempo)

def whichoctavepitch(hand):
    if hand == "r":
        return('60') 
    elif hand == "l":
        return('40')
    else:
        raise NameError("hand must be 'r' or 'l' ")

def meltTwoListsTogether(list1, list2):
    if len(list1) != len(list2):
        raise Exception("durations don't match kinds")
    meltedlist1list2 = []

    for i, elem1 in enumerate(list1):
        elem2 = list2[i]
        meltedlist1list2.append((elem1, elem2))
    return(meltedlist1list2)


def getoctavedifference(note):
    octavedifference = '00'
    if note > 0 and note < 8:
        return(octavedifference, note)
    elif note > 7:
        while note > 7:
            octavedifference = duodecimalAdd(octavedifference, '10')
            note -= 7
    elif note < 0:
        while note < 0:
            octavedifference = duodecimalAdd(octavedifference, '-10')
            note += 7
    return(octavedifference, note)
                                                                                     # ---> add feature that intonation is an optional parameter
def addnote(hand, octavedifference, midiNote, barNum, beattime, duration, intonations): #"beattime" name is temporary, means something like the time, the note has to be added
    octavepitch = whichoctavepitch(hand)
    finalMidiNote = duodecimalInDecimal(duodecimalAdd(octavedifference, duodecimalAdd(octavepitch, midiNote)))
    finalTime = barNum + beattime
    finalVolume = volume
    if beattime in intonations:
        finalVolume += 25

    if hand == 'r':
        channel = 0
    elif hand == 'l':
        channel = 1

    #if [finalTime, duration, finalMidiNote] not in addednotes:
        #intonation has the same format as beattime and means, which notes are playes more loudly
    MyMIDI.addNote(track, channel, finalMidiNote, finalTime, duration, finalVolume)
    addednotes.append([finalTime, duration, finalMidiNote])
        

def addchord(hand, kind, barNum, beattime, duration, intonations, style, rhythmicStyle, notes, durations):
    chordfoundation = progressionFoundation[barNum]
    if style == 'unchanged':
        if rhythmicStyle == 'broken':
            thischord = duodecimalSort(chord(kind, chordfoundation))
            addseriesofnotesfreely(hand, notes, durations, thischord, barNum, intonations)
        elif rhythmicStyle == 'unchanged':
            for note in chord(kind, chordfoundation):
                addnote(hand, '00', note, barNum, beattime, duration, intonations)

    elif style == 'nearest':
        if rhythmicStyle == 'broken':
            firstchordfoundation = progressionFoundation[0]
            if barNum == 0:
                thischord = chord(kind, firstchordfoundation)
                addseriesofnotesfreely(hand, notes, durations, thischord, barNum, intonations)
            else:
                thischord = nearestTransposition(kind, firstchordfoundation, chordfoundation)
                addseriesofnotesfreely(hand, notes, durations, thischord, barNum, intonations)
        elif rhythmicStyle == 'unchanged':
            if barNum == 0:
                for note in chord(kind, chordfoundation):
                    addnote(hand, '00', note, 0, beattime, duration, intonations)
            else:
                for note in nearestTransposition(kind, progressionFoundation[0], chordfoundation):
                    addnote(hand, '00', note, barNum, beattime, duration, intonations)

            


def addtriad(hand, barNum, beattime, duration, intonations, style, rhythmicStyle, notes, durations): # often used ---> extra function only for triads as a specific chord
    addchord(hand, '0', barNum, beattime, duration, intonations, style, rhythmicStyle, notes, durations)


def notesAndDurationsAddUp(notesAndDurations):
    aboutequalone = 0
    for note, duration in notesAndDurations:
        aboutequalone += duration
    if aboutequalone > 0.9999999 and aboutequalone < 1.0000001:
        # to account for inaccuracy of dealing with fractions when using floats
        return True
    else:
        return False
    

def addseriesofnotes(hand, beatmeasurements, notes, chordfoundation, barNum, intonations):
    duration = 1/beatmeasurements
    beattime = 0
    if len(notes) != beatmeasurements:
        raise Exception("beattime and notes don't add up")

    for note in notes:
        octavedifference = getoctavedifference(note)[0]
        note = getoctavedifference(note)[1]
        addnote(hand, octavedifference, chordfoundation[note], barNum, beattime, duration, intonations)
        beattime += duration

def addseriesofnotesfreely(hand, notes, durations, chordfoundation, barNum, intonations):
    notesAndDurations = meltTwoListsTogether(notes, durations)
    beattime = 0
    if not notesAndDurationsAddUp(notesAndDurations):
        raise Exception("duration and notes don't add up")

    for note, duration in notesAndDurations:
        octavedifference = getoctavedifference(note)[0]
        note = getoctavedifference(note)[1]
        addnote(hand, octavedifference, chordfoundation[note], barNum, beattime, duration, intonations) 
        beattime += duration                                                                              

def addseriesofchords(hand, beatmeasurements, kinds, barNum, intonations, styles):
    duration = 1/beatmeasurements
    beattime = 0
    if not beatmeasurements == len(kinds) == len(styles):
        raise Exception("beatmeasurements, the length of kinds and styles has to be the same")

    for num, kind in enumerate(kinds):
        style = styles[num]
        addchord(hand, kind, barNum, beattime, duration, intonations, style, 'unchanged', [], []) # notes and durations are quite unneccecary here, because there most likely wont be any instances of broken chord seeries
        beattime += duration                                                           #----> notes and durations will be minimized to not be a broken chord
                                                                                       # the empty lists are just placeholders to give enough arguments
def addseriesofchordsfreely(hand, kinds, durations, barNum, intonations, styles):
    kindsAndDurations = meltTwoListsTogether(kinds, durations)
    beattime = 0

    if not len(kinds) == len(durations) == len(styles):
        raise Exception("kinds, durations and styles have to have the same length")

    for num, kindAndDuration in enumerate(kindsAndDurations):
        style = styles[num]
        kind =  kindAndDuration[0]
        duration = kindAndDuration[1]
        addchord(hand, kind, barNum, beattime, duration, intonations, style, 'unchanged', [], [])
        beattime += duration
