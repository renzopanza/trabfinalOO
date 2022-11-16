from usuarios import Usuario
from utils import *
import re

try:

    print('Bem vindo ao sistema de gerenciamento de biblioteca\n')

    cadastrado = input('voce ja tem conta?"Para sim, digite "s", para não digite "n": ')


    if cadastrado == 'n':

        nome = validarNome(str(input('Digite seu nome: ')))

        telefone = telValidation(input('digite seu telefone no formato : '))

        cpf = cpfValidation(input('Digite seu cpf: '))

        cep = cepValidation(input('Digite seu cep: '))

        user = Usuario(nome, telefone, cpf, cep)

        print(user.cadastrarUsuario())
        
    else:

        if cadastrado == 's':

            nome = nomeValidation(str(input('digite seu nome: ')))

            cpf = cpfValidation(input('Digite seu cpf: '))

except:
    print('Voce cometeu algum erro, por favor tente novamente. Try funcionou')