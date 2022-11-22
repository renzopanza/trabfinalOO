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
        json.dump((userObject), dbUser)
        dbUser.write('\n')
        return (f'{self.nome} cadastrado com sucesso!')
                
        
    def validarUsuario(login, paswd):
        dbUser = open("data/usuarios.txt")
        usr = []
        for line in dbUser:
            usr.append(json.loads(line))
        for i in usr:
            if login in i['nome']:
                if paswdEncode(paswd) == i["paswd"]:
                    return True
            
        return False