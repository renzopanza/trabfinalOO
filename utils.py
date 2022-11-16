import re

def validarNome(nome):
    

    for i in nome:

        valid = re.match(r'[a-zA-Z]', i)

        while not valid:
            return validarNome(input('Digite um nome valido: '))

    return nome  


def telValidation(telefone):
    
    padrao = "^[1-9]{2}(?:[2-8]|9[1-9])[0-9]{3}[0-9]{4}$"

    valid = re.search(padrao, telefone)

    while not valid:
            return telValidation(input('Digite um telefone valido: '))

    return telefone  

def cpfValidation(cpf):

    padrao = "^[0-9]{3}[0-9]{3}[0-9]{3}[0-9]{2}$"

    valid = re.search(padrao, cpf)
    
    while not valid:
        return cpfValidation(input('Digite um cpf valido: '))

    return cpf


def cepValidation(cep):

    padrao = "^[0-9]{8}$"

    valid = re.search(padrao, cep)

    while not valid:
        return cepValidation(input('Digite um cep valido: '))
    
    return cep