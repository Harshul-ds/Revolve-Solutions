from solution_start import return_output, transactions, sort_output

import pandas as pd
def test_return_output():
    customers = pd.read_csv('../input_data/starter/customers.csv')
    products = pd.read_csv('../input_data/starter/products.csv')
    transaction = transactions(r'..\input_data\starter\transactions/*')
    # with open('test/output_6_months.json') as f:
    #     output = pd.read_json(f,orient='records', lines= True)
    fn_output = sort_output(return_output(customers, products, transaction))
    assert output.equals(fn_output)
    