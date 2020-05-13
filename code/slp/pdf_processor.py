from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter, PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage, PDFTextExtractionNotAllowed
from pdfminer.pdfdevice import PDFDevice

from document import Document

class PDFProcessor:
    #def __init__(self):
    
    def text_to_sentences(self, text):
        import spacy
        # loading the portugese model
        nlp = spacy.load("pt_core_news_sm")
        # parsej
        doc = nlp(text)
        # return sentences
        return [str(sent) for sent in list(doc.sents) if len(sent) > 5]
        

    def pdf_to_document(self, path, state, date):
        with open(path, 'rb') as in_file:
            # parse file
            parser = PDFParser(in_file)
            # initialize the document object
            document = PDFDocument(parser)
            # check if the document is extractable, otherwise error
            if not document.is_extractable:
                raise PDFTextExtractionNotAllowed
            # create a PDF resource manager object that stores shared resources
            rsrcmgr = PDFResourceManager()
            # set parameters for analysis
            laparams = LAParams()
            # create a pdf device object
            device = PDFPageAggregator(rsrcmgr, laparams=laparams)
            # create a pdf interpreter object
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            # declare the document
            document_obj = Document(state, date)
            # process each page contained in the document
            n_pages = 1
            for page in PDFPage.create_pages(document):
                print('processing page ', n_pages)
                n_pages = n_pages + 1
                # process the page
                interpreter.process_page(page)
                # get the entire text of the page?
                # get the text of an entire page.
                layout = device.get_result()
                #
                page_text = ''
                for element in layout:
                    # we don't want some elements
                    if not type(element).__name__ in ['LTFigure', 'LTRect', 'LTLine', 'LTCurve']:
                        # save the text of the page
                        page_text = page_text + ' ' + element.get_text().replace('\n', '')
                        
                # convert the text of the page to a sentence list 
                sentences = self.text_to_sentences(page_text)
                # add sentences to the page
                document_obj.addPage(sentences)
            
            # returning the document obj
            return document_obj

