import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

### load all the labels present across datasets

def labels_reader(path_to_labels):
    with open(f'{path_to_labels}', 'r') as file:
        lines = file.readlines()
    lines = [item.strip() for item in lines if item.strip() != 'Label']
    lines = list(enumerate(sorted(lines)))
    
    return lines


### implement sklearn simple imputation on loaded dataset

def my_imputer(df, simple = True):
    if isinstance(df, pd.DataFrame):
        imp_mean = SimpleImputer(missing_values = np.nan,
                                strategy = 'mean')
        for column in df.columns:
            arr = np.array(df[column]).reshape(-1,1)
            df[column] = imp_mean.fit_transform(arr)
        
        return df
    
    else:
        imp_class = SimpleImputer(missing_values = np.nan,
                                strategy = 'most_frequent')
        df = imp_class.fit_transform(np.array(df).reshape(-1,1))

        return df


### cleaner function implementing the entire cleaning process including
### label check and imputation

def attacks_cleaner(DF, path_to_labels, for_csv = False):
    X_df = DF.drop(['Timestamp','Label'],axis=1)
    Y_df = DF.Label
    
    types_list = labels_reader(path_to_labels)
    
    for column in X_df.columns:
        X_df[column] = np.where(X_df[column] == f'{column}', np.nan, X_df[column])
        try:
            X_df[column] = np.where(np.isinf(X_df[column]),np.nan, X_df[column])
        except:
            X_df[column] = list(map(lambda x: float(x), X_df[column]))
            X_df[column] = np.where(np.isinf(X_df[column]),np.nan, X_df[column])
    
    for tup in types_list:
        Y_df = np.where(Y_df == tup[1],tup[0], Y_df)
    
    Y_df = np.where(Y_df == 'Label', np.nan, Y_df)
        
    if for_csv:
        X_df = my_imputer(X_df)
        X_df['Label'] = my_imputer(Y_df)
        return X_df
    
    else:
        X_df = my_imputer(X_df)
        Y_df = my_imputer(Y_df)
        return X_df, Y_df







