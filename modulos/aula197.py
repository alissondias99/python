# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2

from pathlib import Path

from PyPDF2 import PdfReader, PdfWriter, PdfMerger

PDF = 'aula197.pdf'

reader = PdfReader(PDF)

#print(len(reader.pages))

# for page in reader.pages:
#     print(page) # cada retorno representa um elemento do PDF
#     print()

page = reader.pages[0]
#print(page.extract_text())

writer = PdfWriter()
writer.add_page(page) # copia os dados do pdf orginal para outro

with open('page.pdf', 'wb') as arquivo:
    writer.write(arquivo)

files = [
    'aula197.pdf',
    'page.pdf'
]

merger = PdfMerger() # Cria um PDF novo com o conteúdo dos dois antigos.

for file in files:
    merger.append(file)

with open('merged.pdf', 'wb') as arquivo:
    merger.write(arquivo)