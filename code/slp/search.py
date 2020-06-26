import os
import os.path

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

        self.writer = self.index.writer(procs=6, limitmb=2048)
    #
    def index_document(self, doc):
        # write document
        for k, s in enumerate(doc.pages):
            self.writer.add_document(
                state=doc.state,
                page=str(k+1),
                date=doc.date,
                sentence=' '.join(s)
            )
            print('indexed: (state->', doc.state, '), (page->',
                  k+1, '), (date->', doc.date, ')')
            #print('sentence: ', s)
        self.writer.commit()

    #
    def index_elements(self, state, page, date, sentence, decree, commit=True):
        # write document
        self.writer.add_document(
            state=state,
            page=page,
            date=date,
            sentence=sentence,
            decree=decree
        )
        #print('sentence: ', s)
        if commit:
            self.writer.commit()
            w = self.index.writer(procs=6, limitmb=2048)
            # reset cachesize
            stem_ann = w.schema['content'].format.analyzer
            stem_ann.cachesize = -1
            stem_ann.clear()
            self.writer = w

    def search_term(self, term):
        # build the query
        qp = QueryParser('sentence', schema=self.schema)
        query = qp.parse(term)
        # print hits
        with self.index.searcher() as searcher:
            match_list = []
            # this limits the number of matches = 10
            results = searcher.search(query)
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
                    '<id>'
                )
                print(match)
                match_list.append(match)
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
