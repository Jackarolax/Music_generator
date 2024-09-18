from musicalElements import *
import os
import shutil


from musicalElementsRandomizer import *
firstElement = choice(chordElements)
secondElement = randomSecondmusicalElement(firstElement)
elementtupels = [[firstElement, secondElement]]


for i in range(len(progressionFoundation)//progressionlengthsingle):
        secondElement = randomSecondmusicalElement(firstElement)
        elementtupels += [[firstElement, secondElement]]



for chordfoundation in progressionFoundation:
    if barNum//4 == 0:
        returnWithParameters(elementtupels[barNum//progressionlengthsingle], barNum)
    else:
        returnWithParameters(elementtupels[barNum//progressionlengthsingle], barNum)
    barNum += 1


MyMIDI.addNote(track, 1, duodecimalInDecimal(duodecimalAdd(
    '40', progressionFoundation[0][1])), len(progressionFoundation), duration, volume)

filenum = 0
filename = 'Melody0.mid'
folder = 'Midi Dateien/'
while os.path.isfile(folder + filename):
    filenum += 1
    filename = 'Melody' + str(filenum) + '.mid'

with open(filename, "wb") as output_file:
    MyMIDI.writeFile(output_file)

shutil.move(filename, folder + filename )