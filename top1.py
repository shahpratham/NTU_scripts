import ast
import pandas as pd
# f = open('top1_stsb_train.txt', 'w')
# df_op = pd.read_csv('palm_gen10_bertscore.csv')
# for i in range(df_op.shape[0]):
#   top1 = ast.literal_eval(df_op.iloc[i][1])[0]
#   f.write(top1+'\n')
f = open('eng_train.txt', 'w')
df_op = pd.read_csv('palm_gen10_bertscore.csv')
for i in range(df_op.shape[0]):
  # top1 = ast.literal_eval(df_op.iloc[i][0])[0]
  f.write(df_op.iloc[i][0])
