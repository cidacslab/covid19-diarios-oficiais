#from match import Mach
from document import Document
from search import Search
from pdf_processor import PDFProcessor

from io import StringIO

search = Search()
#search.index_document(doc)

# search part
search.search_term('sempre')
