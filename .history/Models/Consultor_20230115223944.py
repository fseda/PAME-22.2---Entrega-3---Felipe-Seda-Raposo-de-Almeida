import os
import csv
import bcrypt

class Consultor:
  def __init__(self, username, password):
    self.id = self.__create_id()
    self.username = username
    self.__password = self.__hash_password(password)
    self.__create_consultor()
  
  # Criado em ordem sequencial
  def __create_id(self):  

    # Ler Consultor.csv para saber qual o id para o próximo Consultor deve ser
    with open('Consultor.csv', 'r') as file:
      reader = csv.reader(file)
      self.id = len(reader)
      
  # "Hash" a senha para maior proteção
  def __hash_password(self, password):

    # Se não tiver o bcrypt instalado a senha é guardada "crua"
    try:
      return bcrypt.hashpw(password, bcrypt.gensalt())
    except:
      return password

  def __create_consultor(self):

    # Se existir Consultor.csv criar e definir headers
    if not os.path.exists('Consultor.csv'):
      with open('Consultor.csv', 'a') as file:
        fieldnames = ['id', 'username', 'password']

    # Adicionar consultor · base de dados
    with open('Consultor.csv', 'a') as file:
      fieldnames = ['id', 'username', 'password']
      writer = csv.DictWriter(file, fieldnames=fieldnames)

      writer.writerow({
        'id': self.id,\
        'username': self.username,\
        'password': self.password\
      })






