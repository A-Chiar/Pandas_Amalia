#importo il modulo dove sono presenti le funzioni per effettuare la preanalisi dei dati con pandas
import Pandas_EsercizioFinale as ef
compagnia = ef.CompagniaTelecomunicazioni()
#imposto inizialmente il dataframe come None
df = None
#importo anche il modulo per la gestione degli errori
import GestioneErrori as ge
errori = ge.Error()

#creo il menù, dove all'interno inserisco anche la gestione degli errori che potrebbero verificarsi durante l'uso del programma
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
    print("11. Esci")

    seleziona = input("Scegli un'opzione: ")

    #effettuo un controllo sull'input inserito dall'utente
    if seleziona.isalpha():
            print("Errore Input ")
            break
    if seleziona.isspace():
            print("Errore Input ")

    if seleziona == '1':
        
        df=compagnia.crea_dataframe()
    

    elif seleziona == '2':
        if df is not None:
            compagnia.analisi_dataframe(df)
        else:
            errori.gestioneNameError()

    elif seleziona == '3':
        
        if df is not None:
            df = compagnia.elimina_dati_mancanti(df)
        else:
            errori.gestioneNameError()

    elif seleziona == '4':
        
        if df is not None:
            df = compagnia.imputa_dati_mancanti(df)
        else:
            errori.gestioneNameError()

    elif seleziona == '5':
        
        if df is not None:
            df = compagnia.anomalie(df)
        else:
            errori.gestioneNameError()

    elif seleziona == '6':
        
        if df is not None:
            df = compagnia.nuova_colonna(df)
        else:
            errori.gestioneNameError()

    elif seleziona == '7':
        
        if df is not None:
            compagnia.raggruppa(df)
        else:
            errori.gestioneNameError()

    elif seleziona == '8':
        
        if df is not None:
            compagnia.correlazioni(df)
        else:
            errori.gestioneNameError()


    elif seleziona == '9':
            
        if df is not None:
            df = compagnia.modifica_churn(df)
        else:
            errori.gestioneNameError()

    elif seleziona == '10':
            
        if df is not None:
            compagnia.normalizzazione(df)
        else:
            errori.gestioneNameError()

    elif seleziona == '11':
        break
    else:
        print("Scelta non valida. Riprova.")