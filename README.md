# problem-space

[![Build Status](https://travis-ci.com/ChristianMurphy/problem-space-py.svg?branch=master)](https://travis-ci.com/ChristianMurphy/problem-space-py)

for Python

> Takes a question template, creates questions in the problems space

## Usage

### CLI

```sh
problem-space --input example/addition.md
```

## Local Development

### Setup

1.  _Optional_ [install pyenv](https://github.com/pyenv/pyenv) (`curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash` then `pyenv update`)
2.  [Install Python 3.7+](https://www.python.org/downloads) (`pyenv install 3.7.1`)
3.  [Install Poetry](https://poetry.eustace.io/docs/) (`curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python`)
4.  `poetry install`

### Test

```sh
poetry run pytest
```

### Format Code

```sh
poetry run black .
```
