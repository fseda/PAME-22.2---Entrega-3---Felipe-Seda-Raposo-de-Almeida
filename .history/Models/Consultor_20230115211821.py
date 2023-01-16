import csv

class Consultor:
  def __init__(self, user):
    self.id = self.create_id()
  
  def create_id(self):
    