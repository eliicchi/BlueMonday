from Gioco import Gioco
def main():         #definizione del main
    # Creo la variabile giocatore e le assegno la classe Gioco
    gioco = Gioco()

    # Creo la variabile richiesta che sarà l'input a cui chiedere l'utente una scelta fra quelle disponibili, in questo caso ho inserito solo la scelta di aggiungere un nuovo partecipante o terminare il programma
    # Con la funzione .strip tolgo eventuali spazi bianchi prima o dopo la stringa inserita. Con la funzione .lower rendo case insensitive l'input, in modo che digitando fine anche a caratteri diversi l'input venga preso
    richiesta = input("Digita '1' per aggiungere un nuovo partecipante\nDigita '2' per assegnare o riassegnare l\'amico segreto ai partecipanti\nDigita 'fine' per terminare: ").strip().lower()

    # Creo un ciclo while che continua finchè l'utente non digita fine
    while richiesta != "fine":
    # se l'input dell'utente è 1, chiedo all'utente nome e cognome del partecipante
        if richiesta == "1":
            # Chiedo all'utente il nome del partecipante e uso la funzione .strip
            nome = input("Inserisci il nome del partecipante: ").strip()
            # Creo un ciclo while che continua se l'utente inserisce numeri al posto di lettere e richiede all'utente il nome del partecipante
            # tramita la funzione all and .isalpha controllo che l'input dell'utente non contenga lettere, in caso contrario stampo un messaggio di errore e il ciclo si ripete
            # Con la funzione .isspace permetto che il nome possa essere composto da più parole
            while not all(char.isalpha() or char.isspace() for char in nome):
                print("Errore: devi digitare solo lettere. Riprova.")
                # Richiedo dunque all'utente il nome del partecipante
                nome = input("Inserisci il nome del partecipante: ").strip()
            
            # Chiedo all'utente il nome del partecipante e uso la funzione .strip
            cognome = input("Inserisci il cognome del partecipante: ").strip()
            # tramita la funzione all and .isalpha controllo che l'input dell'utente non contenga lettere, in caso contrario stampo un messaggio di errore e il ciclo si ripete
            # Con la funzione .isspace permetto che il cognome possa essere composto da più parole
            while not all(char.isalpha() or char.isspace() for char in cognome):
                print("Errore: devi digitare solo lettere. Riprova.")
                cognome = input("Inserisci il cognome del partecipante: ").strip()

            # Se l'utente ha inserito il nome e il cognome corretti, richiamo il metodo inserisci della classe Gioco e aggiungo nome e cognome del partecipante come unico elemento all'interno della lista self.giocatori
            gioco.inserisci(nome, cognome)
        elif richiesta == '2':
            #list_assegna = gioco.assegna()
            gioco.assegna()
            print ("Le assegnazioni sono: \n")
            for x in range(len(gioco.giocatori)):
                print (f"{gioco.giocatori[x]} con {gioco.assegnazioni[x]}")
        # Aggiungo un messaggio di errore se l'utente quando gli viene chiesta un'opzione o di terminare il programma sceglie un valore non previsto e faccio ripartire il ciclo richiedendo all'utente l'opzione che desidera scegliere
        else:
            print("Errore: comando non valido. Digita '1' o 'fine'.")
        # Riscrivo l'input di richiesta per chiedere all'utente che opzione desidera scegliere (aggiungere partecipante o terminare) per far ripartire il ciclo in caso di errori dell'utente
        richiesta = input("Digita '1' per aggiungere un nuovo partecipante\nDigita '2' per assegnare l\'amico segreto ai partecipanti\nDigita 'fine' per terminare: ").strip().lower()

    # Se tutto il ciclo prima creato non riscontra errori, il programma stampa la lista definitiva di tutti i giocatori scelti
    print("La lista definitiva dei giocatori è:")
    # utilizzo un ciclo for che itera su tutti gli elementi della lista giocatori, attributo dell'oggetto giocatore prima creato, e istanza della classe gioco
    # la variabile g rappresenta un singolo oggetto Partecipante della lista


    for x in range(len(gioco.giocatori)):
        print (f"{gioco.giocatori[x]} con {gioco.assegnazioni[x]}")




if __name__ == "__main__":  #creazione funzione main (cioè la prima funzione che viene eseguita)
    main()                  #per organizzare meglio il codice richiamo il main
