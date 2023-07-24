import nlpaug.augmenter.word as naw
syn_aug = naw.SynonymAug()

f = open('data/train.txt', 'r')
f1 = open('data/train_syn_4_all.txt', 'w')
lines = f.readlines()
count = 0

for sentence in lines:
    f1.write(sentence)
    mod_sentence = sentence
    for i in range(4):
        mod_sentence = syn_aug.augment(mod_sentence, n=1)
        f1.write(mod_sentence[0]+ '\n')
    if(count % 1000 == 0):
        print(count)
    count +=1
f1.close()
