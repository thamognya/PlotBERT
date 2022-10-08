import pandas as pd
import nltk
from nltk import tokenize

nltk.download('punkt')

class BreakTextToSentence:

    def __init__(self, textCsvLoc="", brokenSentenceCsvLoc=""):
        self.textCsvLoc = textCsvLoc
        self.brokenSentenceCsvLoc = brokenSentenceCsvLoc

    def setTextCsvLoc(self, textCsvLoc):
        self.textCsvLoc = textCsvLoc

    def setBrokenSentenceCsvLoc(self, brokenSentenceCsvLoc):
        self.brokenSentenceCsvLoc = brokenSentenceCsvLoc

    def breakTextToSentence(self):
        df = pd.read_csv(self.textCsvLoc)
        textList = []
        nameList = []
        for index, row in df.iterrows():
            name = row['name']
            text = row['text']
            tmp = tokenize.sent_tokenize(text)
            for i in tmp:
                nameList.append(name)
            textList.extend(tmp)
        self.textList = textList
        self.nameList = nameList
        data = {
            'name': nameList,
            'text': textList
        }
        df = pd.DataFrame(data)
        df.to_csv(self.brokenSentenceCsvLoc, mode='a', index=False, header=True)
