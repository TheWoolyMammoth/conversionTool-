'''
unitConversion.py
Unit Converter (temp, currency, volume, mass and more) - Converts various units between one another.
The user enters the type of unit being entered, the type of unit they want to convert to and then the value.
The program will then make the conversion.
Command prompt - Tool accesible.

match-case statement <- https://learnpython.com/blog/python-match-case-statement/
main <- https://realpython.com/python-main-function/#a-basic-python-main
pytest <- https://docs.pytest.org/en/7.2.x/getting-started.html
using WSL <- https://janelbrandon.medium.com/a-guide-for-using-wsl-for-development-d135670313a6
https://www.cuemath.com/measurement/imperial-system/
https://www.cuemath.com/measurement/metric-system/
'''
import convertTemp, convertCurrency, convertDistance, convertMass, convertTime, convertVolume

def main():
    # what if i want to convert multiple things? loop that shit
    whatToConvert = input('''What are we converting today?
1. Temp
2. Distance
3. Mass
4. Volume
5. Time (Convert Military to Normal) 
6. Currency
Choice: ''')
    match whatToConvert:
        case '1':
            # Temperature
            unit = input('What temperature unit are we converting from?').lower()
            value = float(input('What is the temperature we are converting? '))
            convert = input(f'What are we converting {value} {unit} to? ').lower()
            convertTemp.convertTemp(unit,value,convert) # this returns a string
        case '2':
            # Distance
            unit = input('What distance unit are we converting from?').lower()
            value = float(input('What is the distance we are converting? '))
            convert = input(f'What are we converting {value} {unit} to? ').lower()
            convertDistance.convertDistance(unit,value,convert)
        case '3':
            # Mass
            unit = input('What mass unit are we converting from?').lower()
            value = float(input('What is the mass we are converting? '))
            convert = input(f'What are we converting {value} {unit} to? ').lower()
            convertMass.convertMass(unit,value,convert)
        case '4':
            # Volume
            unit = input('What volume unit are we converting from?').lower()
            value = float(input('What is the volume we are converting? '))
            convert = input(f'What are we converting {value} {unit} to? ').lower()
            convertVolume.convertVolume(unit,value,convert)
        case '5':
            # Time
            unit = input('What are we converting from (military or normal)? ').lower()
            if unit == 'normal':
                value = input('What is the time we are converting (ex. 12:30 pm)? ')
            else:
                value = input('What is the time we are converting? ')
            convertTime.convertTime(unit,value)
        case '6':
            # Currency
            unit = input('What currency are we converting from? (USD, Euro, CAD, etc)').lower()
            value = float(input('What is the amount of currency we are converting? '))
            convert = input(f'What are we converting {value} {unit} to? ').lower()
            convertCurrency.convertCurrency(unit,value,convert)
        case other:
            exit()

if __name__ == "__main__":
    main()