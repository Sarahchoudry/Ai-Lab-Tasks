from setuptools import setup
author_name = 'Masooma Zahra'
src_repo = 'src'
list_of_requirements = ['streamlit']

setup(
    name=src_repo,
    version='0.0.1',
    author=author_name,
    author_email='masoomazahra616@gmail.com',
    description='Python package to make a simple web app',
    packages=[src_repo],
    python_requires='>=3.7',
    install_requires=list_of_requirements 
)