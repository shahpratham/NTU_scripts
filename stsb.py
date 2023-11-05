from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import csv
import pandas as pd
import re

model = SentenceTransformer('sentence-transformers/stsb-xlm-r-multilingual')

# Custom functions
def getlist(eng, cs):
  e1 = model.encode(eng).reshape(1,-1)
  ans = []
  for s in cs:
    e2 = model.encode(s).reshape(1,-1)
    ans.append(cosine_similarity(e1, e2)[0][0])
  return ans

def clean(input_string):
  cleaned_string = re.sub(r'(?<=\n)\d+\.', '', input_string)
  # Split the string without '\n'
  result_list = cleaned_string.split('\n')
  # Remove empty strings from the list (if any)
  result_list = [item.strip() for item in result_list if item.strip()]
  return result_list

def sort_lists(list1, list2):
    combined = list(zip(list1, list2))
    sorted_combined = sorted(combined, key=lambda x: x[1], reverse=True)
    sorted_list1, sorted_list2 = zip(*sorted_combined)
    return list(sorted_list1), list(sorted_list2)

df_op = pd.read_csv('palm_gen10_bertscore.csv')
index = df_op.shape[0]

df_ip = pd.read_csv('palm_generate10.csv')
total_sentences = df_ip.shape[0]
print("File ranges: ",index, total_sentences)

with open('palm_gen10_bertscore.csv', 'a') as csvfile:
  csvwriter = csv.writer(csvfile)
  for i in range(index, total_sentences):
    eng, cs = df_ip.iloc[i]['Input english sentence'], clean(df_ip.iloc[i]['Output 10 codeswitch palm'][2:])
    op = getlist(eng, cs)
    cs, val = sort_lists(cs, op)
    csvwriter.writerow([eng,cs,val])
