'''
Create vocab file from all words including the train data of the ngram model
'''

f = open('train_atn_4_all.txt', 'r')
f1 = open('vocab_imda5_unique_train_atn_4.txt', 'w')
lines = f.readlines()
uni = set()

for line in lines:
    arr = line.split(' ')
    arr[-1] = arr[-1][:-1]
    for i in  arr:
        uni.add(i)

for i in uni:
    f1.write(i+'\n')
