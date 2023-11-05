'''
Create vocab file from all words including the train data of the ngram model
'''

f = open('lm4_train_clean.txt', 'r')
f1 = open('vocab_lm4_train.txt', 'w')
lines = f.readlines()
uni = set()

for line in lines:
    arr = line.split(' ')
    arr[-1] = arr[-1][:-1]
    for i in  arr:
        uni.add(i)

for i in uni:
    f1.write(i+'\n')
