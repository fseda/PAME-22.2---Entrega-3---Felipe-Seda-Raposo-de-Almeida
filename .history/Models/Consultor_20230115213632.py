import os
import csv

class Consultor:
  def __init__(self, user, password):
    self.id = self.__create_id()
    self.user = user
    self.__password = self.__hash_password()
    self.__create_consultor()
  
  # 
  def __create_id(self):  

    # Ler Consultor.csv para saber qual o id para o próximo Consultor deve ser
    with open('Consultor.csv', 'r') as file:
      writer = csv.writer(file,)

  def __hash_password(self):
    pass

  def __create_consultor(self):
    pass


