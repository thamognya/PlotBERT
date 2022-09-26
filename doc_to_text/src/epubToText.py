import ebooklib
from ebooklib import epub

class EpubToTextClass:

    def __init__(self, dirToEpub=""):
        self.dirToEpub = dirToEpub

    def setDirToEpub(self, dirToEpub):
        self.dirToEpub = dirToEpub

    def convertEpubToText(self):
        book = epub.read_epub(self.convertEpubToText)
        items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))
        text = ""
        for i in items:
            text = text + i
        return text

e = EpubToTextClass()
e.setDirToEpub("/home/jeff/Downloads/PlotBERTBooks/How to Win Friends and Influence People in the Digital Age (Dale Carnegie and Associates) (z-lib.org).epub")
print(e.convertEpubToText())
