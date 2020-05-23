#!/usr/bin/env sh
source $(which virtualenvwrapper.sh) && mkvirtualenv -p /usr/bin/{{ cookiecutter.python_binary }} -a $(pwd) {{ cookiecutter.repo_name }}

if [[ {{ cookiecutter.with_pkgbuild }} != "yes" ]]; then
    rm -rf misc
fi

git init
git add .
git rm --cached */version.py
git commit -m "Initial commit"
