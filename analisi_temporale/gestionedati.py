###Programma realizzato con Davide Pappalardo

"""L'obiettivo di questo esercizio è generare un set di dati di serie temporali
utilizzando NumPy, analizzarli con pandas e visualizzare i risultati usando
Matplotlib. Gli studenti dovranno eseguire le seguenti operazioni:
1. Generazione dei Dati: Utilizzare NumPy per generare una serie temporale
di 365 giorni di dati, simulando il numero di visitatori giornalieri in
un parco. Assumere che il numero medio di visitatori sia 2000 con una
deviazione standard di 500. Inoltre, aggiungere un trend crescente nel
tempo per simulare l'aumento della popolarità del parco.
2. Creazione del DataFrame: Creare un DataFrame pandas con le date come
indice e il numero di visitatori come colonna.
3. Analisi dei Dati: Calcolare il numero medio di visitatori per mese e la
deviazione standard.
4. Visualizzazione dei Dati:
- Creare un grafico a linee del numero di visitatori giornalieri.
- Aggiungere al grafico la media mobile a 7 giorni per mostrare la
tendenza settimanale.
- Creare un secondo grafico che mostri la media mensile dei visitatori."""

import pandas as pd
import numpy as np
import gestioneerrori as er
import matplotlib.pyplot as plt

errori = er.Error()

class Gestionedati:
    def __init__(self):
        self.df = None

    def generazione_dati(self):
        n_medio = 2000
        deviazione = 500
        giorni = np.arange('2023-01', '2024-01', dtype='datetime64[D]')
        visitatori = np.random.normal(n_medio, deviazione, size= 365)
        trend = np.linspace(0,500, len(giorni))  
        visitatori_trend = visitatori + trend
        visitatori_trend = visitatori_trend.astype(int)
        print(trend)
        print(visitatori_trend)
        return visitatori_trend, giorni
        
    def creazione_dataframe(self,visitatori_trend, giorni):
        data = {"Indice": giorni,
                "Numero Visitatori":visitatori_trend,
                }
        self.df = pd.DataFrame(data)
        self.df.set_index('Indice', inplace=True)
        print(self.df)
        return self.df
    
    def statistiche(self):  
        media = self.df.resample('ME').mean()
        deviazione_standard = self.df.resample('ME').std().astype(int)
        print(media)
        print(f"\n La deviazione standard Ã¨: {deviazione_standard}")
        return media

    def grafico_linee(self,giorni,visitatori_trend):
      
        plt.figure(figsize=(12, 6))

        plt.plot(visitatori_trend,giorni)

        plt.title('Numero di visitatori giornaliero')

        plt.xlabel('Giorni')

        plt.ylabel('Visitatori')

        plt.show()
    
    def grafico_media_mobile(self):
        
        media_mobile = self.df['Numero Visitatori'].rolling(window=7).mean()
        plt.figure(figsize=(12, 6))
        plt.plot(self.df.index, media_mobile, color='red')
        plt.plot(self.df.index, self.df['Numero Visitatori'],  color='blue')

        plt.title('Media Mobile dei Visitatori Giornalieri')
        plt.xlabel('Giorni')
        plt.ylabel('Visitatori')
        plt.legend()
        plt.show()

    def grafico_media(self,media):

        mese = [1,2,3,4,5,6,7,8,9,10,11,12]

        plt.figure(figsize=(12, 6))

        plt.plot(mese,media)

        plt.title('Media di visitatori mensile')

        plt.xlabel('Mese')

        plt.ylabel('Visitatori')

        plt.show()


gestione = Gestionedati()
visitatori_trend,giorni = gestione.generazione_dati()
df = gestione.creazione_dataframe(visitatori_trend,giorni)
media = gestione.statistiche()
gestione.grafico_linee(visitatori_trend,giorni)
gestione.grafico_media(media)
gestione.grafico_media_mobile()