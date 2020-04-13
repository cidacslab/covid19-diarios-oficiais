from io import StringIO

import pdfminer

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter, PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage, PDFTextExtractionNotAllowed
from pdfminer.pdfdevice import PDFDevice



class Document:
    def __init__(self, doc_id):
        self.pages = 0
        # using an empty dict to store the sentences
        self.sentences = dict()
        self.doc_id = doc_id
    
    def addPage(self, sentences, page=None):
        # TODO: implement this function
        return 0
    

    def getAllSenteces(self):
        return self.sentences


def textToSentences(text):
    import spacy
    # loading the portugese model
    nlp = spacy.load("pt_core_news_sm")
    # parsej
    doc = nlp(text)
    # return sentences
    return [str(sent) for sent in list(doc.sents)]
    #return list(doc.sents)

sentences = textToSentences("Esse e um exemplo de texto. Esse e outro exemplo de texto.")
assert(sentences == ['Esse e um exemplo de texto.', 'Esse e outro exemplo de texto.'])


def fromPDFToDocument(path):
    with open(path, 'rb') as in_file:
        # parse file
        parser = PDFParser(in_file)
        # initialize the document object
        document = PDFDocument(parser)
        # check if the document is extractable, otherwise error
        if not document.is_extractable:
            raise PDFTextExtractionNotAllowed
        # create a PDF resource manager object that stores shared resources
        rsrcmgr = PDFResourceManager()
        # set parameters for analysis
        laparams = LAParams()
        # create a pdf device object
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        # create a pdf interpreter object
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        # declare the document
        document_obj = Document('fakeid')
        # process each page contained in the document
        for page in PDFPage.create_pages(document):
            # process the page
            interpreter.process_page(page)
            # get the entire text of the page?
            # get the text of an entire page.
            layout = device.get_result()
            #
            page_text = ''
            for element in layout:
                # we don't want some elements
                if not type(element).__name__ in ['LTFigure', 'LTRect', 'LTLine', 'LTCurve']:
                    # save the text of the page
                    page_text = page_text + ' ' + element.get_text().replace('\n', '')
                    
            # convert the text of the page to a sentence list 
            sentences = textToSentences(page_text)
            # TODO: document_obj.addPage(sentences) 
            print(sentences)


fromPDFToDocument('data/ba/01/20200107.pdf')
# TODO: add the assertion
