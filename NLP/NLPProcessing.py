import pandas as pd 
df = pd.read_csv('C:/Users/MFBA/Documents1/big data dp project/Dataset/out.csv')
data =pd.DataFrame()
data['class'] = df['recommendation']
data['review'] = df['review']
 