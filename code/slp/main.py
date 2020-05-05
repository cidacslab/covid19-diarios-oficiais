#from match import Mach
from .document import Document
from .search import Search
from .pdf_processor import PDFProcessor

from io import StringIO


#pdfproc = PDFProcessor()
#doc = pdfproc.pdf_to_document('data/test.pdf') 

search = Search()
search.index_document('data/test.pdf')


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



