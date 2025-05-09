import pandas as pd
from elasticsearch import Elasticsearch, helpers

# Elasticsearch connection
es = Elasticsearch("http://localhost:9200")  # Replace with your Elasticsearch URL

# Index name
INDEX_NAME = "airports"

# Read the CSV file
csv_file = "airports.csv"  # Replace with the path to your CSV file
df = pd.read_csv(csv_file)

# Extract required fields: name, iso_country, and municipality
df = df[["name", "iso_country", "municipality"]]

# Prepare data for bulk indexing
def generate_bulk_data(df, index_name):
    for _, row in df.iterrows():
        yield {
            "_index": index_name,
            "_source": {
                "name": row["name"],
                "iso_country": row["iso_country"],
                "municipality": row["municipality"],
            },
        }

# Perform bulk indexing
try:
    helpers.bulk(es, generate_bulk_data(df, INDEX_NAME))
    print(f"Data successfully indexed into Elasticsearch index '{INDEX_NAME}'")
except Exception as e:
    print(f"Error during bulk indexing: {e}")