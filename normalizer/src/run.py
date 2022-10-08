import main

normalizer = main.NormalizeDataCsv()

def main(csvLoc, normalCsvLoc):
    normalizer.setDataCsvLoc(csvLoc)
    normalizer.setNormalizedDataCsvLoc(normalCsvLoc)
    normalizer.normalizeDataCsv()

main("../../data/brokenText.csv", "../../data/normalizedText.csv")
