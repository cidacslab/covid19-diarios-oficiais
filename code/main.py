from io import StringIO

import pdfminer

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter, PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage, PDFTextExtractionNotAllowed
from pdfminer.pdfdevice import PDFDevice



def fromPDFToText(path):
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
        # process each page contained in the document
        for page in PDFPage.create_pages(document):
            # process the page
            interpreter.process_page(page)
            # get the entire text of the page?
            # get the text of an entire page.
            layout = device.get_result()
            #
            for element in layout:
                # we don't want some elements
                if not type(element).__name__ in ['LTFigure', 'LTRect', 'LTLine', 'LTCurve']:
                    # print the elements of interest
                    print( element.get_text())



fromPDFToText('data/ba/01/20200107.pdf')
