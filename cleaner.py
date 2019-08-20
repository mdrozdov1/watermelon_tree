from helper import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
import csv

for i in range(1,2):
    attacks = pd.read_csv(f'/Users/mdrozdov/Documents/watermelon_tree/data/attacks{i}.csv')
    attacks_new = attacks_cleaner(attacks, './labels.txt', for_csv = True)
    del attacks
    
    with open(f'/Users/mdrozdov/Documents/watermelon_tree/data/attacks{i}_1.csv', mode = 'w') as file:
        data_writer = csv.writer(file, delimiter = ',')
        
        data_writer.writerow(attacks_new.columns.tolist())
        
        for row in range(len(attacks_new)):
            data_writer.writerow(attacks_new.iloc[row].tolist())
        
    del attacks_new
    


