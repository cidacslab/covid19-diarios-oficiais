# This is an example Dockerfile that assumes
# a project with a Python 3.7 code base.

# Feel free to change as needed.
FROM python:3.7

LABEL author="George C. G. Barbosa"
LABEL description="Timeline of Decrees"

# Create app directory
WORKDIR /app

# Bundle app source
COPY . .

# Install python dependencies
RUN pip install -U pip
# Jupyter deps
RUN pip install -U jupyter==1.0.0
RUN pip install -U jupyter-contrib-nbextensions==0.5.1
RUN jupyter contrib nbextension install --user
# Test utils
RUN pip install -U green==3.1.0
# Project-specific deps
RUN pip install -r requirements.txt
# spacy model
RUN python -m spacy download pt_core_news_sm 
# install SLP itself
RUN pip insttall -e .
