import Pandas_EsercizioFinale as ef
import pandas as pd

class Pulizia():
    def elimina_dati_mancanti(self,ef.df):
        ef.df.dropna(subset=['ID_Cliente'])
    def imputa_dati_mancanti(self,ef.df):
        imputa = ef.df.copy()
        imputa['Durata_Abbonamento'].fillna(ef.df['Durata_Abbonamento'].mean(), inplace=True)
        print(imputa)


pulito = Pulizia()
pulito.elimina_dati_mancanti()
