import sys
sys.path.append('slp')

from main import textToSentences

# see https://github.com/CleanCut/green#unit-test-structure-tutorial
import unittest

class TestExamples(unittest.TestCase):
    def test_equals(self):
        "Example test using equality"
        self.assertEqual(2, 2)

    '''
    def test_fail(self):
        "this test should always fail."
        "comment out"
        self.assertEqual(1,0)
    '''


''' this class is going to house NLP related tests
'''
class TestNLP(unittest.TestCase):
    def test_textToSencenes(self):
        ## testing text to sentence func
        sentences = textToSentences("Esse e um exemplo de texto. Esse e outro exemplo de texto.")
        self.assertEqual(sentences, ['Esse e um exemplo de texto.', 'Esse e outro exemplo de texto.'])


''' this class is going to house  information extraction tests
'''
class TestIE(unittest.TestCase):
    def test_fromPDFToDocument(self):
        ## testing fromPDFToDocument func
        tt = fromPDFToDocument('data/test.pdf')
        # this document has 64 pagesj
        self.assertEqual(tt.getNumPages(), 5)
        # this document has 9709 sentences
        # self.assertEqual(tt.getNumSentences() == 9709)
        print(tt.getNumSentences())

''' TODO: add a searching classs 
'''


