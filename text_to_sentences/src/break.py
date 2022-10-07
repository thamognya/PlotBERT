import pandas as pd

class BreakTextToSentence:

    def __init__(self, normalizedCsvLoc="", brokenSentenceCsvLoc=""):
        self.normalizedCsvLoc = normalizedCsvLoc
        self.brokenSentenceCsvLoc = brokenSentenceCsvLoc

    def setNormalizedCsvLoc(self, normalizedCsvLoc):
        self.normalizedCsvLoc = normalizedCsvLoc

    def setBrokenSentenceCsvLoc(self, brokenSentenceCsvLoc):
        self.brokenSentenceCsvLoc = brokenSentenceCsvLoc

    def breakTextToSentence(self):
        df = pd.read_csv(self.normalizedCsvLoc)
        textList = []
        nameList = []
        for index, row in df.iterrows():
            name = row['name']
            text = row['text']
        self.textList = textList
        self.nameList = nameList
        data = {
            'name': nameList,
            'text': textList
        }
        df = pd.DataFrame(data)
        df.to_csv(self.normalizedDataCsvLoc, mode='a', index=False, header=True)
