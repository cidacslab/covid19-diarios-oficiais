import shutil
import sys

from slp.search import Search
from slp.pdf_processor import PDFProcessor 
from slp.embeddings import Embeddings

# see https://github.com/CleanCut/green#unit-test-structure-tutorial
import unittest

print('Runnint tests')

# preparing pdf proc
pdfproc = PDFProcessor()
''' this class is going to house NLP related tests
'''
class TestNLP(unittest.TestCase):
    def test_text_to_sentences(self):
        # now we need an object
        ## testing text to sentence func
        sentences = pdfproc.text_to_sentences("Esse e um exemplo de texto. Esse e outro exemplo de texto.")
        self.assertEqual(sentences, ['Esse e um exemplo de texto.', 'Esse e outro exemplo de texto.'])

# preparing pdf document
tt = pdfproc.pdf_to_document('data/test.pdf', 'ba', '2019-12-04')

''' this class is going to house  information extraction tests
'''
class TestIE(unittest.TestCase):
    def test_get_num_pages(self):
        ## testing fromPDFToDocument func
        # this document has 5
        self.assertEqual(tt.getNumPages(), 5)
    def test_get_num_sentences(self):
        # this document has 9709 sentences
        self.assertEqual(tt.getNumSentences(), 172)

# peparing search
try: 
    print('Cleaning old files')
    shutil.rmtree('idx_test')
    print('Creating index')
except:
    print('Creating index')

search = Search('idx_test')
search.index_document(tt)
''' 
'''
class TestSearch(unittest.TestCase):
    def test_search_term(self):
        # test getTermFrequency
        self.assertEqual(search.get_term_freq('grafos'), 11.0)
    def test_get_phrase_freq(self):
        # test getPhraseFrequency
        self.assertEqual(search.get_phrase_freq('problemas clássicos'), 2.0)
    
# preparing embedddings
obj = Embeddings('data/embeddings/pt.vec')
''' 
'''
class TestEmbeddings(unittest.TestCase):
    # comparison assertions
    def test_get_similarity(self):
        self.assertEqual('%.3f'%obj.get_similarity('oi', 'ola'), '0.174')
        self.assertEqual('%.3f'%obj.get_similarity('teste', 'teste'), '1.000')
        self.assertEqual('%.3f'%obj.get_similarity('deus', 'jesus'), '0.593')
    
    def test_return_correct_emb(self):
        # checking if the function returns the embedding correctly
        self.assertEqual(obj.get_emb('ola')[0][0] , 0.089899)

