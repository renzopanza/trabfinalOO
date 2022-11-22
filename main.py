from usuarios import Usuario
from utils import *
import re
import pandas as pd

# try:

print('Bem vindo ao sistema de gerenciamento de biblioteca\n')

cadastrado = input('voce ja tem conta?"Para sim, digite "s", para não digite "n": ')


if cadastrado == 'n':

    nome = nameValidation(str(input('Digite seu nome: ')))

    telefone = telValidation(input('digite seu telefone: '))

    cpf = cpfValidation(input('Digite seu cpf: '))

    cep = cepValidation(input('Digite seu cep: '))
    
    senha = paswdValidation(input('Digite uma senha: '))

    user = Usuario(nome, telefone, cpf, cep, senha)

    print(user.cadastrarUsuario())
    
else:

    if cadastrado == 's':
        pass



# except:
#     print('Voce cometeu algum erro, por favor tente novamente. Try funcionou')