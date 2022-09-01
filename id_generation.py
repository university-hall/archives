import pandas as pd
from archivepy.GenerateID import generate_uuid

archives = pd.read_csv('archives/data/101_suggestion_book.csv', 
                       dtype={'year': str})

archives['start_date'] = pd.to_datetime(archives['start_date'], format='%Y-%m-%d')
archives['end_date'] = pd.to_datetime(archives['end_date'], format='%Y-%m-%d')

archives['year'] = archives['end_date'].dt.year

archives['year'] = pd.to_datetime(archives['year'], 
                                  format='%Y') # assign the datatype to datetime

archives = generate_uuid(archives)

archives.to_csv('archives/data/101_suggestion_book.csv', index=False)
