import argparse
from cgi import print_arguments
import pandas as pd



def get_params() -> dict:
    parser = argparse.ArgumentParser(description='DataTest')
    parser.add_argument('--customers_location', required=False, default="./input_data/starter/customers.csv")
    parser.add_argument('--products_location', required=False, default="./input_data/starter/products.csv")
    parser.add_argument('--transactions_location', required=False, default="./input_data/starter/transactions/")
    parser.add_argument('--output_location', required=False, default="./output_data/outputs/")
    return vars(parser.parse_args())



def read():
    customers = pd.read_csv('customer_location')
    products = pd.read_csv('products_location')



def main():
    params = get_params()
    
    

if __name__ == "__main__":
    main()
