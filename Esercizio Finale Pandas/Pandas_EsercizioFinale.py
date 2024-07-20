#Pandas
"""Obiettivo: Utilizzare pandas e numpy per esplorare, pulire, trasformare e analizzare un dataset di clienti della compagnia di
telecomunicazioni. L'esercizio mira a costruire un modello predittivo di base per la churn rate e scoprire correlazioni tra
vari attributi del cliente e la loro fedeltà."""
#Dataset: 
"""ID_Cliente: Identificativo unico per ogni cliente
Età: Età del cliente
Durata_Abonnamento: Quanti mesi il cliente è stato abbonato
Tariffa_Mensile: Quanto il cliente paga al mese
Dati_Consumati: GB di dati consumati al mese
Servizio_Clienti_Contatti: Quante volte il cliente ha contattato il servizio clienti
Churn: Se il cliente ha lasciato la compagnia (Sì/No)
"""
#Caricamento e Esplorazione Iniziale:
"""
X1. Caricamento e Esplorazione Iniziale:
     1A. Caricare i dati da un file CSV. #TEMPO STIMATO: 10 min  10 min
     2A. Utilizzare info(), describe(), e value_counts() per esaminare la distribuzione dei dati e identificare colonne con valori mancanti. #TEMPO STIMATO: 25 minuti 
2. Pulizia dei Dati: #TEMPO STIMATO: 30 minuti >
    2A. Gestire i valori mancanti in modo appropriato, considerando l'imputazione o la rimozione delle righe.
    2B. Verificare e correggere eventuali anomalie nei dati (es. età negative, tariffe mensili irrealistiche).
3. Analisi Esplorativa dei Dati (EDA): #TEMPO STIMATO: 50 minuti <20 min
    3A. Creare nuove colonne che potrebbero essere utili, come Costo_per_GB (tariffa mensile divisa per i dati consumati).
    3B. Utilizzare groupby() per esplorare la relazione tra Età, Durata_Abonnamento, Tariffa_Mensile e la Churn.
    3C. Utilizzare metodi come corr() per identificare possibili correlazioni tra le variabili.
4. Preparazione dei Dati per la Modellazione: #TEMPO STIMATO: 30 minuti
    4A. Convertire la colonna Churn in formato numerico (0 per "No", 1 per "Sì").
    4B. Normalizzare le colonne numeriche usando numpy per prepararle per la modellazione.
5. Analisi Statistica e Predittiva: #TEMPO STIMATO:  40 minuti
    5A. Implementare un semplice modello di regressione logistica usando scikit-learn per predire la probabilità di churn basata
        su altri fattori.
    5B. Valutare la performance del modello attraverso metriche come l'accuratezza e l'AUC (Area Under Curve)."""

#importo le librerie
import pandas as pd
import numpy as np

#importo anche il modulo per la gestione degli errori
import GestioneErrori as ge
errori = ge.Error()

#creo la classe compagnia telecomunicazioni
class CompagniaTelecomunicazioni():
    def __init__(self): #creo la classe costruttore
        self.df = None
    
    #creo il metodo per creare il dataframe
    def crea_dataframe(self):
        self.df = pd.read_csv('EsercizioFinale.csv')
        print(self.df)
        return self.df
    
    #creo un metodo per le statistiche descrittive
    def analisi_dataframe(self):
        try:
            print("\n Riassunto delle informazioni del dataframe: ")
            print(self.df.info(verbose=True))
        except AttributeError:
            errori.gestioneAttributeError()
        
        try:
            print("\n Descrizione del dataframe: ")
            print(self.df.describe(include='all'))
        except AttributeError:
            errori.gestioneAttributeError()

        try:
            for column in self.df.columns:
                print(f"\nConta i valori per la colonna {column}:")
                print(self.df[column].value_counts())
        except TypeError:
            errori.gestioneTypeError()
    #creo un metodo per la pulizia dei dati, nel primo elimino i valori mancanti dell'ID

    def elimina_dati_mancanti(self):
        try:
            self.df = self.df.dropna(subset=['ID_Cliente'])
            print(self.df)
            return self.df
        except AttributeError:
            errori.gestioneAttributeError()
        
    #nel secondo creo un metodo per la sostituzione dei valori con la media dei valori di quella colonna
    def imputa_dati_mancanti(self):
        try:
            self.df['Età'] = self.df['Età'].fillna(self.df['Età'].mean())
            self.df['Durata_Abbonamento'] = self.df['Durata_Abbonamento'].fillna(self.df['Durata_Abbonamento'].median())
            self.df['Tariffa_Mensile'] = self.df['Tariffa_Mensile'].fillna(self.df['Tariffa_Mensile'].mean())
            self.df['Dati_Consumati'] = self.df['Dati_Consumati'].fillna(self.df['Dati_Consumati'].median())
            self.df['Servizio_Clienti_Contatti'] = self.df['Servizio_Clienti_Contatti'].fillna(self.df['Servizio_Clienti_Contatti'].mode()[0])
            self.df['Churn'] = self.df['Churn'].fillna('No')
            print(self.df)
            return(self.df)
        except TypeError:
            errori.gestioneTypeError()
    #gestisco i valori anomali, come le età negative
    def anomalie(self):
        try:
            self.df = self.df[self.df['Età'] > 0]
            print(self.df)
            return self.df
        except AttributeError:
            errori.gestioneAttributeError()

    #genero la nuova colonna Costo_per_GB
    def nuova_colonna(self):
        try:
            self.df['Costo_per_GB']=self.df['Tariffa_Mensile']/self.df['Dati_Consumati']
            print("\n è stata aggiunta la categoria Costo_per_GB: ",self.df)
            return self.df
        except TypeError:
            errori.gestioneTypeError()
        
    #raggruppo per esplorare le relazioni
    def raggruppa(self):
        try:
            media_età_tariffa = self.df.groupby('Età')['Tariffa_Mensile'].mean()
            print("\n",media_età_tariffa)
            media_churn_durata = self.df.groupby('Churn')['Tariffa_Mensile'].mean()
            print("\n", media_churn_durata)
            moda_età_durata = self.df.groupby('Durata_Abbonamento')['Età'].mean()
            print("\n", moda_età_durata)
        except AttributeError:
            errori.gestioneAttributeError()

    #ricerco le correlazioni
    def correlazioni(self):
        try:
            print(self.df.corr(method = 'pearson',numeric_only = True)) #fare in modo di eliminare dalla corr l'uso della colonna ID
        except AttributeError:
            errori.gestioneAttributeError()

    #converto la colonna Churn in formato numerico (0 per "No", 1 per "Sì").
    def modifica_churn(self):
        try:
            self.df['Churn']=self.df['Churn'].map(lambda x: 1 if x == "Sì" else 0)
            print(self.df)
            return self.df
        except TypeError:
            errori.gestioneTypeError()
    #effettuo la normalizzazione
    def normalizzazione(self):
        try:
            print("\n I valori normalizzati sono: ")
            for colonna in self.df.columns:
                self.df[colonna]=(self.df[colonna] - self.df[colonna].min()) / (self.df[colonna].max() - self.df[colonna].min())
            print(self.df)
        except TypeError:
            errori.gestioneTypeError()

    def salva_csv(self):
        self.df.to_csv('EsercizioFinale.csv', index=False)
        print(" -- CSV AGGIORNATO -- ")

