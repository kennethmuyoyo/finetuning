import openai
import os

openai_api_key = os.getenv('OPENAI_API_KEY')

question_choice = input("question_choice: ")

prompt = f"Category: {question_choice}"
response = openai.Completion.create(
    model='curie:ft-personal-2023-07-02-02-49-33',
    prompt=prompt,
    max_tokens=200,  
    n=1,  
    stop="END",  
    temperature=1,  
    top_p=1,  
)

generated_text = response.choices[0].text.strip()
generated_text = generated_text.rstrip(" -> END")  # Remove the suffix ending from the generated text
print(generated_text)