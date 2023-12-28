from dataclasses import asdict

from sphinxawesome_theme import ThemeOptions

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Audulus-Canvas'
copyright = '2023, Mark Alan Boyd'
author = 'Mark Alan Boyd'
release = 'v0.0.2-alpha'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinxawesome_theme.highlighting",
    "sphinxcontrib.luadomain"
]

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'lightbulb'



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinxawesome_theme'

theme_options = ThemeOptions(
    logo_dark="img/audulus-logo-dark.svg",
    logo_light="img/audulus-logo-light.svg",
)

html_theme_options = asdict(theme_options)