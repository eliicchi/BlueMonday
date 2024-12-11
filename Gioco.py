# Importo il modulo random per poter usare sample per poter randomizzare le posizioni dell'array delle assegnazioni
import random
from Partecipante import Partecipante
# Creo la classe partecipante inizializzandola con init (andrà poi importata al momento della parte finale del progetto)

# Creo la classe gioco e la inizializzo con def init
class Gioco:
    def __init__(self):
        # Creo la lista per contenere i giocatori che partecipano al gioco
        self.giocatori = []
        # Creo una seconda lista per contenere un ordine randomizzato dei partecipanti che verranno poi assegnati
        self.assegnazioni = []

    # Creo il metodo inserisci per inserire i partecipanti del gioco
    def inserisci(self, nome, cognome):
        # creo la variabile partecipante a cui assegno la classe partecipante
        partecipante = Partecipante(nome, cognome)
        # aggiungo la variabile partecipante alla lista dei giocatori
        self.giocatori.append(partecipante)
        print(f"Aggiunto: {partecipante}")

    # Creo il metodo assegna per andare ad assegnare i giocatori della prima lista con i giocatori della seconda
    def assegna(self):
        # Controllo se la lista dei giocatori non sia vuota
        if len(self.giocatori) > 0:
            # Controllo se il numero di giocatori sono pari
            if len(self.giocatori)%2 == 0:
                print('Assegnazione in corso...')
                # Creo una variabile flag che serve per tenere traccia se le liste hanno i nomi nelle posizioni diverse
                diversi = False
                while not diversi:
                    # Assegno in i nomi in posizioni a caso con sample. Gli argomenti si sample sono l'array da randomizzare e la lunghezza
                    self.assegnazioni = random.sample(self.giocatori, len(self.giocatori))
                    # Ciclo for per controllare ogni posizione 
                    for i in range(len(self.giocatori)):
                        # Faccio un confronto tra i nomi delle liste se sono diversi
                        if self.giocatori[i] == self.assegnazioni[i]:
                            # Se i nomi della stessa posizione delle 2 liste sono uguali allora il ciclo for si interrompe e rifà la randomizzazione
                            diversi = False
                            break
                        else:
                            # Se i nomi sono diversi, il flag 'diversi' diventa True e il ciclo continua per controllare gli altri nomi 
                            diversi = True
                    if diversi:
                        # Se tutti i nomi sono diversi, allora il ciclo finisce
                        print('Assegnazione Eseguita')
            else:
                # Se i giocatori sono dispari si esce fuori dalla funzione e si richiede di assegnare
                print('I giocatori sono dispari, aggiungi un nuovo giocatore e riprova')
        else:
            print('Non ci sono giocatori')
    
