import pandas as pd
import numpy as np

def parse_csv(csv):
    return identify_type(csv)


def identify_type(csv):
    colunas_conta = {'date', 'title', 'amount'}
    colunas_cartao = {'Data', 'Valor', 'Identificador', 'Descrição'}

    df_csv = pd.read_csv(csv, sep=',', header=0)

    if not (colunas_conta.issubset(df_csv.columns) or colunas_cartao.issubset(df_csv.columns)):
        raise ValueError("Formato de CSV não reconhecido")
    
    if 'date' in df_csv.columns:
        df = parse_credit(df_csv)
    else:
        df = parse_conta(df_csv)
    

    return df

def parse_credit(df_csv):
    df = df_csv.rename(columns={'title': 'description'})
    df['date'] = pd.to_datetime(df['date'], format="%Y-%m-%d")
    df['amount'] = pd.to_numeric(df['amount'])
    df['type'] = np.where(df['amount'] < 0, 'expense', 'income')
    df['origin'] = 'csv'

    return df.to_dict("records")

def parse_conta(df_csv):
    
    df = df_csv.drop('Identificador', axis=1)
    df = df.rename(columns={'Data': 'date', 'Valor': 'amount', 'Descrição': 'description'})
    df['date'] = pd.to_datetime(df['date'], format="%d/%m/%Y")
    df['amount'] = pd.to_numeric(df['amount'])
    df['type'] = np.where(df['amount'] < 0, 'expense', 'income')
    df['origin'] = 'csv'

    return df.to_dict("records")



