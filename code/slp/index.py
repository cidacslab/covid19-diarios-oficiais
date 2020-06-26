import os
import re
import datetime

from document import Document
from pdf_processor import PDFProcessor
from search import Search

class Index:
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

    # define the expected format
    # root
    # - state1
    # - - <date.pdf>
    # - - <date.pdf>
    # - - <date.pdf>
    # - state2
    # - - <date.pdf>
    # - - <date.pdf>
    def index_folder_txt(self, root):
        # list the first level
        states = os.listdir(root)
        # declare search object to index stuff
        # TODO search should be renamed to search_engine or something
        search = Search()
        for state in states:
            all_files = os.listdir(root + '/' + state)
            #
            pdf_files = [f for f in all_files if f[-4:] == '.pdf']
            # remove all extentions
            folders_txt = [root+'/'+state+'/'+f[:-4] for f in pdf_files]
            # print(folders_txt)
            for folder in folders_txt:
                # TODO: proccess the files in order to keep the decree from the previous page
                # date formate YYYY-MM-DD
                date = folder[-10:]
                date_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
                files = os.listdir(folder)
                txt_files = [f for f in files if f[-4:] == '.txt']
                last_decree = ''
                for txt in txt_files:
                    no_extension = txt[:-4]
                    # ignore the complete file
                    if len(no_extension.split('-')) <= 3:
                        continue
                    page = no_extension.split('-')[-1]
                    txt_file = open(folder+'/'+txt)
                    #
                    for line in txt_file:
                        # skip small lines
                        if len(line.split(' ')) <= 5:
                            continue
                        decree = self.detect_decree(line)
                        if decree:
                            last_decree = decree
                        # controll commits
                        search.index_elements(
                            state, page, date_obj, line, last_decree)
                        print(
                            f"state={state}, page={page}, date={date}, last_decree={last_decree}, sentence=<{line}>")

                    txt_file.close()
        # commit indexing
        print('commiting changes...')
        search.commit_indexing()

idx = Index()
idx.index_folder_txt(
    '/home/gcgbarbosa/repos/covid19-diarios-oficiais/toy-data/covid19')
# idx.index_folder('data/root')
