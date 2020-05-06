# State Logs Processing (SLP)

## Setting the Environment

```
conda create -n slp python=3.7
conda activate slp
conda install -c conda-forge spacy
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
python.setInterpreter	Select Interpreter
python.setShebangInterpreter

nlp solution
https://spacy.io/

search solution
https://whoosh.readthedocs.io/en/latest/intro.html

backend solution
https://flask.palletsprojects.com/en/1.1.x/

frontend solution
https://getbootstrap.com/

graph plotting solution
https://www.chartjs.org/

## TODO:

- check the slides
- read the doc for word2vec
- check the second word2vec paper

-- create a function to return the max date and min date.
-- this function is going to be needed to plot the graph
