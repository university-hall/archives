import pandas as pd
from archivepy.GenerateID import generate_uuid

archives = pd.read_csv('./data/1_archives.csv', dtype={'year': str})
archives['year'] = pd.to_datetime(archives['year'], format='%Y') # assign the datatype to datetime

archives = generate_uuid(archives)

archives.to_csv('./data/1_archives.csv', index=False)
