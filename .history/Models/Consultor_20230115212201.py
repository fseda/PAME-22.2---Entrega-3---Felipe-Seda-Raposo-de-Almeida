import csv

class Consultor:
  def __init__(self, user, password):
    self.id = self.__create_id()
    self.user = user
    self.__password = self.__hash_password()
    self.create
  

  def __create_id(self):

