# file imports
import constants
# imports
import contractions
import string
import nltk
from transformers import pipeline

"""
Resources:
- https://towardsdatascience.com/text-normalization-for-natural-language-processing-nlp-70a314bfa646
"""

# add contradictions
for i in constants.contractionsDict:
    contractions.add(i, constants.contractionsDict[i])

class NormalizeTextClass:
    def __init__(self, inputText = ""):
        self.inputText = inputText

    def setInputText(self, inputTextIn):
        self.inputText = str(inputTextIn)

    def lowerCase(self):
        # convert all letters to lowercase
        return self.inputText.lower()

    def expandContradictions(self):
        # expand contradictions (for example ain't )
        return contractions.fix(self.lowerCase())

    def removePunctuation(self):
        # Remove punctuation from sentence
        return self.expandContradictions().translate(str.maketrans('', '', string.punctuation))

    def getNormalizedText(self):
        return self.removePunctuation()
