from pdfminer.high_level import extract_text
from openai import AzureOpenAI
import json
import numpy as np

with open('config_aoai.json', 'r') as file:
   config_aoai = json.load(file)

aoai_embedding = config_aoai['AZURE_OPENAI_EMBEDDING']
aoai_endpoint = config_aoai['AZURE_OPENAI_ENDPOINT']
aoai_key = config_aoai['AZURE_OPENAI_API_KEY'] 

client = AzureOpenAI(
  api_key = aoai_key,  
  api_version = "2023-05-15",
  azure_endpoint = aoai_endpoint
)

def compute_vector(text):
  response = client.embeddings.create(
    input=text,
    model=aoai_embedding
  )
  vector = response.data[0].embedding
  return vector
   
def get_text_from_pdf(pdf_path):
  text = extract_text(pdf_path)
  # with open('data/example.txt', 'w', encoding='utf-8') as f:
  #     f.write(text)
  # with open('data/example.txt', 'r', encoding='utf-8') as f:
  #     text = f.read()
  return text


def compute_embedding(pdf_path):
  text = extract_text(pdf_path)
  embeddings = []
  length = len(text)
  nb_of_letters_per_chunk = 1000
  i = 0
  while nb_of_letters_per_chunk * i < length:
      if nb_of_letters_per_chunk * (i+1) < length:
        embeddings.append(compute_vector(text[nb_of_letters_per_chunk * i: nb_of_letters_per_chunk * (i + 1)]))
      else:
        embeddings.append(compute_vector(text[nb_of_letters_per_chunk * i:]))
      i += 1
  np.save('data/example.npy', embeddings)
  # embeddings = np.load('data/example.npy')  
  return len(embeddings)















