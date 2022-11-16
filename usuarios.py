class Usuario:

    users = []

    def __init__(self, nome, telefone, cpf, cep):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.cep = cep


    def cadastrarUsuario(self):
        userObject = {
                'nome': self.nome,
                'telefone': self.telefone,
                'cpf': self.cpf,
                'cep': self.cep,
                'emprestimos': {}
            }

        self.users.append(userObject)
        return (f'{self.nome} cadastrado com sucesso! {self.telefone}')
                


        
    def validarUsuario(self):
        pass
        
        
        
        
    