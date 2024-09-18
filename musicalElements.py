from noteaddingFoundation import *

def element__c__OneBeat(kinds, barNum, hand, style):  # c: chord
    addseriesofchords(hand, 1, kinds, barNum, intonationsBasic, [style])

def element__c_cc__FourBeat(kinds, barNum, hand, style):  # c: chord
    kinds = kinds[:-1]
    style = [style] * 3
    durations = [2/4, 1/4, 1/4]
    addseriesofchordsfreely(hand, kinds, durations, barNum, intonationsBasic, style)

def element__cc_c__FourBeat(kinds, barNum, hand, style):  #c: chord
    kinds = kinds[:-1]
    style = [style] * 3
    durations = [1/4, 1/4, 2/4]
    addseriesofchordsfreely(hand, kinds, durations, barNum, intonationsBasic, style)
       
def element__ccc__ThreeBeat(kinds, barNum, hand, style):  # c:chord
    style = [style] * 3
    addseriesofchords(hand, 3, kinds, barNum, intonationsBasic, style)
       
def element__c__c__c___OffsetEightBeat(kinds, barNum, hand, style):  # c: chord
    kinds = kinds[:-5]
    style = [style] * 3
    durations = [3/8, 3/8, 2/8]
    addseriesofchordsfreely(hand, kinds, durations,  barNum, intonationsOffset8Beats, style)
       
def element__to__TwoBeat(kinds, barNum, hand, style):  # t:triad o:octave
    style = [style] * 2
    addseriesofchords(hand, 2, ['0', 'o'],  barNum, intonationsBasic, style)

def element__1585__FourBeat(kinds, barNum, hand, style):  
    addchord(hand, 'o0', barNum, 0, 1, intonationsBasic, style, 'broken', [0, 2, 3, 2], [1/4]*4)

def element__1515__FourBeat(kinds, barNum, hand, style):  
    addchord(hand, '0', barNum, 0, 1, intonationsBasic, style, 'broken', [0, 2, 0, 2], [1/4]*4)

def element__15__TwoBeat(kinds, barNum, hand, style):  
    addchord(hand, '0', barNum, 0, 1, intonationsBasic, style, 'broken', [0, 2], [1/2]*2)

def element__1__1__FourBeat(kinds, barNum, hand, style):  
    addchord(hand, '0', barNum, 0, 1, intonationsBasic, style, 'broken', [0, 0], [3/4, 1/4])

def element__1__1__5___Offset(kinds, barNum, hand, style):
    addchord(hand, '0', barNum, 0, 1, intonationsOffset8Beats, style, 'broken', [0, 0, 2], [3/8, 3/8, 2/8])

def element__135787__SixBeat(kinds, barNum,  hand, style):  
    addchord(hand, 'o7', barNum, 0, 1, intonationsBasic, style, 'broken', [0, 1, 2, 3, 4, 3], [1/6]*6)

def element__1353__FourBeat(kinds, barNum, hand, style):  
    addchord(hand, '0', barNum, 0, 1, intonationsBasic, style, 'broken', [0, 1, 2, 1], [1/4]*4)

def element__1535__FourBeat(kinds, barNum, hand, style):  
    addchord(hand, '0', barNum, 0, 1, intonationsBasic, style, 'broken', [0, 2, 1, 2], [1/4]*4)

def element__53153153__OffsetEightBeat(kinds, barNum, hand, style):  
    addchord(hand, '0', barNum, 0, 1, intonationsOffset8Beats, style, 'broken', [2, 1, 0, 2, 1, 0, 2, 1], [1/8]*8)

def element__53153151__OffsetEightBeat(kinds, barNum, hand, style):  
    addchord(hand, '0', barNum, 0, 1, intonationsOffset8Beats, style, 'broken', [2, 1, 0, 2, 1, 0, 2, 0], [1/8]*8)


allElements = []
allElementsString = []

for functionStringmusicalElements in dir():
    if len(functionStringmusicalElements) > 8 and functionStringmusicalElements[:9] == "element__":
        allElements.append(globals()[functionStringmusicalElements])
        allElementsString.append(functionStringmusicalElements)


melodyElements = []
melodyElementsString = []
chordElements = []
chordElementsString = []

for elementsFunctionString in allElementsString:
    if elementsFunctionString[10].isnumeric(): 
        melodyElements.append(globals()[elementsFunctionString])
        melodyElementsString.append(elementsFunctionString)
    else:
        chordElements.append(globals()[elementsFunctionString])
        chordElementsString.append(elementsFunctionString)

oneBeatElements = []
twoBeatElements = []
threeBeatElements = []
fourBeatElements = []
sixBeatElements = []
eightBeatElements = []

for elementString in allElementsString:
    if elementString[-7:] == 'OneBeat':
        oneBeatElements.append(globals()[elementString])
    elif elementString[-7:] == 'TwoBeat':
        twoBeatElements.append(globals()[elementString])
    elif elementString[-9:] == 'ThreeBeat':
        threeBeatElements.append(globals()[elementString])
    elif elementString[-8:] == 'FourBeat':
        fourBeatElements.append(globals()[elementString])
    elif elementString[-7:] == 'SixBeat':
        sixBeatElements.append(globals()[elementString])
    elif elementString[-15:] == 'OffsetEightBeat':
        eightBeatElements.append(globals()[elementString])

    
def none(*args):
    return


