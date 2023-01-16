import os
import csv
import b

class Consultor:
  def __init__(self, user, password):
    self.id = self.__create_id()
    self.user = user
    self.__password = self.__hash_password()
    self.__create_consultor()
  
  # Criado em ordem sequencial
  def __create_id(self):  

    # Ler Consultor.csv para saber qual o id para o próximo Consultor deve ser
    with open('Consultor.csv', 'r') as file:
      reader = csv.reader(file)
      self.id = len(reader)
      
  def __hash_password(self):
    try 

  def __create_consultor(self):
    pass


