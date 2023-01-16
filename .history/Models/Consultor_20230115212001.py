import csv

class Consultor:
  def __init__(self, user, password):
    self.id = self.__create_id()
    self.user = user
    self.__password = password
  

  def __create_id(self):

