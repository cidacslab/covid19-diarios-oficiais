from document import Document
from search import Search
#
from io import StringIO
#
from flask import Flask, render_template

app = Flask(__name__)

## todo FLASK
@app.route('/')
@app.route('/<query>')
def q(query=None):
    hits = None
    if query:
        search = Search()
        # search.index_document(doc)
        
        hits = search.search_term(query)

    return render_template('index.html', hits=hits)



# search part
