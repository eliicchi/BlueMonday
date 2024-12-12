from Gioco import Gioco
def main():         #definizione del main
    print("yahoooooo")
    # Creo la variabile giocatore e le assegno la classe Gioco
    gioco = Gioco()

    #while len(gioco.giocatori)==0 or len(gioco.giocatori)%2==1: 
#ENTRA IN CICLO SE LA LUNGHEZZA è DISPARI O 0 (CIOè 0 GIOCATORI ASSEGNATI) 
   # while True: 

    gioco.inserisci() 
    gioco.assegna()
    gioco.stampaAssegnazioni()
 #RICHIEDE DI INSERIRE IL NOME DEI GIOCATORI
       # gioco.assegna()
#ASSEGNA UN GIOCATORE AD UN ALTRO
       # gioco.stampaAssegnazioni()


if __name__ == "__main__":  #creazione funzione main (cioè la prima funzione che viene eseguita)
    main()                  #per organizzare meglio il codice richiamo il main
