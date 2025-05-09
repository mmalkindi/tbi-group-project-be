# Indexing for TBing Search

> Muhamad Rifqi - `2206081433`  
> Muhammad Milian Alkindi - `2206081856`  
> Fatih Raditya Pratama - `2206083520`

## Indexing Procedure

1. Install required libraries

    ```bash
    pip install -r requirements.txt
    ```

2. Create a `.env` file in the root directory with the following content:

    ```env
    SEARCH_HOST=http://localhost:9200  ## Change this to your Elasticsearch host
    ```

3. Run bulk indexing

    ```bash
    python .\bulk_index_airports.py
    ```
