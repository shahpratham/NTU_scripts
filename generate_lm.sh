#!/bin/zsh
train_file="./data/lm1_train.txt"
test_file="./data/All_filteredIMDA5-10w_test.txt"
vocab_file="./data/vocab_lm5_train.txt"
lm_file_dir="lm/lm1"
# extras="_syn_4_all"

alphas=(0.001)
orders=(1 2 3 )

for ((j=1; j<=${#alphas[@]}; j++)); do
    alpha=${alphas[j]}
    files=("train_uni_imda4_${alpha}${extras}" "train_bi_imda4_${alpha}${extras}" "train_tri_imda4_${alpha}${extras}" ) #
    echo $files

    for ((i=1; i<=${#files[@]}; i++)); do
        order=${orders[i]}
        file=${files[i]}
        /usr/share/srilm/bin/i686-m64/ngram-count -text $train_file -order $order -write "$lm_file_dir/$file.count" -lm "$lm_file_dir/$file.lm" -addsmooth $alpha -vocab $vocab_file
    done
done
