import os
import re 
import csv

def print_pdfs():
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.pdf'):
                full_file_path = os.path.join(root,file)
                print(full_file_path)

def get_odd_files():
    for root,dirs,files in os.walk('.'):
        for file in files:
            if re.search(r'[13579]',file):
                full_file_path = os.path.join(root,file)
                print(full_file_path)

def read_zen_of_python():           
    with open('zen_of_python.txt', 'r') as file:
        for line in file:
            if 'better' in line.lower():
                print(line)
                break

with open('top_films.csv') as file:
    data = csv.DictReader(file)
    structured_data = [row for row in data]
print(structured_data[0])