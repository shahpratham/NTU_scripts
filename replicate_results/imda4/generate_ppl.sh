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

    for file in "${files[@]}"; do
        echo "---------------------"
        echo "$lm_file_dir/$file"
        /usr/share/srilm/bin/i686-m64/ngram -lm "$lm_file_dir/$file.lm" -ppl $test_file
    done
done
