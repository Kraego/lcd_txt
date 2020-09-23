import pytest
from source.lcdtxt import find_common_stuff


def test_find_common_stuff_complete_same():
    reply = find_common_stuff('./testdata/scenarioSame')
    assert reply != None

    with open('./testdata/scenarioSame/fileA.txt', 'r') as f:
        expected_reply = f.read()
    assert expected_reply == reply
    

def test_find_common_stuff_complete_different():
    reply = find_common_stuff('./testdata/scenarioDifferent')
    assert reply == None
    

def test_find_common_same_parts():
    reply = find_common_stuff('./testdata/scenarioSameParts')
    assert reply == "I' am a test file with plenty lines\nNOT"
    

def test_find_common_mixed_parts():
    reply = find_common_stuff('./testdata/scenarioMixed')
    assert reply == "I' am a test file with plenty lines\nNOT"


def test_find_common_mixed_parts_one_differnt():
    reply = find_common_stuff('./testdata/scenarioMixedOneDifferent')
    assert reply == None
    
    
def test_find_common_complex():
    reply = find_common_stuff('./testdata/scenarioComplex')
    assert reply == "DasselbeZeuchs\n1234\n#*>\nWiederdasselbe\n***"
