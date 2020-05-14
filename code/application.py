from slp.document import Document
from slp.search import Search
from slp.embeddings import Embeddings
#
from io import StringIO
#
from flask import Flask, render_template

import datetime


app = Flask(__name__)
embeddings = Embeddings('data/embeddings/pt.vec')
search = Search()

## todo FLASK
@app.route('/')
@app.route('/<query>')
def q(query=None):
    suggestions = None
    hits = None
    base = datetime.datetime.today()
    num_days = 130
    hits_per_date = {(base - datetime.timedelta(days=x)).strftime('%Y-%m-%d'):0 for x in range(num_days)}
     
    if query:
        suggestions = embeddings.get_top_k(query, 5)
        # search.index_document(doc)
        
        hits = search.search_term(query)
        for hit in hits:
            hit.date = hit.date[:4] + '-' + hit.date[4:6] + '-' + hit.date[6:]

        # generate graph
        # group by date
        # print num hits
        all_dates = [h.date for h in hits]
        for date in all_dates:
            if date not in hits_per_date:
                hits_per_date[date] = 0
            hits_per_date[date] = hits_per_date[date] + 1


    return render_template('index.html', hits=hits, query=query, graph=hits_per_date, suggestions=suggestions)


app.run(host='0.0.0.0')
