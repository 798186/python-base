#!/usr/bin/python3
"""Hello Word Multi Linguas

Dependendo da Lingua configurada no ambiente o programa exibe a mensagem 
correspondete.

Como usar:

Tenha a variavel LANG devidamente configurada ex:

    exporr LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Eduardo Oliveira"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG","en_US")[:5]

msg = "Hello, Word!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour, Monde!"
print(msg)

