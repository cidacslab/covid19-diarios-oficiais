import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class Embeddings:
    def __init__(self, path):
        self.emb = dict()
        # open the path
        j = open(path, 'r')
        # read the embeddings as a dictionary word:embedding 
        for l in j:
            l = l.replace("'", '').split() 
            # check for header
            if len(l) == 2:
                print(f'Loading embeddings:\n ** Vocab Size: {l[0]}\n ** Embedding size: {l[1]}\n ** Path: {path}')
            else:
                # the word is the first column
                word = l[0]
                # embedding should be a numpy array
                emb =  np.fromstring(' '.join(l[1:]), dtype=float, sep=' ')
                ## add the word to the dictionary
                self.emb[word] = np.asarray([emb])#.reshape(-1, 1)
                ## for debuggig
                #print(f'word:<{word}>, emb:<{emb}>')
    
    # receives the word and returns the correspondent embedding
    def get_emb(self, word):
        if word in self.emb.keys():
            return self.emb[word]
        return None
    
    # func to calculate the similarity between two words
    def get_similarity(self, word1, word2):
        emb1 = self.get_emb(word1)
        emb2 = self.get_emb(word2)
        return cosine_similarity(emb1, emb2).item(0)
    
    # TODO: code get_top_k
    # it is worth noting that cosine_similarity performs a pairwise opearation
    def get_top_k(self, word):
        return None

    # TODO: generate MWU:
    def generate_mwu(self, whoosh):
        # TODO: put the formula here
        # FORMULA:
        # score =  (count(word_a, word_b) - delta) / (count(word_a) * count(word_b))
        ##### delta is a minimum frequency that discounts infrequent pairs
        ##### pairs above some score threshold are merged
        return 0

# TODO: download a portuguese embedding
obj = Embeddings('data/embeddings/model.emb')

# TODO: transform these into tests
#print(obj.get_emb('hi'))
print(obj.get_similarity('hi', 'hello')) # should be 0.415
print(obj.get_similarity('test', 'test')) # should be 1
print(obj.get_similarity('fuck', 'jesus')) # should be 0.331
