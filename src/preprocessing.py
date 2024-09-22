import pandas as pd

def load():
    dataset=pd.read_csv('../data/MiningProcess_Flotation_Plant_Database.csv')
    return dataset

def preprocess(df):
    
    #cleans the data if there any null values
    if (df.isnull().sum().any()):
        df=df.dropna()
    
    #coverts the date column as datetime format    
    for i in df.columns:
        if (i == 'date'):
            df[i]=pd.to_datetime(df[i])
            
    #replaces the symbol ',' with '.'        
    df=df.apply(lambda x: x.str.replace(',', '.') if x.dtype == "object" else x)
    
    #changing the object datatype to float
    df=df.apply(lambda x: x.astype(float) if x.dtype == "object" else x)
    
    #this rounds the values in columns to two decimal places except date column
    for m in df.columns:
        if (m != 'date'):
            df[m]=df[m]  
        
    return df
