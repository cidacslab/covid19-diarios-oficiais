from search import Search 
from document import Document
from pdf_processor import PDFProcessor

import re
import os

class Index:
    #def __init__(self):
        #print('fill me')
    
    # define the expected format
    # root
    # - state1
    # - - <date.pdf>
    # - - <date.pdf>
    # - - <date.pdf>
    # - state2
    # - - <date.pdf>
    # - - <date.pdf>
    def index_folder(self, root):
        s = Search()
        j = open('w2v.words.txt', 'a+')
        pdfp = PDFProcessor()
        # list files in root
        states = os.listdir(root)
        # TODO: filter off non folders
        # for each folder
        for state in states:
            #   grab the name of the folder
            #   list the files in folder
            files = os.listdir( root + '/' + state)
            pdf_files = [f for f in files if f[-4:] == '.pdf']
            for pdf_file in pdf_files:
                # process the pdf file
                date = pdf_file[:8]
                path = root + '/' + state + '/' + pdf_file
                print(f'indexing document <{path}>')
                # convert pdf to document
                doc = pdfp.pdf_to_document(path, state, date)
                # index document
                s.index_document(doc)
                # write every sentence to a file
                # this will be used for w2v
                for s in doc.getAllSentences():
                    # remove double white space
                    # remove edge spaces
                    # make everything lower
                    s = ' '.join(s.strip().lower().split())
                    
                    j.write(s + '\n')
                    
                    print(s)
                    
                
                
        j.close()


idx = Index()
idx.index_folder('data/root')
