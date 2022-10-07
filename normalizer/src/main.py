import pandas as pd
import normalize

normalizer = normalize.NormalizeTextClass()

class NormalizeDataCsv:

    def __init__(self, dataCsvLoc="", normalizedDataCsvLoc="", textList=[], nameList=[]):
        self.dataCsvLoc = dataCsvLoc
        self.normalizedDataCsvLoc = normalizedDataCsvLoc
        self.textList = textList
        self.nameList = nameList

    def setDataCsvLoc(self, dataCsvLoc):
        self.dataCsvLoc = dataCsvLoc

    def setNormalizedDataCsvLoc(self, normalizedDataCsvLoc):
        self.normalizedDataCsvLoc = normalizedDataCsvLoc

    def normalizeDataCsv(self):
        df = pd.read_csv(self.dataCsvLoc)
        textList = []
        nameList = []
        for index, row in df.iterrows():
            name = row['name']
            text = row['text']
            normalizer.setInputText(str(text))
            text = normalizer.getNormalizedText()
            nameList.append(name)
            textList.append(text)
        self.textList = textList
        self.nameList = nameList
        data = {
            'name': nameList,
            'text': textList
        }
        df = pd.DataFrame(data)
        df.to_csv(self.normalizedDataCsvLoc, mode='a', index=False, header=True)

