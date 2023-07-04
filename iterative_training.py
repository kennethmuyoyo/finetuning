import openai
import os

openai_api_key = os.getenv('OPENAI_API_KEY')

fine_tune_id = os.getenv('FINE_TUNE_ID')
n_epochs = 16  

fine_tune = openai.FineTune.retrieve(fine_tune_id)

new_fine_tune = openai.FineTune.create(
    model="davinci",
    training_file=fine_tune["training_files"][0]["id"],
    validation_file=fine_tune["validation_files"][0]["id"],
    n_epochs=n_epochs,
    batch_size=fine_tune["hyperparams"]["batch_size"],
    learning_rate_multiplier=fine_tune["hyperparams"]["learning_rate_multiplier"]
)

print("New Fine-tuning ID:", new_fine_tune["id"])

