import os
import re

from document import Document
from pdf_processor import PDFProcessor
from search import Search

class Index:
    # def __init__(self):
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
            files = os.listdir(root + '/' + state)
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

    def detect_decree(self, sentence):
        sentence = sentence.replace('\n', '').lower()
        # keywords we are looking for
        keywords = ['portaria nº', 'sei nº', 'decreto nº']
        # 
        for word in keywords:
            # if found the keyword
            if word in sentence:
                sentence_words = sentence.split(' ')
                for i, s_word in enumerate(sentence_words):
                    if i+2 < len(sentence_words) and word.split(' ')[0] == sentence_words[i]:
                        if sentence_words[i+1].lower() == 'nº':
                            if sentence_words[i+2]:
                                decree = ' '.join(sentence_words[i: i+3])
                                if decree[-1] in [',', '.']:
                                    return decree[:-1]
                                return decree
    def index_folder_txt(self, root):
        states = os.listdir(root)
        # TODO: pdfp = PDFProcessor()
        # pdf processor should be renamed to file processor bc now it processes two different things.
        search = Search()
        for state in states:
            # TODO: list all directories
            all_files = os.listdir(root + '/' + state)
            #
            pdf_files = [f for f in all_files if f[-4:] == '.pdf']
            # remove all extentions
            folders_txt = [root+'/'+state+'/'+f[:-4] for f in pdf_files]
            #print(folders_txt)
            cached_files = 0
            for folder in folders_txt:
                # date formate YYYY-MM-DD
                date = folder[-10:]
                files = os.listdir(folder)
                txt_files = [f for f in files if f[-4:] == '.txt']
                for txt in txt_files:
                    no_extension = txt[:-4]
                    # ignore the complete file
                    if len(no_extension.split('-')) <= 3:
                        continue
                    page = no_extension.split('-')[-1]
                    txt_file = open(folder+'/'+txt)
                    #
                    last_decree = ''
                    #
                    for line in txt_file:
                        commit = False
                        decree = self.detect_decree(line)
                        if decree:
                            last_decree = decree
                        # index stuff
                        print(f"processing state: <{state}>, date:<{date}>, page: <{page}>")
                        cached_files = cached_files + 1
                        # controll commits
                        if(cached_files > 1000000):
                            commit = True
                            cached_files = 0
                        search.index_elements(state, page, date, line, last_decree, commit)
                    
                    txt_file.close()

idx = Index()
idx.index_folder_txt(
    '/home/gcgbarbosa/repos/covid19-diarios-oficiais/toy-data/covid19')
# idx.index_folder('data/root')
