from tokenize import group
import pyperclip
import re


telefone_regex = re.compile(r'''(
                             (\d{3}|\(\d{3}\)|\d{2}|\(\d{2}\))?
                             (\s|-|\.)?
                             (\d{5}|\d{4})?
                             (\s|-|\.)
                             (\d{4})
                            )''',re.VERBOSE)

email_regex = re.compile(r'''(
                          [a-zA-Z0-9._%+-]+
                          @
                          [a-zA-Z0-9.-]+
                          (\.[a-zA-Z]{2,4})
                          )''',re.VERBOSE)

texto = str(pyperclip.paste())

conformidades = []

for grupos in telefone_regex.findall(texto):
    numero_telefone = '-'.join([grupos[1], grupos[3], grupos[5]])

for grupos in email_regex.findall(texto):
    conformidades.append(grupos[0])

if len(conformidades) > 0:
    pyperclip.copy('\n'.join(conformidades))
    print("Copiado para a área de transferência:")
    print('\n'.join(conformidades))
else:
    print("Não encontrado dados.")