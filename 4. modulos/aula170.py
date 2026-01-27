# os.lisdir para navegar em caminhos
import os

caminho = os.path.join('C:\\Users\\dias9\\Desktop\\Udemy\\python')

for pasta in os.listdir(caminho):
    print(pasta)
    
    if not os.path.isdir(pasta):
        continue

    for imagem in os.listdir(pasta):
        print(imagem)