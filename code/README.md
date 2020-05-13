# State Logs Processing (SLP)

## Setting a conda  Environment

```
conda create -n slp python=3.7
conda activate slp
conda install -c conda-forge spacy scikit-learn whoosh flask
pip install pdfminer

# installing the portuguese spacy model

pip apt_core_news_sm
python -m spacy download pt_core_news_sm
```

## How to test

Right now everything is being developed at `code/main.py`.

To run it simply do:

```
python code/main.py
```

You should see stdout with sentences being extracted from a pdf document

## Solutions

pdf solution:
https://github.com/pdfminer/pdfminer.six

nlp solution
https://spacy.io/

search solution
https://whoosh.readthedocs.io/en/latest/intro.html

backend solution
https://flask.palletsprojects.com/en/1.1.x/

frontend solution
https://getbootstrap.com/

graph plotting solution
http://d3js.org

