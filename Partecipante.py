#Inizializza il giocatore con nome e cognome. con creazione classe Partecipante
class Partecipante:
   #È il costruttore della classe e serve per inizializzare gli attributi dell'oggetto
    def __init__(self, nome, cognome):
        #Si mettono due parametri: nome e cognome, che vengono poi assegnati 
        #agli attributi dell'oggetto tramite self.nome e self.cognome.
        self.nome = nome
        self.cognome = cognome
  
    #Mi permette di definire come un oggetto della classe Partecipante, mi 
    #restituisce una stringa formattata con il nome e il cognome del partecipante
    def __str__(self):
        return f"{self.nome} {self.cognome}"

    #Mi definisce l'uguaglianza tra oggetti metodo == per gli oggetti della 
    #classe Partecipante, mentre l'other è l'altro oggetto che viene confrontato con l'oggetto corrente
    def __eq__ (self, other): 
        return self.nome == other.nome and self.cognome == other.cognome
