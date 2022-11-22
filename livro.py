from utils import *
import pandas as pd
import json

class Livro:
    
   
    
    def __init__(self,id_livro, nome_livro,preco):
        self.nome_livro = nome_livro
        self.id_livro = id_livro
        self.preco = preco

    def cadastrarLivro(self):
        livroObject = {
            "id" : self.id_livro,
            "nome" : self.nome_livro,
            "preco" : self.preco
        }
        dbLivro = open("data/livros.txt", "a")
        data = json.loads()
        banco = pd.read()
        print(banco)
        
        json.dump(livroObject, dbLivro, indent=4)
        dbLivro.close()
        return (f'{self.nome_livro} cadastrado com sucesso!')


    #def consultarLivro(self):
          
