# file imports
from unicodedata import normalize
import constants
# imports
import contractions
import tokenizers
from tokenizers.normalizers import Lowercase, NFKD, StripAccents

"""
Resources:
- https://towardsdatascience.com/text-normalization-for-natural-language-processing-nlp-70a314bfa646
- https://www.ntentional.com/nlp/datasets/tokenization/processing/2020/10/09/comprehensive-datasets.html
"""

# add contradictions
for i in constants.contractionsDict:
    contractions.add(i, constants.contractionsDict[i])

class NormalizeTextClass:
    def __init__(self, inputText = ""):
        self.inputText = inputText

    def setInputText(self, inputTextIn):
        self.inputText = str(inputTextIn)

    def expandContradictions(self):
        return contractions.fix(self.inputText)

    def normalize(self):
        normalierSeq = tokenizers.normalizers.Sequence([Lowercase(), NFKD(), StripAccents()])
        return normalierSeq.normalize_str(self.expandContradictions())
        
    def getNormalizedText(self):
        return self.normalize()