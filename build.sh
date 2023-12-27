#!/bin/zsh

# Navigate to the directory containing your Sphinx documentation
cd ~/developer/audulus-canvas-docs/

# Run Sphinx build command
sphinx-build -b html . _build/html

open _build/html/index.html