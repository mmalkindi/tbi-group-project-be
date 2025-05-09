import csv
from elasticsearch import Elasticsearch, helpers
import os
from tqdm import tqdm
from dotenv import load_dotenv

load_dotenv()
search_host = os.getenv('SEARCH_HOST', 'localhost:9200')

es = Elasticsearch(
    search_host,
    headers={"Accept": "application/vnd.elasticsearch+json; compatible-with=8",
             "Content-Type": "application/vnd.elasticsearch+json; compatible-with=8"}
)

def generate_docs():
    csv_path = os.path.join(os.path.dirname(__file__), ".", "airports.csv")
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for i, row in tqdm(enumerate(reader), desc="Indexing airports", unit="rows", total=76365):
            yield {
                "_index": "airports",
                "_id": i,
                "_source": {
                    "name": row.get("name"),
                    "icao_code": row.get("ident"),
                    "iata_code": row.get("iata_code"),
                    "gps_code": row.get("gps_code"),
                    "local_code": row.get("local_code"),
                    "type": row.get("type"),
                    "iso_country": row.get("iso_country"),
                    "latitude_deg": float(row.get("latitude_deg") or 0),
                    "longitude_deg": float(row.get("longitude_deg") or 0),
                    "elevation_ft": float(row.get("elevation_ft") or 0),
                }
            }

def bulk_index():
    helpers.bulk(es, generate_docs())
    print("✅ Bulk indexing complete.")

if __name__ == "__main__":
    print(os.getenv('SEARCH_HOST'))
    bulk_index()
