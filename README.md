# State Logs Processing (SLP)
[![Build Status](https://travis-ci.com/cidacslab/covid19-diarios-oficiais.svg?token=4NPdpgkxu7MaGzxEDga4&branch=master)](https://travis-ci.com/cidacslab/covid19-diarios-oficiais)

## Goal of the project

## Project layout

## How to run

Navigate to `code` folder and inside it type:

```
sudo docker build -f Dockerfile -t "ling-539/final-project:latest" .
sudo docker run -it -p 7777:5000 "ling-539/final-project:latest" python application.py
```

The first command will build the docker image.
The second will launch a webserver using port `7777`.

Type `http://localhost:7777/` on your Web browser.
