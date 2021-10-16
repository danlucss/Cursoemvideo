"""
Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
"""

from urllib.request import Request, urlopen
from urllib.error import URLError

req = Request('http://pudim.com.br')
try:
    res = urlopen(req)
except URLError:
    print('O site pudim não está acessivel no momento.')
else:
    print('O site pudim está acessivel.')
