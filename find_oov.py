'''
Find OOV words( which are in test but not in train ) 
'''

f = open('data/oov_train_norm.txt', 'w')
f1 = open('data/vocab_imda4_unique_train.txt', 'r')
f2 = open('data/test_norm_ngram_cut.txt', 'r')

lines = f1.readlines()
uni = set()
for line in lines:
    line = line[:-1]
    uni.add(line)

lines = f2.readlines()
oov = set()
for line in lines:
    arr = line.split(' ')
    arr[-1] = arr[-1][:-1]
    for i in arr:
        if(i not in uni):
            oov.add(i)

print(len(oov))

for i in oov:
    f.write(i+'\n')
