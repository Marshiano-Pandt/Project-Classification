import pandas as pd
from sklearn.model_selection import train_test_split

def prep_iris(df):
    """
    Drop and rename columns to clean data.
    """
    df = df.drop(columns=['species_id', 'measurement_id'])
    df = df.rename(columns={'species_name':'species'})
    
    return df



def prep_telco(df):
    '''
    Columns were dropped because they represented in another column, 
    total_charges whitespace was converted to 0, 
    null values were replaced to no internet service,
    total charges were changesd to a float,
    filled the null value to a value of None.
    clean the data. 
    '''
    df = df.drop(columns= ['payment_type_id', 'internet_service_type_id', 'contract_type_id', 'customer_id'])
    df.total_charges = df.total_charges.str.replace(' ', '0.0')
    df.internet_service_type = df.internet_service_type.fillna(value='No internet service')
    df.total_charges = df.total_charges.astype(float)
    df.internet_service_type = df.internet_service_type.fillna(value='None')
    
    return df



def splitting_data(df, col):
    '''
    splitting the data to seperate to explore and validate the dataframe.
    '''
    #first split
    train, validate_test = train_test_split(df, 
                                            train_size=0.6,
                                            random_state=123,
                                            stratify=df[col]
                                           )
    
    validate, test = train_test_split(validate_test,
                                      train_size=0.5,
                                      random_state=123,
                                      stratify=validate_test[col]
                                      
                                     )
    return train, validate, test



def clean_titanic(df):
    """
    drop columns, changed string to an object to make it categorical, and chnaged the nas to have a value. 
    """
    #drop unncessary columns
    df = df.drop(columns=['embarked', 'age','deck', 'class'])
    
    #made this a string so its categorical
    df.pclass = df.pclass.astype(object)
    
    #filled nas with the mode
    df.embark_town = df.embark_town.fillna('Southampton')
    
    return df





def preprocess_telco(train_df, val_df, test_df):
    '''
    preprocess_telco will take in three pandas dataframes
    of our telco data, expected as cleaned versions of this 
    titanic data set (see documentation on acquire.py and prepare.py)
    
    output:
    encoded, ML-ready versions of our clean data, with 
    columns:[gender, partner, dependents, phone_service, 
    phone_service, multiple_lines, online_security, 
    online_backup, device_protection, tech_support, 
    streaming_tv', streaming_movies, paperless_billing, churn, 
    contract_type, internet_service_type, payment_type] in  encoded.
    return: (pd.DataFrame, pd.DataFrame, pd.DataFrame)
    '''
   
    encoded_dfs = []
    for df in [train_df, val_df, test_df]:
        df_encoded_cats = pd.get_dummies(df.drop(columns=['senior_citizen', 'tenure', 'total_charges', 'monthly_charges']),
              drop_first=True).astype(int)
        encoded_dfs.append(pd.concat(
            [df,
            df_encoded_cats],
            axis=1).drop(columns=['gender', 'partner', 'dependents', 'phone_service', 'phone_service',
                                  'multiple_lines', 'online_security', 'online_backup', 'device_protection',
                                  'tech_support', 'streaming_tv', 'streaming_movies', 'paperless_billing', 'churn',
                                  'contract_type', 'internet_service_type', 'payment_type']))
    return encoded_dfs

