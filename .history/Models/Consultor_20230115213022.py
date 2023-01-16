import os
import csv

class Consultor:
  def __init__(self, user, password):
    self.id = self.__create_id()
    self.user = user
    self.__password = self.__hash_password()
    self.__create_consultor()
  
  def __create_id(self):


    if os.path.exists('Consultor.csv'):
      append_write = 'a' # Adicionar ao arquivo se o mesmo já existe

  def __hash_password(self):
    pass

  def __create_consultor(self):
    pass


