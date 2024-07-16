import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente
load_dotenv()

# Lista de commodities
commodities = ['CL=F', 'GC=F', 'SI=F']

# Variáveis de conexão com o banco de dados
DB_HOST = os.getenv('DB_HOST_PROD')
DB_PORT = os.getenv('DB_PORT_PROD')
DB_NAME = os.getenv('DB_NAME_PROD')
DB_USER = os.getenv('DB_USER_PROD')
DB_PASS = os.getenv('DB_PASS_PROD')
DB_SCHEMA = os.getenv('DB_SCHEMA_PROD')

# URL de conexão com SSL habilitado
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}?sslmode=require"

# Criar engine de conexão
engine = create_engine(DATABASE_URL)

def search_data(symbol, period='5d', interval='1d'):
    ticker = yf.Ticker(symbol)
    data = ticker.history(period=period, interval=interval)[['Close']]
    data['symbol'] = symbol
    return data

def search_all_data(commodities):
    all_data = []
    for symbol in commodities:
        data = search_data(symbol)
        all_data.append(data)
    return pd.concat(all_data)

def load_data(df, schema='DB_SCHEMA'):
    df.to_sql('commodities', engine, schema=schema, if_exists='replace', index=True)

if __name__ == '__main__':
    data_concat = search_all_data(commodities)
    load_data(data_concat, schema=DB_SCHEMA)