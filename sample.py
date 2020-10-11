import os

import pandas as pd
from azure.storage.blob import BlobServiceClient

connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
blob_service_client = BlobServiceClient.from_connection_string(connect_str)


def main():
    df = pd.DataFrame(
        {'fruits': ['banana', 'orange', 'apple'], 'price': [100, 150, 170]})
    print(df)
    blob_client = blob_service_client.get_blob_client(
        container='sample', blob='sample.csv')
    output = df.to_csv(index=False)
    blob_client.upload_blob(output)


if __name__ == '__main__':
    main()
