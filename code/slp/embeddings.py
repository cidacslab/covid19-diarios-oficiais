import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from .search import Search


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
        if emb is None:
            return None
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
   
    def get_mwu_score(self, word1, word2, search_obj):
        # if the word is the same, no need
        if word1 == word2:
            return 0
        # calculate count(word_a, word_b)
        count_word1and2 = search_obj.get_phrase_freq(' '.join([word1, word2]))
        # if there is no ocurrence of these words together, ignore
        if  count_word1and2 == 0:
            return 0
        
        # here we avoind having 0 in the denominator
        # calculate count(word1)
        count_word1 = search_obj.get_term_freq(word1) 
        if count_word1 == 0:
            return 0
        # calculate count(word2)
        count_word2 = search_obj.get_term_freq(word2) 
        if count_word2 == 0:
            return 0
        # calculate the score
        return count_word1and2/(count_word1*count_word2)

    def generate_mwu(self, search_obj):
        all_words = list(self.emb.keys())
        # filter out words that are not in the dataset
        # this takes a long time to run
        #filtered_words = list(filter(lambda f: search_obj.get_term_freq(f) > 0, all_words))
        # trying to speed things up with list comprehension
        filtered_words = [w for w in all_words if search_obj.get_term_freq(w) > 0]
        print(f'generating MWU\n ** filtered vocab size:<{len(filtered_words)}>') 
        
        # for each word1 in vocab
        for word1 in filtered_words:
            ## for each word2 in vocab
            for word2 in filtered_words:
                score = self.get_mwu_score(word1, word2, search_obj)
                if score > 0:
                    print(f'testind word:<{word1}> and word<{word2}>, the score is:<{score}>')
                    # T0D0: add mwu's > threshold to the self.emb

# these are the pt embeddings generated for scielo
#obj = Embeddings('data/embeddings/pt.vec')

## work on the k-most similar
# print(obj.get_top_k('coronavirus', 10))

#
#search = Search()
#obj.generate_mwu(search)
