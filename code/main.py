from io import StringIO

import pdfminer

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument

# read and write strings as files
output_string = StringIO()

with open('data/ba/01/20200107.pdf', 'rb') as in_file:
    # parse file?
    parser = PDFParser(in_file)
    # get the pdf doc 
    doc = PDFDocument(parser)
    # 
    rsrcmr = PDFResourceManager()
    # TODO: follow this https://pdfminersix.readthedocs.io/en/latest/tutorials/composable.html
