import os
import os.path
import sys

sys.path.append('slp')

from whoosh import index
from whoosh.analysis import StemmingAnalyzer
from whoosh.fields import DATETIME, ID, STORED, TEXT, Schema
from whoosh.qparser import QueryParser
from whoosh.query import Phrase

from document import Document
from match import Match


class Search:
    def __init__(self, index_path='default'):
        # define schema
        self.schema = Schema(
            state=ID(stored=True),
            date=DATETIME(stored=True),
            page=ID(stored=True),
            sentence=TEXT(stored=True),
            decree=ID(stored=True)
        )

        # create the self.index with index file from Whoosh
        if not os.path.exists(index_path):
            print('There was no index. Creating one')
            os.mkdir(index_path)
            self.index = index.create_in(index_path, self.schema)
        else:
            print('Loading index...')
            self.index = index.open_dir(index_path)

        self.writer = self.index.writer(procs=6, limitmb=1024)
    
    ## 
    def index_elements(self, state, page, date, sentence, decree, commit=True):
        # write document
        self.writer.add_document(
            state=state,
            page=page,
            date=date,
            sentence=sentence,
            decree=decree
        )

    def commit_indexing(self):
        self.writer.commit()
        self.writer = self.index.writer(procs=6, limitmb=1024)

    def search_term(self, term):
        # build the query
        qp = QueryParser('sentence', schema=self.schema)
        query = qp.parse(term)
        # print hits
        with self.index.searcher() as searcher:
            match_list = []
            # this limits the number of matches = 10
            results = searcher.search(query, limit=None)
            print('-- number of hits: ', len(results))
            for hit in results:
                # hit has:
                # date
                # page
                # sentennce
                # state
                match = Match(
                    hit['page'],
                    hit['state'],
                    hit['sentence'],
                    hit['date'],
                    '<link>',
                    '<id>',
                    hit['decree']
                )
                print(match)
                match_list.append(match)
            print('-- result-size: ', len(match_list))
        # return all matches
        return match_list

    def get_term_freq(self, term):
        # get the index reader
        index_reader = self.index.reader()
        # get the frequency
        # reading.frequency(<fieldname>, <text>)
        # the total of instances of the given term in the document
        return index_reader.frequency('sentence', term)

    def get_phrase_freq(self, phrase):
        #
        query = Phrase('sentence', phrase.split())
        #
        searcher = self.index.searcher()
        #
        hits = searcher.search(query, limit=None)
        #
        return float(len(hits))
