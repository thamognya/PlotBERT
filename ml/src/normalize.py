# file imports
from unicodedata import normalize
import constants
# imports
import string
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

    def removePunctuation(self):
        # Remove punctuation from sentence
        return self.normalize().translate(str.maketrans('', '', string.punctuation))
        
    def getNormalizedText(self):
        return self.removePunctuation()


"""
normalier = NormalizeTextClass()
testingInput = "It would be unfair to demand that people cease pirating files when those same people aren't paid for their participation in very lucrative network schemes. Ordinary people are relentlessly spied on, and not compensated for information taken from them. While I'd like to see everyone eventually pay for music and the like, I'd not ask for it until there's reciprocity."
normalier.setInputText(testingInput)
print(normalier.getNormalizedText())
"""