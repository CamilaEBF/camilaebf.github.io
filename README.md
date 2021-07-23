# camilaebf.github.io
# Contenidos

- [camilaebf.github.io](#camilaebfgithubio)
- [Contenidos](#contenidos)
- [Conocé más sobre el proyecto](#conocé-más-sobre-el-proyecto)
- [GitHub Pages](#github-pages)
- [Pelican](#pelican)
- [Dockerizá tu entorno de desarrollo](#dockerizá-tu-entorno-de-desarrollo)
  - [Descarga la imagen o generala](#descarga-la-imagen-o-generala)
    - [Ejectur el contenedor y acceder a la consola](#ejectur-el-contenedor-y-acceder-a-la-consola)
    - [Crea tu propia imagen de docker](#crea-tu-propia-imagen-de-docker)
- [Clonar el repositorio](#clonar-el-repositorio)
- [Rama src](#rama-src)
- [Crea el sitio con Pelican](#crea-el-sitio-con-pelican)
  - [Contenido por defecto](#contenido-por-defecto)
  - [Ejecutá el sitio](#ejecutá-el-sitio)
  - [Accede](#accede)
- [Configura el tema Flex](#configura-el-tema-flex)

# Conocé más sobre el proyecto

Trata del desarrollo portfolio sencillo creado con [Pelican](http://getpelican.com/) para presentarlo en un [Workshop del Campus Party 2021](https://argentina.campus-party.org/contenido/workshops/).

Originalmente dado por [LinuxChix](https://gitbook.linuxchixar.org/linuxchix-pelican/) y editado por [Jucha](https://github.com/juchita) y [camilaebf](https://github.com/camilaebf).

> En colaboración a la comunidad Argentina de [SysArmy](https://sysar.my/) & [Nerdearla](https://nerdear.la/).


---
# GitHub Pages


Source code for this site is available on [branch /src](https://github.com/CamilaEBF/camilaebf.github.io/tree/src), as GHP suggests on [this page](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site#creating-a-repository-for-your-site).


---
# Pelican

[¿Qué es Pelican?](https://docs.getpelican.com/en/latest/#why-the-name-pelican)

# Dockerizá tu entorno de desarrollo
## Descarga la imagen o generala

Para descargar la imagen ejecuta en tu `terminal`:

    `docker pull camilaebf/pelican-dev-env:latest`

### Ejectur el contenedor y acceder a la consola

    `docker run -it --name pelicandevenv --rm --volume ${PWD}:/usr/src/app -p 8080:8000 camilaebf/pelican-dev-env:latest sh`

Este comando automáticamente descarga la imagen `camilaebf/pelican-dev-env:latest`
    
 > Esta imagen incluye las dependencias necesarias para tener andando tu sitio con Pelican dadas en el taller.


### Crea tu propia imagen de docker

o bien *creá un `Dockerfile`* para modificar la imagen a gusto:

```
FROM python:3.9.6-alpine

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
RUN apk add git

EXPOSE 8000
```

y un archivo de texto `requirements.txt` : 
```
pelican
typogrify
markdown
ghp-import
```
en el mismo directorio que el archivo `Dockerfile`.

> Ventajas: añadir más dependencias que pueda requerir según el contenido.

Contruyelo con:

    `docker build -t pelicandevenv .`

 > No te olvides de agregar '.' al final del comando para refernciar al Dockerfile en el directorio actual.

 
Para ejecturarlo y acceder a la consola:

    `docker run -it --name pelicandevenv --rm --volume ${PWD}:/usr/src/app -p 8080:8000 pelicandevenv:latest sh`


> Curso docker en [este link](https://www.youtube.com/watch?v=UZpyvK6UGFo&list=PLqRCtm0kbeHAep1hc7yW-EZQoAJqSTgD-)


---
# Clonar el repositorio

Desde el directorio raiz del proyecto, donde inicialmente te encuentras, vamos a clonar el repositorio:

    `git clone https://github.com/CamilaEBF/camilaebf.github.io.git`

> TIP: puedes verificar en dónde te encuentras con el comando `pwd`
> También podes verificar cual es el servidor remoto `git remote -v`

Ahora verás actualizado el directorio con el nombre del repositorio. Accedemos a él:

    `cd camilaebf.github.io`

# Rama src

Crear la rama y acceder a ella: 

    `git checkout -b src`

> TIP: puedes verificar el estado de tu rama con `git status`.

Ahora pasemos a crear el archivo `.gitignore`:

    `touch .gitignore`

Y en VS Code, o tu IDE de preferencia, escribe:

```
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]

# C extensions
*.so

# Distribution / packaging
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*,cover
tests/output

# Translations
*.mo
*.pot

# Django stuff:
*.log

# Sphinx documentation
docs/_build/

# PyBuilder
target/

venv

# NPM
node_modules
```

Esto evitará que se almacene contenido que no se necesite en el repositorio remoto.

---
# Crea el sitio con Pelican

Para crear el sitio con Pelican, ejecuta en tu `terminal`:

    `pelican-quickstart`

Hará unas preguntas para su inicialización:

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

---
## Contenido por defecto

Generaremos una página de inicio con una lista de artículos.

    `/usr/src/app # pelican content`

---
## Ejecutá el sitio

Veamos cómo se ve el sitio:

    `/usr/src/app # pelican --listen -b 0.0.0.0`

---
 ## Accede

    Desde tu navegador  `http://localhost:8080`

---
# Configura el tema Flex

[Flex](https://github.com/alexandrevicenzi/Flex/wiki) es el *tema minimalista de Pelican*.

Para instalarlo primero vamos a clonarlo:

    `git clone https://github.com/alexandrevicenzi/Flex.git`

---


Like it? [Star it](https://github.com/CamilaEBF/camilaebf.github.io/stargazers)



