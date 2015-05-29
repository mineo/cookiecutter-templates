#!/usr/bin/env sh
# Strip spaces around { and }
# Those are necessary for things like { \{\{cookiecutter....\}\} }
sed -e 's/{ /{/' -e 's/ }/}/' -i *.tex
git init
git add .
git commit -m "Initial commit"
