#Inizializza il giocatore con nome e cognome con creazione classe Partecipante
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
        if not isinstance(other, Partecipante):
            return self.nome == other.nome and self.cognome == other.cognome

# Creo la classe gioco e la inizializzo con def init
class Gioco:
    def __init__(self):

        # Creo la lista per contenere i giocatori che partecipano al gioco
        self.giocatori = []

        # Creo un dizionario per tenere poi traccia dei nomi duplicati
        self.contatore_nomi = {}

        # Creo una seconda lista per contenere un ordine randomizzato dei partecipanti che verranno poi assegnati
        self.assegnazioni = []

    # Creo il metodo inserisci per inserire i partecipanti del gioco
    def inserisci(self):

        # Creo la variabile richiesta che sarà l'input a cui chiedere l'utente una scelta fra quelle disponibili, in questo caso ho inserito solo la scelta di aggiungere un nuovo partecipante o terminare il programma
        # Con la funzione .strip tolgo eventuali spazi bianchi prima o dopo la stringa inserita. Con la funzione .lower rendo case insensitive l'input, in modo che digitando fine anche a caratteri diversi l'input venga preso
        richiesta = input("Digita '1' per aggiungere un nuovo partecipante o 'fine' per terminare: ").strip().lower()

        # Creo un ciclo while che continua finchè l'utente non digita fine
        while richiesta != "fine":

            # se l'input dell'utente è 1, chiedo all'utente nome e cognome del partecipante
            if richiesta == "1":

                # Chiedo all'utente il nome del partecipante e uso la funzione .strip
                nome = input("Inserisci il nome del partecipante: ").strip()

                # Creo un ciclo while che continua se l'utente inserisce numeri al posto di lettere e richiede all'utente il nome del partecipante
                # tramita la funzione all and .isalpha controllo che l'input dell'utente non contenga lettere, in caso contrario stampo un messaggio di errore e il ciclo si ripete
                # Con la funzione .isspace permetto che il Nome possa essere composto da più parole
                while not all(char.isalpha() or char.isspace() for char in nome) or nome == "":
                    print("Errore: devi digitare solo lettere. Riprova.")

                    # Richiedo dunque all'utente il nome del partecipante
                    nome = input("Inserisci il nome del partecipante: ").strip()

                # Chiedo all'utente il nome del partecipante e uso la funzione .strip
                cognome = input("Inserisci il cognome del partecipante: ").strip()

                # tramita la funzione all and .isalpha controllo che l'input dell'utente non contenga lettere, in caso contrario stampo un messaggio di errore e il ciclo si ripete
                # Con la funzione .isspace permetto che il Cognome possa essere composto da più parole
                while not all(char.isalpha() or char.isspace() for char in cognome) or nome == "":
                    print("Errore: devi digitare solo lettere. Riprova.")
                    cognome = input("Inserisci il cognome del partecipante: ").strip()

                # Creo una tupla che rappresenta una chiave univoca per nome e cognome
                chiave = (nome, cognome)

                # Controllo se esiste già la combinazione nome e cognome
                # Se la combinazione esiste già nel dizionario allora...
                if chiave in self.contatore_nomi:
                    # Aggiungo un numero progressivo al partecipante
                    self.contatore_nomi[chiave] += 1
                    cognome += f"_{self.contatore_nomi[chiave]}"
                    print(f"Sei il giocatore {nome} {cognome}")
                else:
                    # Se la combinazione nome e cognome non esiste la aggiungo al dizionario per eventuali controlli su un partecipante doppio
                    self.contatore_nomi[chiave] = 1

                # creo la variabile partecipante a cui assegno la classe partecipante
                partecipante = Partecipante(nome, cognome)
                # aggiungo la variabile partecipante alla lista dei giocatori
                self.giocatori.append(partecipante)
                print(f"Aggiunto: {partecipante}")

            

            # Aggiungo un messaggio di errore se l'utente quando gli viene chiesta un'opzione o di terminare il programma sceglie un valore non previsto e faccio ripartire il ciclo richiedendo all'utente l'opzione che desidera scegliere
            else:
                print("Errore: comando non valido. Digita '1' o 'fine'.")

            # Riscrivo l'input di richiesta per chiedere all'utente che opzione desidera scegliere (aggiungere partecipante o terminare) per far ripartire il ciclo in caso di errori dell'utente
            richiesta = input("Digita '1' per aggiungere un nuovo partecipante o 'fine' per terminare: ").strip().lower()

        # Se tutto il ciclo prima creato non riscontra errori, il programma stampa la lista definitiva di tutti i giocatori scelti
        print("La lista definitiva dei giocatori è:")

        # utilizzo un ciclo for che itera su tutti gli elementi della lista giocatori, attributo dell'oggetto giocatore prima creato, e istanza della classe gioco
        # la variabile g rappresenta un singolo oggetto Partecipante della lista
        for g in self.giocatori:
            print(g)

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

# Creo la variabile giocatore e le assegno la classe Gioco
giocatore = Gioco()

# Invoco il metodo inserisci della classe Gioco
giocatore.inserisci()