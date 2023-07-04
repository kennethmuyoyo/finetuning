import pandas as pd
import ast
import json

def find_answer(options, correct_choices):
    options = options.replace(",:", ":")  # replace the misplaced comma
    options_list = ast.literal_eval(options)
    answers = ""
    for option_dict in options_list:
        for key, value in option_dict.items():
            if key in correct_choices:
                answers += f"{key}: {value}, "
    return answers.rstrip(', ')  # remove trailing comma and space


# Load dataframe
df = pd.read_excel('doctor_set.xlsx')

# Define the 'Answer' column
df['Answer'] = df.apply(lambda x: find_answer(x['选择题可选项/填空问答题得分点'], x['答案'].strip('[]"')), axis=1)

# Creating 'Prompt' and 'Completion' pairs
data = []
for index, row in df.iterrows():
    pair = {}
    pair["prompt"] = row['题目'] + "/nchoices:" + row['选择题可选项/填空问答题得分点'].replace(",:", ":")
    pair["completion"] = row['Answer']
    data.append(pair)

# Saving it as a json file
with open('output.json', 'w', encoding='utf8') as json_file:
    json.dump(data, json_file, ensure_ascii=False)
