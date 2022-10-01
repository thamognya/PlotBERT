from epub_conversion.utils import open_book, convert_epub_to_lines
from bs4 import BeautifulSoup

class EpubToTextClass:

    def __init__(self, dirToEpub=""):
        self.dirToEpub = dirToEpub

    def setDirToEpub(self, dirToEpub):
        self.dirToEpub = dirToEpub

    def convertEpubToHtml(self):
        book = open_book(self.dirToEpub)
        lines = convert_epub_to_lines(book)
        epub = ""
        for i in lines:
            epub += str(i)
        return epub
    
    def convertHtmlToText(self):
        html = self.convertEpubToHtml()
        soup = BeautifulSoup(html, 'html.parser')
        return soup.get_text()
    
    def getEpub(self):
        return self.convertHtmlToText()


e = EpubToTextClass()
e.setDirToEpub("/home/jeff/Downloads/PlotBERTBooks/How to Win Friends and Influence People in the Digital Age (Dale Carnegie and Associates) (z-lib.org).epub")
print(e.getEpub())
