pip install requests_oauthlib
pip install msal

from airflow import DAG
from airflow.operators.python import PythonOperator
import msal
from datetime import date
import pandas as pd
import requests
import pyodbc

def captura_token():
    #Buscar token 
    # Enter the details of your AAD app registration
    client_id = 'client_id'
    client_secret = 'client_secret'
    authority = 'authority'
    scope = ['https://graph.microsoft.com/.default']

    # Create an MSAL instance providing the client_id, authority and client_credential parameters
    client = msal.ConfidentialClientApplication(client_id, authority=authority, client_credential=client_secret)
    
    # First, try to lookup an access token in cache
    token_result = client.acquire_token_silent(scope, account=None)

    # If the token is available in cache, save it to a variable
    if token_result:
        access_token = 'Bearer ' + token_result['access_token']

    # If the token is not available in cache, acquire a new one from Azure AD and save it to a variable
    if not token_result:
        token_result = client.acquire_token_for_client(scopes=scope)
        access_token = 'Bearer ' + token_result['access_token']

    PARAMETRO = { 'authorization':  access_token ,
                                'Accept': 'application/json;odata.metadata=minimal;odata.streaming=true',
                                'Content-Type': 'application/json;odata.metadata=minimal;odata.streaming=true'}
    #print(PARAMETRO)
    return PARAMETRO 

def captura_dados():
    PARAMETRO = ti.xcom_pull(task_ids = 'captura_token')

    hoje= date.today()
    dtatual=str(hoje)
    API_URI = "https://graph.microsoft.com/v1.0/auditLogs/signIns?$filter=(createdDateTime ge "+(dtatual)+"T00:00:00Z AND createdDateTime le "+(dtatual)+"T23:59:00Z)"
    api_LOG_response = requests.get(API_URI, headers=PARAMETRO)

    data= api_LOG_response.json()
    df_LOG = pd.json_normalize(data,record_path=['value'])
    df_LOG.columns = (df_LOG.columns.str.replace('.', ''))
    df= df_LOG

    server = 'ip_servidor'
    database = 'banco_dados' 
    username = 'usuario' 
    password = 'senha' 
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    # Insert Dataframe into SQL Server:
    for index, row in df.iterrows():
        cursor.execute("INSERT INTO tabela (coluna_tabela,coluna_tabela,coluna_tabela) values(?,?,?)",row.colunadf,row.colunadf,row.colunadf)
    cnxn.commit()
    cursor.close()
    return dfL


with DAG(
        'dag_nome',
        start_date=datetime(year=2023, month=5, day=25), 
        schedule_interval='55 23 * * *',   #vai rodar todo dia as 23:55
        ) as dag:
    captura_token = PythonOperator(
            task_id = 'captura_token',
            python_callable = captura_token
            )
    captura_dados = PythonOperator(
            task_id = 'captura_dados',
            python_callable = captura_dados
            )

captura_token >> captura_dados