import pandas as pd
import sqlalchemy 

username, password = 'admin', 'mypassword'
server, database = 'database-1.cfhky9n7snkd.us-east-1.rds.amazonaws.com/ssl_ca=rds-combined-ca-bundle.pem', 'attacks_db'
ssl_args = {'ssl': {'ca': '/Users/mdrozdov/Downloads/rds-ca-2015-root.pem'}}

engine_stmt = f'mysql+mysqldb://{username}:{password}@{server}:3306/{database}'

engine = sqlalchemy.create_engine(engine_stmt, connect_args = ssl_args)

df = pd.read_csv('data/attacks1_1.csv')

df.to_sql(name = 'attacks1', con = engine,
          if_exists = 'append', index = False, chunksize = 1000)
