# Github to Colab Link Generator

[![Build Status](https://dev.azure.com/shawonAshraf/github-to-colab-link/_apis/build/status/ShawonAshraf.github-to-colab-link%20(1)?branchName=main)](https://dev.azure.com/shawonAshraf/github-to-colab-link/_build/latest?definitionId=11&branchName=main)

Sometimes you may want to load a Jupyter notebook from your repo to colab and run it there. Other times you may just want to add a colab link to your repositories readme page. Sure you can download and then import to colab but that may not always be ideal. The goal of this cli tool is to short-circuit that process so you don't have to go through extra clicks.

## Pre-requisites

- __The repo where your notebook is must be public__
- __Your system must have `python` installed__

## Installation and Usage

### Install from pip

```bash
pip install -U github-to-colab-link
```

### Usage

The package currently generates links in two formats, one is a plain string, which you can copy and load in an web browser; another is a markdown embed which you can use in your markdown style docs, e.g. Github readmes.

```bash
# for plain string
colab-link-gen --string --gh link_to_notebook
# example
colab-link-gen --string --gh https://github.com/ShawonAshraf/jax_examples/blob/main/playground/palmers_penguins.ipynb
```

```bash
# for markdown embed
colab-link-gen --md --gh link_to_notebook
# example
colab-link-gen --md --gh https://github.com/ShawonAshraf/jax_examples/blob/main/playground/palmers_penguins.ipynb
```

## Dev

- Clone the repo
- Create a `virtualenv`
- Install the requirements

```bash
pip install -r requirements.txt
```

- The entrypoint for the cli tool is in `cli.py` (the `run()` function)
- `link.py` contains the helpers to generate the links

### Testing

```bash
python -m unittest discover -s ./tests -p "*_test.py"
```
