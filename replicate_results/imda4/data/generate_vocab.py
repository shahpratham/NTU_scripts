'''
Create vocab file from all words including the train data of the ngram model
'''

f = open('train_norm_ngram_cut', 'r')
f1 = open('vocab_imda4_unique_train.txt', 'w')
lines = f.readlines()
uni = set()

for line in lines:
    arr = line.split(' ')
    arr[-1] = arr[-1][:-1]
    for i in  arr:
        uni.add(i)

for i in uni:
    f1.write(i+'\n')
