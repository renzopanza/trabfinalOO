import json
from utils import *

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
        dbUser.write(str(userObject) + '\n')
        return (f'{self.nome} cadastrado com sucesso! {self.telefone}')
                
        
    def validarUsuario(self):
        dbUser = open("data/usuarios.txt", "r")
        pass
        
        
    