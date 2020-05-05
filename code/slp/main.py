#from match import Mach
import match
from document import Document
from pdf_processor import PDFProcessor

from io import StringIO

import pdfminer

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter, PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage, PDFTextExtractionNotAllowed
from pdfminer.pdfdevice import PDFDevice


pdfproc = PDFProcessor()
doc = pdfproc.pdf_to_document('data/test.pdf') 




## Search function
def search_term(document_list, query):
    return 0
    # for each document in the list

    # for each sentence in each document

    # if query matches the sentence

    # create a match object
    ## the object should have:
    ## document id
    ## sentence matched + sentences around for manual review
    ## page matched
    ## day matched
    ## link to the document
    ## state matched

    ## such information should come from the file structure itself



