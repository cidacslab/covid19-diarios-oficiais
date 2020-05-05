import sys
sys.path.append('slp')

from pdf_processor import PDFProcessor 

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


''' this class is going to house  information extraction tests
'''
class TestIE(unittest.TestCase):
    def test_fromPDFToDocument(self):
        pdfproc = PDFProcessor()
        ## testing fromPDFToDocument func
        tt = pdfproc.pdf_to_document('data/test.pdf')
        # this document has 64 pagesj
        self.assertEqual(tt.getNumPages(), 5)
        # this document has 9709 sentences
        self.assertEqual(tt.getNumSentences(), 172)

