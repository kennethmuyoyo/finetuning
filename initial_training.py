import openai
import os
from pprint import pprint

openai_api_key = os.getenv('OPENAI_API_KEY')

def file_upload(filename, purpose='fine-tune'):
    resp = openai.File.create(purpose=purpose, file=open(filename))
    pprint(resp)
    return resp

def finetune_model(training_file_id, validation_file_id, suffix='doctor', model='davinci', n_epochs=10, batch_size=4, learning_rate_multiplier=0.5):
    fine_tune = openai.FineTune.create(
        model=model,
        training_file=training_file_id,
        validation_file=validation_file_id,
        suffix=suffix,
        n_epochs=n_epochs,
        batch_size=batch_size,
        learning_rate_multiplier=learning_rate_multiplier
    )
    print("Fine-tuning ID:", fine_tune["id"])

training_resp = file_upload('output_prepared.jsonl')
validation_resp = file_upload('validation.jsonl')

finetune_model(training_resp['id'], validation_resp['id'], 'doctor', 'davinci')

# Now use that file when fine-tuning:
# > openai api fine_tunes.create -t "output_prepared.jsonl"

# After you’ve fine-tuned a model, remember that your prompt has to end with the indicator string `\n\n###\n\n` for the model to start generating completions, rather than continuing with the prompt. Make sure to include `stop=[" END"]` so that the generated texts ends at the expected place.
# Once your model starts training, it'll approximately take 1.1 days to train a `curie` model, and less for `ada` and `babbage`. Queue will approximately take half an hour per job ahead of you.
