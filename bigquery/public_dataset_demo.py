from google.cloud import bigquery

def query_public_dataset():
    client = bigquery.Client()

    query = """
            SELECT order_items.id, order_id, product_id, name
            from `bigquery-public-data.thelook_ecommerce.order_items` AS order_items
            JOIN `bigquery-public-data.thelook_ecommerce.products` AS products
            ON order_items.product_id = products.id
    """
    results = client.query(query).to_dataframe()[:10]  # Get the first 10 results

    print(results)

if __name__ == "__main__": 
    query_public_dataset()