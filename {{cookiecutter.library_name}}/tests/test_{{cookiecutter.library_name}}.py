import pytest
from {{cookiecutter.library_name}} import __version__, __author__, __email__, __doc__, __url__
def test_example():
    assert True

def test_{{cookiecutter.library_name}}_version():
    assert __version__ == '{{cookiecutter.version}}'

def test_{{cookiecutter.library_name}}_author():
    assert __author__ == '{{cookiecutter.author_name}}'

def test_{{cookiecutter.library_name}}_email():
    assert __email__ == '{{cookiecutter.email}}'

def test_{{cookiecutter.library_name}}_description():
    assert __doc__ == '{{cookiecutter.description}}'

def test_{{cookiecutter.library_name}}_url():
    assert __url__ == '{{cookiecutter.url}}'