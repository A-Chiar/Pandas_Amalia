#importo il modulo dove sono presenti le funzioni per effettuare la preanalisi dei dati con pandas
import Pandas_EsercizioFinale as ef
compagnia = ef.CompagniaTelecomunicazioni()


#creo il menù
while True:
    print("\nMenu:")
    print("1. Crea un Dataframe ")
    print("2. Esamina la distribuzione dei dati  ")
    print("3. Elimina dati mancanti ")
    print("4. Imputa dati mancanti, attraverso la media ")
    print("5. Elimina le anomalie ")
    print("6. Crea una nuova colonna 'Costo_per_GB ")
    print("7. Effettua dei raggruppamenti per esplorare le relazioni ")
    print("8. Ricerca le correlazioni tra le variabili ")
    print("9. Converti la colonna Churn in formato numerico")
    print("10. Normalizza le colonne numeriche")
    print("11. Salva il dataframe in formato CSV")
    print("11. Esci")

    seleziona = input("Scegli un'opzione: ")

    #effettuo un controllo sull'input inserito dall'utente
    if seleziona.isalpha():
            print("Errore Input ")
            break
    if seleziona.isspace():
            print("Errore Input ")

    if seleziona == '1':
        compagnia.crea_dataframe()
    
    elif seleziona == '2':
        compagnia.analisi_dataframe()
          
    elif seleziona == '3':
        compagnia.elimina_dati_mancanti()
    
    elif seleziona == '4':
        compagnia.imputa_dati_mancanti()
        
    elif seleziona == '5':
        compagnia.anomalie()
        
    elif seleziona == '6':
        compagnia.nuova_colonna()
        
    elif seleziona == '7':
        compagnia.raggruppa()
        
    elif seleziona == '8':
        compagnia.correlazioni()
        
    elif seleziona == '9':
        compagnia.modifica_churn()
        
    elif seleziona == '10':
        compagnia.normalizzazione()
        
    elif seleziona == '11':
        compagnia.salva_csv()

    elif seleziona == '12':
        break
    else:
        print("Scelta non valida. Riprova.")