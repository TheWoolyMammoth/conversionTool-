import pytest


def convertTemp(userUnit,userValue,convertedUnit):
    # assuming temp is of the form 'number_tempunit' or 'number_temp unit'
    # unit can be (F,C,K)
    # split temp into temp and unit
    listTempUnits = ['fahrenheit', 'celsius', 'kelvin']
    if userUnit in listTempUnits:
        match userUnit:
            case 'fahrenheit':
                if convertedUnit == 'celsius':
                    conversion = fToC(userValue)
                    conversionStatement = f'{userValue}\u00B0 {userUnit} -> {conversion:.2f}\u00B0 {convertedUnit}'
                elif convertedUnit == 'kelvin':
                    conversion = fToK(userValue)
                    conversionStatement = f'{userValue}\u00B0 {userUnit} -> {conversion:.2f}\u00B0 {convertedUnit}'
            case 'celsius':
                if convertedUnit == 'fahrenheit':
                    conversion = cToF(userValue)
                    conversionStatement = f'{userValue}\u00B0 {userUnit} -> {conversion:.2f}\u00B0 {convertedUnit}'
                elif convertedUnit == 'kelvin':
                    conversion = cToK(userValue)
                    conversionStatement = f'{userValue}\u00B0 {userUnit} -> {conversion:.2f}\u00B0 {convertedUnit}'
            case 'kelvin':
                if convertedUnit == 'celsius':
                    conversion = kToC(userValue)
                    conversionStatement = f'{userValue}\u00B0 {userUnit} -> {conversion:.2f}\u00B0 {convertedUnit}'
                elif convertedUnit == 'kelvin':
                    conversion = fToK(userValue)
                    conversionStatement = f'{userValue}\u00B0 {userUnit} -> {conversion:.2f}\u00B0 {convertedUnit}'
            case other:
                print('That is not a proper unit for conversion')
    print(conversionStatement)
    return conversion

def cToF(tempCelsius):
    return (1.8 * tempCelsius + 32)

def fToC(tempFahrenheit):
    return ((5 / 9) * (tempFahrenheit - 32))

def fToK(tempFahrenheit):
    return (((tempFahrenheit - 32) * (5 / 9)) + 273.15)

def cToK(tempCelsius):
    return (tempCelsius + 273.15)

def kToC(tempKelvin):
    return (tempKelvin - 273.15)

def kToF(tempKelvin):
    return (((tempKelvin - 273.15) * 1.8) + 32)

def test0_func():
    assert convertTemp('fahrenheit',32,'celsius') == 0.0
def test1_func():
    assert convertTemp('celsius', 100, 'fahrenheit') == 212
def test2_func():
    assert convertTemp('fahrenheit',98.6,'celsius') == 37
def test3_func():
    assert convertTemp('celsius', -50, 'fahrenheit') == -58
def test4_func():
    assert convertTemp('celsius',-273.15,'kelvin') == 0
def test5_func():
    assert convertTemp('kelvin',294.15,'celsius') == 21
