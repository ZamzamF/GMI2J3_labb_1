#This file contains code pertaining to converting to and from Roman numerals.


#pythons framework for unit testing
import unittest

#First iteration - FAIL (TDD - Red)
"""
def to_roman(n):
    '''convert integer to Roman numeral'''
    pass                                   
"""

#Second iteration - Pass (TDD - Green)
roman_numeral_map = (
    ('M',  1000),
    ('CM', 900),
    ('D',  500),
    ('CD', 400),
    ('C',  100),
    ('XC', 90),
    ('L',  50),
    ('XL', 40),
    ('X',  10),
    ('IX', 9),
    ('V',  5),
    ('IV', 4),
    ('I',  1)
)                 
def to_roman(n):
    '''convert integer to Roman numeral'''
    result = ''
    for numeral, integer in roman_numeral_map:
        while n >= integer:                     
            result += numeral
            n -= integer
    return result


#





if __name__ == '__main__':
    unittest.main()
