import os, json
import pandas as pd
import glob
pd.set_option('display.max_columns', None)

transactions = pd.DataFrame()

path_to_json = r'C:\Users\Zipla\Desktop\FORMS 2023\Revolve Solutions - Python Assignment\input_data\starter\transactions/*' 

json_pattern = os.path.join(path_to_json,'*.json')
file_list = glob.glob(json_pattern)

for file in file_list:
    data = pd.read_json(file, lines=True)
    transactions = pd.concat([transactions,data])
    

