import pandas as pd
import uuid

def generate_uuid(dataframe: pd.DataFrame):
    for i in range(len(dataframe)):
        if dataframe.iloc[i]['uuid'] is None:
            dataframe.iloc[i]['uuid'] = str(uuid.uuid1(dataframe.iloc[i]['year']))
            
    return dataframe
