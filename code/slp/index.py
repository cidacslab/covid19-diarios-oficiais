import os
import re

from document import Document
from pdf_processor import PDFProcessor
from search import Search


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
        search = Search()
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
                search.index_document(doc)
                # write every sentence to a file
                # this will be used for w2v
                for sent in doc.getAllSentences():
                    # remove double white space
                    # remove edge spaces
                    # make everything lower
                    sent = ' '.join(sent.strip().lower().split())
                    # write line to embedding file
                    j.write(sent + '\n')
        # close embedding file
        j.close()

    def index_folder_txt(self, root):
        states = os.listdir(root)
        # TODO: pdfp = PDFProcessor()
        # pdf processor should be renamed to file processor bc now it processes two different things.
        search = Search()
        for state in states:
            # TODO: list all directories
            all_files = os.listdir( root + '/' + state)
            #  
            pdf_files = [f for f in all_files if f[-4:] == '.pdf']
            # remove all extentions
            folders_txt = [root+'/'+f[:-4] for f in pdf_files]

            print(folders_txt)
            for folder in folders_txt:
                files = os.listdir(folder)
                txt_files = [f for f in files if f[-4:] == '.txt' and f.find('-') == -1]
                print(txt_files)
                # TODO: write a function to convert txt to doc
                # rename 


            #files = os.listdir( root + '/' + state)
            #print(files)
            ## 
            #txt_files = [f for f in files if f[-4:] == '.txt']
            #print(txt_files)
            #for txt in txt_files:
            #    date = pdf_file[:8]
            #    print(date)



idx = Index()
idx.index_folder_txt('/home/gcgbarbosa/repos/covid19-diarios-oficiais/toy-data/covid19')
# idx.index_folder('data/root')
# idx.index_folder('data/root')
