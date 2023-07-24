#!/bin/zsh
train_file="data/train_atn_4_all.txt"
test_file="data/test.txt"
vocab_file="data/vocab_imda5_unique_train_atn_4.txt"
lm_file_dir="nlpaug_atn"
extras="_atn_4_all"

alphas=(0 1 0.01 0.001)
orders=(1 2 3)

for ((j=1; j<=${#alphas[@]}; j++)); do
    alpha=${alphas[j]}
    files=("train_uni_imda5_unique_${alpha}${extras}" "train_bi_imda5_unique_${alpha}${extras}" "train_tri_imda5_unique_${alpha}${extras}")

    for file in "${files[@]}"; do
        echo "---------------------"
        echo "$lm_file_dir/$file"
        /usr/share/srilm/bin/i686-m64/ngram -lm "$lm_file_dir/$file.lm" -ppl $test_file
    done
done
