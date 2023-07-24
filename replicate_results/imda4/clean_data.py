import csv
import re

f = open('data/train7_11.txt', 'r')
f1 = open('data/train_subset.txt', 'w')

def extract_quotes(input_string):
    pattern = r"'(.*?)'"
    extracted_list = re.findall(pattern, input_string)
    return extracted_list

lines = f.readlines()
count = 0
with open("./data/CS_7-11_outputs.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    f1.write(row[0] + '\n')
    for s in extract_quotes(row[1]):
       f1.write(s + '\n')
    count +=1
    # print(row[0], extract_quotes(row[1]))
    # break