# (Parte 1) Básico do protocolo HTTP (HyperText Transfer Protocol)
# HTTP (HyperText Transfer Protocol) é um protocolo usado enviar e receber dados na Internet. Ele funciona no modo cliente/servidor, onde o cliente (seu navegador, por exemplo) faz uma requisição ao servidor (site, por exemplo), que responde com os dados adequados.


# A mensagem de requisição do cliente deve incluir dados como:
# - O método HTTP
#     - leitura (safe) - GET, HEAD (cabeçalhos), OPTIONS (métodos suportados)
#     - escrita - POST, PUT (substitui), PATCH (atualiza), DELETE
# - O endereço do recurso a ser acessado (/users/)
# - Os cabeçalhos HTTP (Content-Type, Authorization)
# - O Corpo da mensagem (caso necessário, de acordo com o método HTTP)
#
# A mensagem de resposta do servidor deve incluir dados como:
# - código de status HTTP (200 success, 404 Not found, 301 Moved Permanently)
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
# - Os cabeçalhos HTTP (Content-Type, Accept)
# - O corpo da mensagem (Pode estar em vazio em alguns casos)

# para iniciar o servido com os arquivo de aula190_site: python -m http.server -d aula190_site/ 3333

#↓ Conteúdo aula 191 ↓
#request para requisições HTTP

import requests

url = "http://localhost:3333/"

response = requests.get(url)

print(response.status_code)
# print(response.content) # retorna o conteúdo da página em bits
# print(response.json()) # retorna o conteúdo da página em json
# print(response.header) # retorna o cabeçalho da pagina 
print(response.text)