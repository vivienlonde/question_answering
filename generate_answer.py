from openai import AzureOpenAI
import json


with open('config_aoai.json', 'r') as file:
   config_aoai = json.load(file)

aoai_completion = config_aoai['AZURE_OPENAI_COMPLETION']
aoai_endpoint = config_aoai['AZURE_OPENAI_ENDPOINT']
aoai_key = config_aoai['AZURE_OPENAI_API_KEY'] 

client = AzureOpenAI(
  api_key=aoai_key,  
  api_version="2023-10-01-preview",
  azure_endpoint=aoai_endpoint
)


def get_answer(question):

    prompt = question

    response = client.chat.completions.create(model=aoai_completion, messages=[{"role": "system", "content":prompt}])
    response = response.choices[0].message.content
    
    return response



if __name__ == "__main__":
  question = "How many GPUs are there in Azure?"
  answer = get_answer(question)
  print(answer)
