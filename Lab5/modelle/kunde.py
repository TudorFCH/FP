from modelle.identifiable import Identifiable

class Kunde(Identifiable):

    def __init__(self, id: int, name: str, adresse: str):
        super().__init__(id)
        self.name = name
        self.adresse = adresse

    def __repr__(self):
        return f'Customer: ID = {self.id}, Name = {self.name}, Address = {self.adresse}'