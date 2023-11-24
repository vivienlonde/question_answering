from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
import json

with open('config_aai_search.json', 'r') as file:
    config_aai = json.load(file)

service_endpoint = config_aai['AZURE_SEARCH_SERVICE_ENDPOINT']
index_name = config_aai['AZURE_SEARCH_INDEX_NAME']
key = config_aai['AZURE_SEARCH_ADMIN_KEY']

search_client = SearchClient(service_endpoint, index_name, AzureKeyCredential(key))



index_name = "hotels"

client = SearchIndexClient(service_endpoint, AzureKeyCredential(key))
name = "hotels"
fields = [
    SimpleField(name="hotelId", type=SearchFieldDataType.String, key=True),
    SimpleField(name="baseRate", type=SearchFieldDataType.Double),
    SearchableField(name="description", type=SearchFieldDataType.String, collection=True),
    ComplexField(
        name="address",
        fields=[
            SimpleField(name="streetAddress", type=SearchFieldDataType.String),
            SimpleField(name="city", type=SearchFieldDataType.String),
        ],
        collection=True,
    ),
]
cors_options = CorsOptions(allowed_origins=["*"], max_age_in_seconds=60)
scoring_profiles: List[ScoringProfile] = []
index = SearchIndex(name=name, fields=fields, scoring_profiles=scoring_profiles, cors_options=cors_options)

result = client.create_index(index)