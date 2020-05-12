import shutil
import sys
sys.path.append('slp')


from pdf_processor import PDFProcessor 
from search import Search

# see https://github.com/CleanCut/green#unit-test-structure-tutorial
import unittest

print('Runnint tests')

''' this class is going to house NLP related tests
'''
class TestNLP(unittest.TestCase):
    def test_textToSencenes(self):
        # now we need an object
        pdfproc = PDFProcessor()
        ## testing text to sentence func
        sentences = pdfproc.text_to_sentences("Esse e um exemplo de texto. Esse e outro exemplo de texto.")
        self.assertEqual(sentences, ['Esse e um exemplo de texto.', 'Esse e outro exemplo de texto.'])


# preparing pdf processor
pdfproc = PDFProcessor()
tt = pdfproc.pdf_to_document('data/test.pdf', 'ba', '2019-12-04')

''' this class is going to house  information extraction tests
'''
class TestIE(unittest.TestCase):
    def test_fromPDFToDocument(self):
        ## testing fromPDFToDocument func
        # this document has 64 pagesj
        self.assertEqual(tt.getNumPages(), 5)
        # this document has 9709 sentences
        self.assertEqual(tt.getNumSentences(), 172)

# peparing search
index_path = 'test_index'
search = Search('test_index')
search.index_document(tt)
''' 
'''
class TestSearch(unittest.TestCase):
    def test_earch_term(self):
        # test getTermFrequency
        assert search.get_term_freq('grafos') == 11.0
        # test getPhraseFrequency
        assert search.get_phrase_freq('problemas clássicos') == 2.0

# clear the index after creating it
shutil.rmtree(index_path)
