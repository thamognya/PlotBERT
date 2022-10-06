import main

conv = main.ConvertAll()
def main(folderPath, csvLoc):
    conv.setFolderPath(folderPath)
    conv.setCsvLoc(csvLoc)
    conv.convertToText()

main("/home/jeff/Downloads/QuantumPlotBertBooks/", "/home/jeff/Documents/gitRepos/QuantumPlotBert/data/text.csv")
