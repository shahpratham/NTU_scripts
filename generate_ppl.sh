#!/bin/zsh
train_file="./data/lm1_train.txt"
test_file="./data/All_filteredIMDA5-10w_test.txt"
vocab_file="./data/vocab_lm5_train.txt"
lm_file_dir="lm/lm1"
# extras="_syn_4_all"
output_file="./results/output_imda5Test/top1_lm1_clean.txt"

alphas=(0.001)
orders=(1 2 3 )


for ((j=1; j<=${#alphas[@]}; j++)); do
    alpha=${alphas[j]}
    files=("train_uni_imda4_${alpha}${extras}" "train_bi_imda4_${alpha}${extras}" "train_tri_imda4_${alpha}${extras}" ) #
    echo "-----------------------------------------------------------" >> $output_file
    for file in "${files[@]}"; do
        echo "$lm_file_dir/$file" >> $output_file
        /usr/share/srilm/bin/i686-m64/ngram -lm "$lm_file_dir/$file.lm" -vocab $vocab_file -ppl $test_file >> $output_file
        /usr/share/srilm/bin/i686-m64/ngram -lm "$lm_file_dir/$file.lm" -vocab $vocab_file -ppl $test_file -debug 2 >> "$lm_file_dir/$file.ppl"
        echo "---------------------" >> $output_file
    done

    # Linear Interpolation
    file1="train_uni_imda4_${alpha}${extras}"
    file2="train_bi_imda4_${alpha}${extras}"
    file3="train_tri_imda4_${alpha}${extras}"
    # file4="train_quad_imda4_${alpha}${extras}" #

    lambda1=$(/usr/share/srilm/bin/i686-m64/compute-best-mix "$lm_file_dir/$file1.ppl" "$lm_file_dir/$file2.ppl" | awk '/best/{gsub(/\(|\)/,"");print $6}')
    lambda2=$(/usr/share/srilm/bin/i686-m64/compute-best-mix "$lm_file_dir/$file2.ppl" "$lm_file_dir/$file3.ppl" | awk '/best/{gsub(/\(|\)/,"");print $6}')
    # lambda3=$(/usr/share/srilm/bin/i686-m64/compute-best-mix "$lm_file_dir/$file3.ppl" "$lm_file_dir/$file4.ppl" | awk '/best/{gsub(/\(|\)/,"");print $6}') #

    /usr/share/srilm/bin/i686-m64/ngram -lm "$lm_file_dir/$file1.lm"  -mix-lm "$lm_file_dir/$file2.lm" -lambda $lambda1 -write-lm mixed1.lm
    /usr/share/srilm/bin/i686-m64/ngram -lm "$lm_file_dir/$file2.lm"  -mix-lm "$lm_file_dir/$file3.lm" -lambda $lambda2 -write-lm mixed2.lm
    # /usr/share/srilm/bin/i686-m64/ngram -lm "$lm_file_dir/$file3.lm"  -mix-lm "$lm_file_dir/$file4.lm" -lambda $lambda3 -write-lm mixed3.lm #

    echo "Unigram-Bigram interpolation for alpha = $alpha" >> $output_file
    /usr/share/srilm/bin/i686-m64/ngram -lm mixed1.lm -vocab $vocab_file -ppl $test_file | awk 'FNR == 2 {print $6}' >> $output_file
    echo "Bigram-Trigram interpolation for alpha = $alpha" >> $output_file
    /usr/share/srilm/bin/i686-m64/ngram -lm mixed2.lm -vocab $vocab_file -ppl $test_file | awk 'FNR == 2 {print $6}' >> $output_file
    # echo "Trigram-Quadgram interpolation for alpha = $alpha" >> $output_file #
    # /usr/share/srilm/bin/i686-m64/ngram -lm mixed3.lm -vocab $vocab_file -ppl $test_file | awk 'FNR == 2 {print $6}' >> $output_file #

done
