import sys
sys.path.append('./python-assignment-level2-6ed53b4e828af18bc24b1770a3a3e3e70706e785/solution/')

from solution_start import return_output, transactions, sort_output

import pandas as pd
def test_sort_output():
    customers = pd.read_csv('../input_data/starter/customers.csv')
    products = pd.read_csv('../input_data/starter/products.csv')
    transaction = transactions(r'..\input_data\starter\transactions/*')
    fn_output = sort_output(return_output(customers, products, transaction)).reset_index(drop=True)
    output = pd.read_json('./output_data/outputs/output.json', orient='records')
    assert output.equals(fn_output)

    