from pandas import read_excel, DataFrame

filename = input('Enter the filename: ')
filepath = 'archives/data/' + filename

df = read_excel(filepath, 
                dtype={'year': str})

df.to_csv(filepath.replace('.xlsx', '.csv'), 
          index=False)

