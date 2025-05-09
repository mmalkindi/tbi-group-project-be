from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

def create_airports_index():
    es.indices.create(
        index="airports",
        body={
            "mappings": {
                "properties": {
                    "name": {"type": "text"},
                    "city": {"type": "text"},
                    "country": {"type": "keyword"},
                    "iata_code": {"type": "keyword"},
                    "latitude": {"type": "float"},
                    "longitude": {"type": "float"},
                }
            }
        },
        ignore=400
    )
    print("✅ Index created or already exists.")

if __name__ == "__main__":
    create_airports_index()
