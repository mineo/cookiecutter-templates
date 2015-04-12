#!/usr/bin/env sh
source $(which virtualenvwrapper.sh) && mkvirtualenv -p /usr/bin/{{ cookiecutter.python_binary }} -a $(pwd) {{ cookiecutter.repo_name }}
git init
git add .
git rm --cached */version.py
git commit -m "Initial commit"
