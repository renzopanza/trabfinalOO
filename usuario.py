import json
from utils import *
import pandas as pd

class Usuario:

    def __init__(self, nome, telefone, cpf, cep, paswd):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.cep = cep
        self.paswd = paswd


    def cadastrarUsuario(self):
        userObject = {
            "nome" : self.nome,
            "telefone" : self.telefone,
            "cpf" : self.cpf,
            "cep" : self.cep,
            "paswd" : paswdEncode(self.paswd)
        }

        dbUser = open("data/usuarios.txt", "a")
        json.dump(userObject, dbUser, indent=4)
        dbUser.close()
        return (f'{self.nome} cadastrado com sucesso!')
                
        
    def validarUsuario(nome, passwd):
        dbUser = open("data/usuarios.txt", "r")
        data = json.loads(dbUser.read())
        teste = []
        for i in data[0]:
            teste.append(i)

        return teste
