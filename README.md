# camilaebf.github.io
Portfolio made with Pelican for Campus Party Workshop 2021 - Argentina


# Download the image or build

`docker pull camilaebf/pelican-dev-env:latest`

or create a Dockerfile

`
FROM python:3.9.6-alpine

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
RUN apk add git

EXPOSE 8000
`

and a file `requirements.txt` : 
`
pelican
typogrify
markdown
ghp-import
`
 on the same directory than the `Dockerfile`.


