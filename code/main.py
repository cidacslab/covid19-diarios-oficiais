from io import StringIO

import pdfminer

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

# read and write strings as files
output_string = StringIO()

with open('data/ba/01/20200107.pdf', 'rb') as in_file:
    # parse file?
    parser = PDFParser(in_file)
    # get the pdf doc 
    doc = PDFDocument(parser)
    # 
    rsrcmgr = PDFResourceManager()
    # TODO: follow this https://pdfminersix.readthedocs.io/en/latest/tutorials/composable.html
    device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
    #
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.create_pages(doc):
        interpreter.process_page(page)

    print(output_string.getvalue())
