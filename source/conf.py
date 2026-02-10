# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'RtD_KHSdoc'
copyright = '2026, HSKIM'
author = 'HSKIM'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# conf.py  아래의 확장 기능을 포함시켜서 Tex 문서 작성을 rst 파일에서 가능하게 함
extensions = [
    'sphinx.ext.mathjax',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'kr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
