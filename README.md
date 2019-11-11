# PUT BDP Blum Micali Generator

## Applications Description
### Prime Generator
This application is used to generated prime numbers (works well for number with 250 digits and below). Miller-Rabin test is used to check if number is prime.
To generate number you have to enter desired number of digits and click 'Random prime' button.

### Blum Micali Generator
This application is used to generate random numbers using Blum-Micali algorithm.
In order to generate number you have to provide application with 3 parameters for formula used in Blum-Micali algorithm (explained later)
and enter desired length of generated bit sequence. After filling parameters and clicking on 'Random numberr' button number should be generated.

## Algorithm
Blum-Micali algorithm is based on formula and decision block.

### Formula
### x<sub>i+1</sub> = g<sup>x<sub>i</sub></sup> mod p
where:
g - primitive root modulo p (g and p has 1 as only common divider)
p - large prime
x<sub>0</sub> - seed

### Decision block
x is used to make decision if next bit will be generated as 1 or 0.
If x<sub>i</sub> <= (p - 1)/2 than generate bit with value 1, otherwise generate bit with value 0.

## Enviroment
- Written using JetBrains Pycharm
- Written in Python
- Interface created with tkinter
- Exe generated with PyInstaller
