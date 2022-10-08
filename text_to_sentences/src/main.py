import breakText

breakSentence = breakText.BreakTextToSentence()

class BreakTextHelper:

    def __init__(self, textCsvLoc="", brokenTextCsvLoc=""):
        self.textCsvLoc = textCsvLoc
        self.brokenTextCsvLoc = brokenTextCsvLoc
    
    def setTextCsvLoc(self, textCsvLoc):
        self.textCsvLoc = textCsvLoc

    def setBrokenTextCsvLoc(self, brokenTextCsvLoc):
        self.brokenTextCsvLoc = brokenTextCsvLoc
    
    def writeToCsv(self):
        breakSentence.setTextCsvLoc(self.textCsvLoc)
        breakSentence.setBrokenSentenceCsvLoc(self.brokenTextCsvLoc)
        breakSentence.breakTextToSentence()

