

class Document:
    def __init__(self, doc_id):
        self.pages = 0
        # using an empty dict to store the sentences
        self.doc_id = doc_id
        self.pages = []
    
    def addPage(self, sentences):
        self.pages.append(sentences)
        return 0

    ## TODO: instead of a list this should return an iterator in the future
    def getPage(self, page_number):
        # -1 here because the data structure is zero indexed and we want to mantain coherence
        return self.pages[page_number - 1]

    def getNumPages(self):
        return len(self.pages)

    def getAllSentences(self):
        sentences = []
        for page in self.pages:
            for sentence in page:
                sentences.append(sentence)
        return sentences

    def getNumSentences(self):
        # TODO: do a proper job here
        return len(self.getAllSentences())


