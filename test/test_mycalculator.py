#from test_mycalculator import calculator_execute
import os 
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
grandparentdir = os.path.dirname(parentdir)
sys.path.append(parentdir)
sys.path.append(grandparentdir)
from src.calculator_function import calculator_execute

def test_mycalculator():
    
    assert (1/2)*(3+(3/4))==calculator_execute('1/2 * 3&3/4')
    assert ((2+(3/8))+(9/8))==calculator_execute('2&3/8 + 9/8')
    assert ((1+(3/4)) - 2)==calculator_execute('1&3/4 - 2')
    assert 2==calculator_execute('11 % 3')





