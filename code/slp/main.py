#from match import Mach
from document import Document
from search import Search
from pdf_processor import PDFProcessor

from io import StringIO

# convert pdf to doc
#pdfproc = PDFProcessor()
#doc = pdfproc.pdf_to_document('data/test.pdf', 'ba', '2019-12-04')

# indexing part [WORKING]
search = Search()
#search.index_document(doc)

# search part
#search.search_term('sempre')

# test getTermFrequency
assert search.get_term_freq('grafos') == 11.0
# test getPhraseFrequency
assert search.get_phrase_freq('problemas clássicos') == 2.0

