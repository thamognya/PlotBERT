import epubToText
import pdfToText
from os import listdir
from os.path import isfile, join
import pandas as pd

class ConvertAll:

    def __init__(self, folderPath="", filesInFolder=[], epubInFolder=[], pdfInFolder=[], csvLoc="", pdfText=[], epubText=[], text=[], name=[]):
        self.folderPath = folderPath
        self.filesInFolder = filesInFolder
        self.epubInFolder = epubInFolder
        self.pdfInFolder = pdfInFolder
        self.csvLoc = csvLoc
        self.pdfText = pdfText
        self.epubText = epubText
        self.text = text
        self.name = name

    def setFolderPath(self, folderPath):
        self.folderPath = folderPath
    
    def getAllFilesInFolder(self):
        filesinFolder = []
        for i in listdir(self.folderPath):
            if (isfile(join(self.folderPath, i))):
                filesinFolder.append(self.folderPath + i)
        self.filesInFolder = filesinFolder

    def getEpubInFolder(self):
        epubInFolder = []
        for i in self.filesInFolder:
            if (i.endswith(".epub")):
                epubInFolder.append(i)
        self.epubInFolder = epubInFolder

    def getPdfInFolder(self):
        pdfInFolder = []
        for i in self.filesInFolder:
            if (i.endswith(".pdf")):
                pdfInFolder.append(i)
        self.pdfInFolder = pdfInFolder

    def setCsvLoc(self, csvLoc):
        self.csvLoc = csvLoc
        # headerList = ['name', 'text']
        # df = pd.read_csv(self.csvLoc)
        # df.to_csv(self.csvLoc, header=headerList, index=False)

    def convertToText(self):
        self.getAllFilesInFolder()
        self.getEpubInFolder()
        self.getPdfInFolder()
        pdfText = []
        epubText = []
        text = []
        name = []
        pdf = pdfToText.PdfToTextClass()
        epub = epubToText.EpubToTextClass()
        for i in self.pdfInFolder:
            pdf.setDirToPdf(i)
            name.append(i)
            pdfData = str(pdf.convertPdfToText())
            pdfText.append(pdfData)
            text.append(pdfData)
        for i in self.epubInFolder:
            epub.setDirToEpub(i)
            name.append(i)
            epubData = str(epub.getEpub())
            epubText.append(epubData)
            text.append(epubData)
        data = {
            'name': name,
            'text': text
        }
        df = pd.DataFrame(data)
        df.to_csv(self.csvLoc, mode='a', index=False, header=True)
        self.pdfText = pdfText
        self.epubText = epubText
        self.text = text
        self.name = name

