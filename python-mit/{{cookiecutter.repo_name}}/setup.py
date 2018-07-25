#!/usr/bin/env {{ cookiecutter.python_binary }}
from __future__ import print_function
from codecs import open
from os import path
from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(name="{{ cookiecutter.repo_name }}",
      author="{{ cookiecutter.full_name }}",
      author_email="{{ cookiecutter.email }}",
      packages=["{{ cookiecutter.repo_name }}"],
      package_dir={"{{ cookiecutter.repo_name }}": "{{ cookiecutter.repo_name }}"},
      download_url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/tarball/master",
      url="http://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}",
      license="MIT",
      classifiers=["Development Status :: 4 - Beta",
                   "License :: OSI Approved :: MIT License",
                   "Natural Language :: English",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python :: 2.7"],
      description="{{ cookiecutter.short_description }}",
      long_description=long_description,
      long_description_content_type='text/markdown',
      setup_requires=["setuptools_scm"],
      use_scm_version={"write_to": "{{ cookiecutter.repo_name }}/version.py"},
      extras_require={
          'docs': ['sphinx']
      }
      )
