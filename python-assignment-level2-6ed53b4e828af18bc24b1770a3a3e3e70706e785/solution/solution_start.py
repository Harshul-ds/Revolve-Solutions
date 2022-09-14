import argparse
import os
from cgi import print_arguments
import pandas as pd
import glob

def get_params() -> dict:
    parser = argparse.ArgumentParser(description='DataTest')
    parser.add_argument('--customers_location', required=False, default="../input_data/starter/customers.csv")
    parser.add_argument('--products_location', required=False, default="../input_data/starter/products.csv")
    parser.add_argument('--transactions_location', required=False, default= r'..\input_data\starter\transactions/*')
    parser.add_argument('--output_location', required=False, default="./output_data/outputs/")
    return vars(parser.parse_args())

def transactions(path_to_json) -> pd.DataFrame:
    transactions = pd.DataFrame()
    json_pattern = os.path.join(path_to_json,'*.json')
    file_list = glob.glob(json_pattern)

    for file in file_list:
        data = pd.read_json(file, lines=True)
        transactions = pd.concat([transactions,data])
    
    return transactions


def read_csv(customers_location, products_location) -> pd.DataFrame:
    customers = pd.read_csv(customers_location)
    products = pd.read_csv(products_location)
    return customers, products

def return_output(customers, products, transactions):
    if not isinstance(customers, pd.DataFrame) or not isinstance(products, pd.DataFrame) or not isinstance(transactions, pd.DataFrame):
        raise Exception("Input data is not a pandas DataFrame")
    transactions = transactions.groupby(['customer_id','date_of_purchase']).sum().reset_index()
    transactions['purchase_count'] = transactions['basket'].apply(lambda x: len(x))
    transactions = transactions.explode('basket').reset_index(drop=True)
    transactions = transactions.join(pd.json_normalize(transactions['basket']))
    transactions = transactions.drop(['price','basket'], axis=1)
    transactions = pd.merge(transactions,products, on='product_id')
    transactions = pd.merge(transactions,customers, on='customer_id').reset_index(drop=True)
    transactions = transactions.drop(['product_description','purchase_count'], axis=1)
    transactions = transactions.groupby(['customer_id','product_id','product_category','loyalty_score']).agg({'date_of_purchase':'count'}).reset_index()
    transactions = transactions.rename(columns={'date_of_purchase':'purchase_count'})
    transactions = transactions[['customer_id','loyalty_score','product_id','product_category','purchase_count']]
    return transactions


def sort_output(output):
    # sort output by customer_id
    idx = (output.assign(customer_id=output.customer_id.str.extract(r'(\d+)$').astype(int))
         .sort_values(['customer_id'])
         .index)

    output = output.iloc[idx]
    return output


def main():
    params = get_params()
    customers , products = read_csv(params['customers_location'],params['products_location'])
    transaction = transactions(params['transactions_location'])
    output = return_output(customers, products, transaction)
    output = sort_output(output)
    output.to_json(params['output_location'] + 'output.json', orient='records')
    return output




    

if __name__ == "__main__":
    main()
