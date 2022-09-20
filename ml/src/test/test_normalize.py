import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import normalize
import pytest

"""
resources:
- https://machinelearningmastery.com/a-gentle-introduction-to-unit-testing-in-python/
"""

testingInput = "It would be unfair to demand that people cease pirating files when those same people aren't paid for their participation in very lucrative network schemes. Ordinary people are relentlessly spied on, and not compensated for information taken from them. While I'd like to see everyone eventually pay for music and the like, I'd not ask for it until there's reciprocity."
testingOutput = "it would be unfair to demand that people cease pirating files when those same people are not paid for their participation in very lucrative network schemes. ordinary people are relentlessly spied on, and not compensated for information taken from them. while i would like to see everyone eventually pay for music and the like, i would not ask for it until there is reciprocity."

@pytest.fixture
def normalTextObj():
    return normalize.NormalizeTextClass()

def test_negative_case(normalTextObj): 
    normalTextObj.setInputText(testingInput)
    assert normalTextObj.getNormalizedText() == testingOutput, "incorrect negative output"