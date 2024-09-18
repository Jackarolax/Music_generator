def duodecimalInDecimal(duoDecimalNumber):
    #converts a duodecimal number(as a string) into a decimal number(as an integer)
    negative = 0
    if duoDecimalNumber[0] == "-":
        duoDecimalNumber = duoDecimalNumber[1:]
        negative = 1
    power = 0
    decimalNumber = 0
    for digit in reversed(duoDecimalNumber):
        if digit == "A":
            decimalNumber += 10*12**power
        elif digit == "B":
            decimalNumber += 11*12**power
        else:
            decimalNumber += int(digit)*12**power
        power += 1

    return(decimalNumber * (-1)**negative)

def decimalInDuodecimal(decimalNumber):
    #converts a decimal number(as an integer) into a duodecimal number(as a string)
    sign = ''
    if decimalNumber < 0:
        decimalNumber = -decimalNumber
        sign = '-'
    if decimalNumber == 0:
        return('0')
    duoDecimalNumber = ""
    while decimalNumber != 0:
        if decimalNumber % 12 == 10:
            duoDecimalNumber += "A"
        elif decimalNumber % 12 == 11:
            duoDecimalNumber += "B"
        else:
            duoDecimalNumber += str(decimalNumber % 12)
        decimalNumber = decimalNumber // 12
    duoDecimalNumber = duoDecimalNumber[::-1]
    return(sign + duoDecimalNumber)


def duodecimalAdd(number1, number2): #adds 2 duodecimal numbers
    result = duodecimalInDecimal(number1) + duodecimalInDecimal(number2)
    return (decimalInDuodecimal(result))

def averageDuodecimal(duodecimalList):
    decimalList = []
    for duodecimalNumber in duodecimalList:
        decimalList.append(duodecimalInDecimal(duodecimalNumber))
    average = sum(decimalList)/len(decimalList)
    return(average)
    

def duodecimalSort(duodecimalList):
    sortedDuodecimalList = []
    decimalList = []
    for duodecimal in duodecimalList:
        decimalList.append(duodecimalInDecimal(duodecimal))
    decimalList = sorted(decimalList)
    for decimal in decimalList:
        sortedDuodecimalList.append(decimalInDuodecimal(decimal))
    return(sortedDuodecimalList)
