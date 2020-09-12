import pytest
from drinkmaker import DrinkMaker

def test_case1():
    drinkmaker = DrinkMaker()    
    result = drinkmaker.instruction("Tea","1")    
    assert result == "T:1:0"

def test_case2():
    drinkmaker = DrinkMaker()    
    result = drinkmaker.instruction("Chocolate","")    
    assert result == "H::"

def test_case3():
    drinkmaker = DrinkMaker()    
    result = drinkmaker.instruction("Coffee","2")    
    assert result == "C:2:0"

def test_case4():
    drinkmaker = DrinkMaker()    
    result = drinkmaker.instruction("Tea","")    
    assert result == "T::"

def test_case5():
    drinkmaker = DrinkMaker()    
    result = drinkmaker.instruction("Chocolate","2")    
    assert result == "H:2:0"
