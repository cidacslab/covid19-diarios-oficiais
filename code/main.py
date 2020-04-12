from io import StringIO

import pdfminer

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
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
    # create a pdf device object
    device = PDFDevice(rsrcmgr)
    # create a pdf interpreter object
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # process each page contained in the document
    for page in PDFPage.create_pages(document):
        # process the page
        interpreter.process_page(page)
        # get the entire text of the page?
        

