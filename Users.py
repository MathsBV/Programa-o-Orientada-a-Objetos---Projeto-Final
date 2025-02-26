from Database import *
from Manager import Manager

class Users():
    def __init__(self, id: int, name: str, email: str, password: str, position: str) -> None:
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.position = position


class UsersManager(Manager):
    def __init__(self):
        self.DAO = UsersDBDAO()
    
    def register(self, user: Users):
        self.DAO.insert(user.id, user.name, user.email, user.password, user.position)
        
    def view(self):
        pass
    
    def update(self):
        pass

    def delete(self):
        pass

'''
As funções precisam:
    criar conexão com banco de dados;
    criar cursor da conexão;
    executar comando;
    fazer o "commit" da ação;
    encerrar conexão com o banco de dados.

As interações com o banco de dados ocorrerão 
através das classes DAO
'''