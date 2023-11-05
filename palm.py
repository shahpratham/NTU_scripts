import google.generativeai as palm
import csv
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv('API_KEY')
print(API_KEY)
os.environ['GRPC_DNS_RESOLVER'] = 'native'
palm.configure(api_key=API_KEY)
model_list = [_ for _ in palm.list_models()]
# for model in model_list:
#     print(model.name)

model_id = "models/text-bison-001"

prompt = """
Sample example:
    English Input Sentences:
    1. no pain no gain you need to you need to suffer the risk darling if the i mean

    Codeswitch Output Sentence format:
    1. So, dia takkan just stand there and tengok mereka buat apa saja, you know what I mean.
    2. Dia takkan just berdiri di situ and watch them do apa saja, kan?
    3. He won't just stand there and watch them buat apa saja, you need to take action.
    4. So, dia takkan just berdiri di situ dan tengok saja what they're doing, kan?
    5. Dia takkan just stand there and tengok what they do saja, you need to step in.
    6. So, dia takkan just stand there and watch them do apa saja without doing anything.
    7. Dia takkan just stand there and tengok saja what they're doing, you know what I mean.
    8. He won't just berdiri di situ and watch them buat apa saja, kan?
    9. So, dia takkan just berdiri di situ and watch them buat apa saja, you know what I mean.
    10. Dia takkan just stand there and watch them do apa saja, you need to take action.

Generate 10 diverse Malay-English codeswitch sentences for the following input sentence:
"""

f = open('replicate_results/imda5/data/All_filteredIMDA5-10w.txt', 'r')
output_file = 'replicate_results/imda5/data/palm_generate10.csv'
index = 62254
lines = f.readlines()
c = 0
headerList = ['Input english sentence', 'Output 10 codeswitch palm']

with open(output_file, 'a') as csvfile:
    csvwriter = csv.writer(csvfile)
    # csvwriter.writerow(headerList)
    for line in lines[index: ]:
        ip = prompt + line
        print(line)
        completion = palm.generate_text(
            model=model_id,
            prompt=ip,
            temperature=0.8,
            max_output_tokens=1024,
            candidate_count=1
            )
        for op in completion.candidates:
            csvwriter.writerow([line,op['output']])
        # print(op['output'])
