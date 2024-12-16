
# Importo il modulo random per poter usare sample per poter randomizzare le posizioni dell'array delle assegnazioni
import random
from Partecipante import Partecipante

# Creo la classe gioco e la inizializzo con def init
class Gioco:
    def __init__(self):

        # Creo la lista per contenere i giocatori che partecipano al gioco
        self.giocatori = []

        # Creo una seconda lista per contenere un ordine randomizzato dei partecipanti che verranno poi assegnati
        self.assegnazioni = []

    # Creo il metodo inserisci per inserire i partecipanti del gioco
    def inserisci(self):

        # Creo la variabile richiesta che sarà l'input a cui chiedere l'utente una scelta fra quelle disponibili, in questo caso ho inserito solo la scelta di aggiungere un nuovo partecipante o terminare il programma
        # Con la funzione .strip tolgo eventuali spazi bianchi prima o dopo la stringa inserita. Con la funzione .lower rendo case insensitive l'input, in modo che digitando fine anche a caratteri diversi l'input venga preso
        #richiesta = input("Scrivi il nome del primo partecipante o 'fine' per terminare: ").strip().lower()
        richiesta=""
        # Creo un ciclo while che continua finchè l'utente non digita fine
        while richiesta != "fine":
            
            # Chiedo all'utente il nome del partecipante e uso la funzione .strip
            Nome = input("Inserisci il nome del partecipante o fine per terminare: ").strip()
            if Nome=="fine":
                if len(self.giocatori)>1:
                    break
                else:
                    print("Il numero dei giocatori è dispari ")
                    continue #per continuare col prossimo ciclo di iterazione
            # Creo un ciclo while che continua se l'utente inserisce numeri al posto di lettere e richiede all'utente il nome del partecipante
            # tramita la funzione all and .isalpha controllo che l'input dell'utente non contenga lettere, in caso contrario stampo un messaggio di errore e il ciclo si ripete
           # Con la funzione .isspace permetto che il Nome possa essere composto da più parole
            while not all(char.isalpha() or char.isspace() for char in Nome):
                print("Errore: devi digitare solo lettere. Riprova.")

                    # Richiedo dunque all'utente il nome del partecipante
                Nome = input("Inserisci il nome del partecipante: ").strip()

                # Chiedo all'utente il nome del partecipante e uso la funzione .strip
            Cognome = input("Inserisci il cognome del partecipante: ").strip()

                # tramita la funzione all and .isalpha controllo che l'input dell'utente non contenga lettere, in caso contrario stampo un messaggio di errore e il ciclo si ripete
                # Con la funzione .isspace permetto che il Cognome possa essere composto da più parole
            while not all(char.isalpha() or char.isspace() for char in Cognome):
                print("Errore: devi digitare solo lettere. Riprova.")
                Cognome = input("Inserisci il cognome del partecipante: ").strip()

                # creo la variabile partecipante a cui assegno la classe partecipante
            partecipante = Partecipante(Nome, Cognome)
                # aggiungo la variabile partecipante alla lista dei giocatori
            self.giocatori.append(partecipante)
            print("La lista dei nuovi giocatori è:")
            for g in self.giocatori:
                print(g)

            # Riscrivo l'input di richiesta per chiedere all'utente che opzione desidera scegliere (aggiungere partecipante o terminare) per far ripartire il ciclo in caso di errori dell'utente
            #richiesta = input("Digita '1' per aggiungere un nuovo partecipante o 'fine' per terminare: ").strip().lower()

        # Se tutto il ciclo prima creato non riscontra errori, il programma stampa la lista definitiva di tutti i giocatori scelti


        # utilizzo un ciclo for che itera su tutti gli elementi della lista giocatori, attributo dell'oggetto giocatore prima creato, e istanza della classe gioco
        # la variabile g rappresenta un singolo oggetto Partecipante della lista


# Creo il metodo assegna per andare ad assegnare i giocatori della prima lista con i giocatori della seconda
    def assegna(self):
        # Controllo se la lista dei giocatori non sia vuota
    #    if len(self.giocatori) > 0:
            # Controllo se il numero di giocatori sono pari
     #       if len(self.giocatori)%2 == 0:
     #           print('Assegnazione in corso...')
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

    #creo una funzione per stampare le assegnazioni
    def stampaAssegnazioni(self):
        #controllo la lista assegnazioni non sia vuota
        if len(self.assegnazioni)>0:
            #ciclo for per stampare ogni giocatore il suo amico segreto assegnato
            for j in range(len(self.assegnazioni)):
                #stampo ogni giocatore della lista self.giocatore e self.assegnazione
                print(f"Il giocatore {self.giocatori[j]} gli è stato assegnato l'amico {self.assegnazioni[j]}")


# Creo la variabile giocatore e le assegno la classe Gioco
#giocatore = Gioco()

# Invoco il metodo inserisci della classe Gioco
#giocatore.inserisci()