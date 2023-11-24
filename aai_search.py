import json
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential

with open('config_aai_search.json', 'r') as file:
    config_aai = json.load(file)

service_endpoint = config_aai['AZURE_SEARCH_SERVICE_ENDPOINT']
index_name = config_aai['AZURE_SEARCH_INDEX_NAME']
key = config_aai['AZURE_SEARCH_ADMIN_KEY']
credential = AzureKeyCredential(key)

with open('data/test.json', 'r') as file:  
    documents = json.load(file)

print(documents[0]['text'])

search_client = SearchClient(endpoint=service_endpoint, index_name=index_name, credential=credential)
result = search_client.upload_documents(documents)
print(f"Uploaded {len(documents)} documents") 