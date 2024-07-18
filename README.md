# Pandas_Amalia
Script Python 
1 FASE: creazione dei dati
2 FASE: inizio a definire le classi che voglio creare
#TEMPO STIMATO TOTALE: 30 minuti
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
1. Caricare i dati da un file CSV. #TEMPO STIMATO: 10 min
2. Utilizzare info(), describe(), e value_counts() per esaminare la distribuzione dei dati e identificare colonne con valori mancanti. #TEMPO STIMATO: 15 minuti 
3. Pulizia dei Dati: #TEMPO STIMATO: 30 minuti
    3A. Gestire i valori mancanti in modo appropriato, considerando l'imputazione o la rimozione delle righe.
    3B. Verificare e correggere eventuali anomalie nei dati (es. età negative, tariffe mensili irrealistiche).
4. Analisi Esplorativa dei Dati (EDA): #TEMPO STIMATO: 50 minuti
    4A. Creare nuove colonne che potrebbero essere utili, come Costo_per_GB (tariffa mensile divisa per i dati consumati).
    4B. Utilizzare groupby() per esplorare la relazione tra Età, Durata_Abonnamento, Tariffa_Mensile e la Churn.
    4C. Utilizzare metodi come corr() per identificare possibili correlazioni tra le variabili.
5. Preparazione dei Dati per la Modellazione: #TEMPO STIMATO: 30 minuti
    5A. Convertire la colonna Churn in formato numerico (0 per "No", 1 per "Sì").
    5B. Normalizzare le colonne numeriche usando numpy per prepararle per la modellazione.
6. Analisi Statistica e Predittiva: #TEMPO STIMATO:  40 minuti
    6A. Implementare un semplice modello di regressione logistica usando scikit-learn per predire la probabilità di churn basata
        su altri fattori.
    6B. Valutare la performance del modello attraverso metriche come l'accuratezza e l'AUC (Area Under Curve)."""
