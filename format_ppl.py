import re
file_name = "output_imda4Test/top1_lm3_clean.txt"

with open(file_name, 'r') as file:
    text = file.read()

# Extracting ppl values
ppl_values = re.findall(r'ppl= (\d+\.\d+)', text)

# Extracting interpolation values
interpolation_values = re.findall(r'([\d.]+)\n([\d.]+)', text)

# Formatting and printing ppl values
print("\n".join(ppl_values))

# Formatting and printing interpolation values
for val in interpolation_values:
    print(f'{val[1]}')

f = open(file_name, 'a')
f.write("------------------\n")
f.write("\n".join(ppl_values))
for val in interpolation_values:
    f.write(f'\n{val[1]}')