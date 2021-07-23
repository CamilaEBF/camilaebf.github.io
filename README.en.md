# camilaebf.github.io
# Contents

- [camilaebf.github.io](#camilaebfgithubio)
- [Contents](#contents)
- [About](#about)
- [GitHub Pages](#github-pages)
- [Pelican](#pelican)
- [Dockerize your development environment](#dockerize-your-development-environment)
  - [Download the image or build it](#download-the-image-or-build-it)
- [Generate the site with Pelican](#generate-the-site-with-pelican)
  - [Add default content](#add-default-content)
  - [Run the site](#run-the-site)
  - [Access to the site](#access-to-the-site)
- [Configure Flex theme](#configure-flex-theme)

# About

This proyect is a simple portfolio made with [Pelican](http://getpelican.com/) for the [Campus Party Workshops 2021](https://argentina.campus-party.org/contenido/workshops/).

Previusly developed by [LinuxChix](https://gitbook.linuxchixar.org/linuxchix-pelican/). Refactored by [Jucha](https://github.com/juchita) and [camilaebf](https://github.com/camilaebf).

> In collaboration with [SysArmy](https://sysar.my/) & [Nerdearla](https://nerdear.la/).


# GitHub Pages

[More about git](http://rogerdudler.github.io/git-guide/index.html). [[es](https://rogerdudler.github.io/git-guide/index.es.html)]


Source code for this site is available on [branch /src](https://github.com/CamilaEBF/camilaebf.github.io/tree/src), as GHP suggests on [this page](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site#creating-a-repository-for-your-site).


---
# Pelican

[What is Pelican?](https://docs.getpelican.com/en/latest/#why-the-name-pelican)

# Dockerize your development environment
## Download the image or build it

    `docker pull camilaebf/pelican-dev-env:latest`

or *create a Dockerfile*

```
FROM python:3.9.6-alpine

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
RUN apk add git

EXPOSE 8000
```

and a file `requirements.txt` : 
```
pelican
typogrify
markdown
ghp-import
```
on the same directory than the `Dockerfile`.

Build it running:

    `docker build -t pelicandevenv .`

 > Do not forget to add '.' at the end of the command to refernce the file on the current directory.

 > This image includes all dependencies for the Pelican site.
 
Run it and access to the console:

    `docker run -it --name pelicandevenv --rm --volume ${PWD}:/usr/src/app -p 8080:8000 pelicandevenv:latest sh`


---
# Generate the site with Pelican

From the root of the project, that was already set up in the image, run:

    `pelican-quickstart`

It will ask you for a few things:

    > Where do you want to create your new web site? [.]
    > What will be the title of this web site? CamilaEBF
    > Who will be the author of this web site? CamilaEBF
    > What will be the default language of this web site? [en] es
    > Do you want to specify a URL prefix? e.g., https://example.com   (Y/n) https://camilaebf.github.io
    > Do you want to enable article pagination? (Y/n) Y
    > How many articles per page do you want? [10] Y
    > What is your time zone? [Europe/Paris] America/Buenos_Aires
    > Do you want to generate a tasks.py/Makefile to automate generation and publishing? (Y/n) *Y*
    > Do you want to upload your website using FTP? (y/N) N
    > Do you want to upload your website using SSH? (y/N)  N
    > Do you want to upload your website using Dropbox? (y/N) N
    > Do you want to upload your website using S3? (y/N) N
    > Do you want to upload your website using Rackspace Cloud Files? (y/N) N
    > Do you want to upload your website using GitHub Pages? (y/N) Y
    Done. Your new project is available at /usr/src/app 

## Add default content

    `/usr/src/app # pelican content`

## Run the site

    `/usr/src/app # pelican --listen -b 0.0.0.0`

 ## Access to the site

    On your browser, go to `http://localhost:8080`


# Configure Flex theme

[Flex](https://github.com/alexandrevicenzi/Flex/wiki) describes itself as *the minimalist Pelican theme*.





Like it? [Star it](https://github.com/CamilaEBF/camilaebf.github.io/stargazers)



