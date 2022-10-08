import main

breaker = main.BreakTextHelper()

def main(textCsvLoc, brokenTextCsvLoc):
    breaker.setTextCsvLoc(textCsvLoc)
    breaker.setBrokenTextCsvLoc(brokenTextCsvLoc)
    breaker.writeToCsv()

main("../../data/text.csv", "../../data/brokenText.csv")


