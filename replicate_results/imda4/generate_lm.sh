#!/bin/zsh
train_file="data/train_norm_ngram_cut"
test_file="data/test_norm_ngram_cut"
vocab_file="data/cs_vocab.txt"
lm_file_dir="baseline"
# extras="_syn_4_all"

alphas=(0 1 0.01 0.001)
orders=(1 2 3)

for ((j=1; j<=${#alphas[@]}; j++)); do
    alpha=${alphas[j]}
    files=("train_uni_imda4_${alpha}${extras}" "train_bi_imda4_${alpha}${extras}" "train_tri_imda4_${alpha}${extras}")
    echo $files

    for ((i=1; i<=${#files[@]}; i++)); do
        order=${orders[i]}
        file=${files[i]}
        /usr/share/srilm/bin/i686-m64/ngram-count -text $train_file -order $order -write "$lm_file_dir/$file.count" -lm "$lm_file_dir/$file.lm" -addsmooth $alpha -vocab $vocab_file
    done
done
