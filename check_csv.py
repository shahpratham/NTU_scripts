import csv

def check_csv_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        line_number = 0
        for line_number, row in enumerate(reader, 1):
            if len(row) != 3:
                print(row)
                print(f"Error at line {line_number}: Expected 3 fields, but found {len(row)} fields")

# file_path = 'your_file.csv'  # Replace with the actual path to your CSV file
check_csv_file("palm_gen10_bertscore.csv")
