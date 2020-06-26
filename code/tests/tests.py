import shutil
import sys

from slp.search import Search
from slp.pdf_processor import PDFProcessor 
from slp.embeddings import Embeddings

# see https://github.com/CleanCut/green#unit-test-structure-tutorial
import unittest

print('Runnint tests')

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

