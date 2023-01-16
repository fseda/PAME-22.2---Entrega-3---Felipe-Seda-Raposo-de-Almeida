import os
import csv
import bcrypt

class Gerente:
  def __init__(self, username, password):
    self.id = self.__create_id()
    self.username = self.set_username(username)
    self.__password = self.set_password(password)
    self.__create_gerente()

    self.projetos = []
  
  # Criado em ordem sequencial
  def __create_id(self):  

    if os.path.exists('Gerente.csv'):
      # Ler Gerente.csv para saber qual o id para o próximo Gerente deve ser
      with open('Gerente.csv', 'r') as file:
        reader = csv.reader(file)
        self.id = len(list(reader))
    else:
      self.id = 0  
    
  # "Hash" a senha para maior proteção
  def __hash_password(self, password):
    # Se não tiver o bcrypt instalado a senha é guardada "crua"
    try:
      return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    except:
      return password

  def __create_gerente(self):

    # Se existir Gerente.csv criar e definir headers
    if not os.path.exists('Gerente.csv'):
      with open('Gerente.csv', 'a') as file:
        fieldnames = ['id', 'username', 'password']

    # Adicionar gerente à base de dados
    with open('Gerente.csv', 'a') as file:
      fieldnames = ['id', 'username', 'password']
      writer = csv.DictWriter(file, fieldnames=fieldnames)

      writer.writerow({
        'id': self.id,
        'username': self.username,
        'password': self.__password,
      })

  @property
  def username(self):
    return self.username

  @username.setter
  def username(self, username):
    return username

  @property
  def password(self):
    return self.__password
 

  def set_password(self, password):
    return self.__hash_password(password)





