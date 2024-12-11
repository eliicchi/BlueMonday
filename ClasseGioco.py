# Importo il modulo random per poter usare sample per poter randomizzare le posizioni dell'array delle assegnazioni
import random
# Creo la classe partecipante inizializzandola con init (andrà poi importata al momento della parte finale del progetto)
class Partecipante:
    def __init__(self, Nome, Cognome):
        self.Nome = Nome
        self.Cognome = Cognome

    # Con il metodo def str comando come mostrare la classe
    def __str__(self):
        return f"{self.Nome} {self.Cognome}"

# Creo la classe gioco e la inizializzo con def init
class Gioco:
    def __init__(self):
        # Creo la lista per contenere i giocatori che partecipano al gioco
        self.giocatori = []
        # Creo una seconda lista per contenere un ordine randomizzato dei partecipanti che verranno poi assegnati
        self.assegnazioni = []

    # Creo il metodo inserisci per inserire i partecipanti del gioco
    def inserisci(self, Nome, Cognome):
        # creo la variabile partecipante a cui assegno la classe partecipante
        partecipante = Partecipante(Nome, Cognome)
        # aggiungo la variabile partecipante alla lista dei giocatori
        self.giocatori.append(partecipante)
        print(f"Aggiunto: {partecipante}")

    # Creo il metodo assegna per andare ad assegnare i giocatori della prima lista con i giocatori della seconda
    def assegna(self):
        # Controllo se il numero di giocatori sono pari
        if len(self.giocatori)%2 == 0:
            # Creo una variabile flag che serve per tenere traccia se le liste hanno i nomi nelle posizioni diverse
            diversi = False
            while not diversi:
                # Assegno in i nomi in posizioni a caso con sample. Gli argomenti si sample sono l'array da randomizzare e la lunghezza
                self.assegnazioni = random.sample(self.giocatori, len(self.giocatori))
                # Ciclo for per controllare ogni posizione 
                for i in range(len(self.giocatori)):
                    # Faccio un confronto tra i nomi delle liste se sono diversi
                    if self.giocatori[0] == self.assegnazioni[0]:
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
    
# Creo la variabile giocatore e le assegno la classe Gioco
gioco = Gioco()

# Creo la variabile richiesta che sarà l'input a cui chiedere l'utente una scelta fra quelle disponibili, in questo caso ho inserito solo la scelta di aggiungere un nuovo partecipante o terminare il programma
# Con la funzione .strip tolgo eventuali spazi bianchi prima o dopo la stringa inserita. Con la funzione .lower rendo case insensitive l'input, in modo che digitando fine anche a caratteri diversi l'input venga preso
richiesta = input("Digita '1' per aggiungere un nuovo partecipante\nDigita '2' per assegnare l\'amico segreto ai partecipanti\nDigita 'fine' per terminare: ").strip().lower()

# Creo un ciclo while che continua finchè l'utente non digita fine
while richiesta != "fine":
# se l'input dell'utente è 1, chiedo all'utente nome e cognome del partecipante
    if richiesta == "1":
        # Chiedo all'utente il nome del partecipante e uso la funzione .strip
        Nome = input("Inserisci il nome del partecipante: ").strip()
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

        # Se l'utente ha inserito il nome e il cognome corretti, richiamo il metodo inserisci della classe Gioco e aggiungo nome e cognome del partecipante come unico elemento all'interno della lista self.giocatori
        gioco.inserisci(Nome, Cognome)
    elif richiesta == '2':
        print('Assegnazione in corso...')
        gioco.assegna()

    # Aggiungo un messaggio di errore se l'utente quando gli viene chiesta un'opzione o di terminare il programma sceglie un valore non previsto e faccio ripartire il ciclo richiedendo all'utente l'opzione che desidera scegliere
    else:
        print("Errore: comando non valido. Digita '1' o 'fine'.")
    # Riscrivo l'input di richiesta per chiedere all'utente che opzione desidera scegliere (aggiungere partecipante o terminare) per far ripartire il ciclo in caso di errori dell'utente
    richiesta = input("Digita '1' per aggiungere un nuovo partecipante\nDigita '2' per assegnare l\'amico segreto ai partecipanti\nDigita 'fine' per terminare: ").strip().lower()

# Se tutto il ciclo prima creato non riscontra errori, il programma stampa la lista definitiva di tutti i giocatori scelti
print("La lista definitiva dei giocatori è:")
# utilizzo un ciclo for che itera su tutti gli elementi della lista giocatori, attributo dell'oggetto giocatore prima creato, e istanza della classe gioco
# la variabile g rappresenta un singolo oggetto Partecipante della lista
for g in gioco.giocatori:
    print(g)

print('Mentre la lista random è:')

for g in gioco.giocatori:
    print(g)