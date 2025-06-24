# Import libraries
from airflow.models import DAG
from airflow.operators.python import PythonOperator
from datetime import timedelta
import datetime as dt
from sqlalchemy import create_engine
from elasticsearch import Elasticsearch
import pandas as pd

# Reads a CSV file and uploads to a PostgreSQL database
def load_csv_to_postgres():
    database = "airflow"
    username = "airflow"
    password = "airflow"
    host = "postgres"

    # Create URL to PostgreSQL
    postgres_url = f"postgresql+psycopg2://{username}:{password}@{host}/{database}"

    # Create URL to SQLAlchemy
    engine = create_engine(postgres_url)
    conn = engine.connect()
    df = pd.read_csv('/opt/airflow/dags/P2M3_nathanael_data_raw.csv')
    df.to_sql('table_m', conn, index=False, if_exists='replace')

# Connects to a PostgreSQL database using SQLAlchemy
def fetch_data():
    engine = create_engine("postgresql+psycopg2://airflow:airflow@postgres/airflow")
    conn = engine.connect()
    df = pd.read_sql_query("SELECT * FROM table_m", conn)
    df.to_csv('/opt/airflow/dags/P2M3_nathanael_data_raw.csv', sep=',', index=False)

# Data Cleaning the CSV File 
def P2M3_nathanael_data_clean():
    df_goods = pd.read_csv('/opt/airflow/dags/P2M3_nathanael_data_raw.csv')
    # Remove duplicate data
    df_goods.drop_duplicates(inplace=True)
    # All columns name are using lower case
    df_goods.columns = [x.lower() for x in df_goods.columns]
    # Changing spaces and special characters into underscore
    df_goods.columns = df_goods.columns.str.strip().str.replace(' ', '_').str.replace('/', '_', regex=False)
    # Changing date type columns to datetime
    df_goods['manufacturing_date'] = pd.to_datetime(df_goods['manufacturing_date'], format='%m/%d/%Y %H:%M')
    df_goods['expiration_date'] = pd.to_datetime(df_goods['expiration_date'], format='%m/%d/%Y %H:%M')
    # Handling missing value
    df_goods.dropna(inplace=True)
    # Saving cleaned data
    df_goods.to_csv('/opt/airflow/dags/P2M3_nathanael_data_clean.csv', index=False)

# Reads a CSV file, converts each row to a dictionary, and indexes the data into an Elasticsearch index named "table_new"
def upload_to_elasticsearch():
    es = Elasticsearch("http://elasticsearch:9200")
    df = pd.read_csv('/opt/airflow/dags/P2M3_nathanael_data_clean.csv')
    
    for i, r in df.iterrows():
        doc = r.to_dict()
        res = es.index(index="table_new", id=i + 1, body=doc)
        print(f"Response from Elasticsearch: {res}")

# Defines an Airflow DAG named "M3CleanData" with a schedule to run at 09:10 AM until 09:30 AM every Saturday.
default_args = {
    'owner': 'nathan',
    'start_date': dt.datetime(2024, 11, 2, 9, 10) - timedelta(hours=7),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

with DAG('M3CleanData',
         default_args=default_args,
         schedule_interval='10,20,30 9 * * 6'  # At 09:10, 09:20, and 09:30 every Saturday
         ) as dag:

    # Task
    load_csv_task = PythonOperator(
        task_id='load_csv_to_postgres',
        python_callable=load_csv_to_postgres)

    # Task: 1
    ''' Function to fetch data from PostgreSQL. '''
    fetching_data = PythonOperator(
        task_id='fetching_data',
        python_callable=fetch_data)

    # Task: 2
    ''' Function to clean data. '''
    edit_data = PythonOperator(
        task_id='edit_data',
        python_callable=P2M3_nathanael_data_clean)

    # Task: 3
    ''' Function to upload data into Elasticsearch. '''
    upload_data = PythonOperator(
        task_id='upload_data_elastic',
        python_callable=upload_to_elasticsearch)

    # The sequence of tasks in the Airflow:
    load_csv_task >> fetching_data >> edit_data >> upload_data
