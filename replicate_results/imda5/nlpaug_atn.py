import nlpaug.augmenter.word as naw
atn_aug = naw.AntonymAug()

sizes = [2, 3, 4]


for size in sizes:
    f = open('data/train.txt', 'r')
    f1 = open('data/train_atn_'+str(size)+'_all.txt', 'w')
    lines = f.readlines()
    count = 0

    for sentence in lines:
        f1.write(sentence)
        mod_sentence = sentence
        for i in range(size):
            mod_sentence = atn_aug.augment(mod_sentence, n=1)
            f1.write(mod_sentence[0]+ '\n')
        if(count % 1000 == 0):
            print(count)
        count +=1
    f1.close()
    f.close()
