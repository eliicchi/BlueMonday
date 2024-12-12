#Inizializza il giocatore con nome e cognome. con creazione classe Partecipante
class Partecipante:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    def __str__(self):
        return f"{self.nome} {self.cognome}"

    def __eq__ (self, other): #mi definisce l'uguaglianza tra oggetti
        return self.nome == other.nome and self.cognome == other.cognome