import openai
import os

openai_api_key = os.getenv('OPENAI_API_KEY')

fine_tune_id = os.getenv('FINE_TUNE_ID')

fine_tune = openai.FineTune.retrieve(fine_tune_id)

print(fine_tune)