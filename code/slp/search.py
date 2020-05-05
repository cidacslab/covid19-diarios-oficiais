from .document import Document
from whoosh.fields import Schema, TEXT, ID, STORED, DATETIME
from whoosh.analysis import StemmingAnalyzer

class Search:
    def __init__(self, index='default'):
        # set index
        self.index = index
        # define schema
        self.schema = Schema(
                state=ID(stored=True),
                date=DATETIME(),
                page=STORED(), # we don't wanna searchfor page, only for doc
                sentence=TEXT()
            )
    
    def index_document(self, doc):
        print(doc)

