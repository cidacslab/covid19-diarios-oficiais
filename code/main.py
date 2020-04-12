from io import StringIO

import pdfminer

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter, PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage, PDFTextExtractionNotAllowed
from pdfminer.pdfdevice import PDFDevice

# read and write strings as files
output_string = StringIO()

with open('data/ba/01/20200107.pdf', 'rb') as in_file:
    # parse file?
    parser = PDFParser(in_file)
    
    document = PDFDocument(parser)
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
                print( element.get_text())
