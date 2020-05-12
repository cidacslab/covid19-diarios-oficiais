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
    
    def get_top_k(self, word, k):
        # get the embedding for the word
        emb = self.get_emb(word)
        # create an object with the format n_samples:n_features
        vecs_list = list(self.emb.values())
        vecs_np = np.concatenate((vecs_list), axis=0)
        # calculate similarity with all other embeddigs
        similarities = cosine_similarity(emb, vecs_np).reshape(-1)
        ## zip similarities with words
        word_similarities = list(zip(self.emb.keys(),similarities))
        # sort similarities
        sorted_word_similarities = sorted(word_similarities, key = lambda k: k[1], reverse=True)
        # return top k
        return sorted_word_similarities[1:k+1]
   
    # TODO: generate mwu
    def get_mwu_score(self, word1, word2):
        # TODO: put the formula here
        # FORMULA:
        # score =  (count(word_a, word_b) - delta) / (count(word_a) * count(word_b))
        ##### delta is a minimum frequency that discounts infrequent pairs
        ##### pairs above some score threshold are merged

        # functions to be used
        ## whoosh.query.Phrase
        ## matches documents containing the phrase
        ## result = s.search(q, limit=None) # to get all hits
        ## len(result) # runs a fast and unscored version of the query to figure out the number of hits
        ## reading.frequency(<fieldname>, <text>) # the total of instances of the given term in the document
        
        #
        return 0

    # TODO: generate MWU:
    def generate_mwu(self, whoosh):
        # for each word1 in vocab
        ## for each word2 in vocab
        ### if word1 != word2:
        #### score = get_mwu_score
        #### if score > threshhold
        ##### generate new mwu with the average of both wb
        return 0

# these are the pt embeddings generated for scielo
obj = Embeddings('data/embeddings/pt.vec')

# TODO: transform these into tests
# comparison assertions
assert '%.3f'%obj.get_similarity('oi', 'ola') == '0.174'
assert '%.3f'%obj.get_similarity('teste', 'teste') == '1.000'
assert '%.3f'%obj.get_similarity('deus', 'jesus') == '0.593'
# checking if the function returns the embedding correctly
assert obj.get_emb('ola')[0][0] == 0.089899

## work on the k-most similar
print(obj.get_top_k('coronavirus', 10))
