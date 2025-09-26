
import json

def transform_product_data(products_str, prices_str):
    products = products_str.split(',')
    prices = map(float, prices_str.split(','))
    

    product_data = zip(products, prices)
    

    valid_products = filter(lambda x: x[1] > 0, product_data)
    transformed_products = list(map(lambda x: {
        'product': x[0],
        'price': x[1],
        'discounted': x[1] * 0.9
    }, valid_products))
    

    with open('products.json', 'w') as file:
        json.dump(transformed_products, file, indent=4)
    
    return transformed_products[:5]  
