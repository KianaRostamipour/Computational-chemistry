"""
This script processes data from a text file 'final.txt' to update an itp file 'output.itp'.
It reads atom types from the text file, calculates their atomic numbers, and formats the data for appending to the ITP file.
Each entry in the text file, except the first line, is processed and added to 'output.itp' with a comment ";added by Kiana".
Determines the atomic numbers based on the initial character of your ligand.
"""

txt_file_path = 'final.txt'
itp_file_path = 'output.itp'
string_to_add = ";added by Kiana"
with open(txt_file_path, 'r') as txt_file:
    data_to_add = txt_file.readlines()
def get_second_column_value(first_column):
    if first_column.startswith('c'):
        return '6'
    elif first_column.startswith('h'):
        return '1'
    elif first_column.startswith('s'):
        return '16'
    elif first_column.startswith('o'):
        return '8'
    elif first_column.startswith('n'):
        return '7'
    elif first_column.startswith('f'):
        return '9'    
    else:
        raise ValueError(f"Unknown case: {first_column}")  
extracted_data = [' '.join([line.split()[0].ljust(4), get_second_column_value(line.split()[0]).rjust(7)] + line.split()[2:7]) + '\n' for line in data_to_add[1:]]
with open(itp_file_path, 'a') as itp_file:
    itp_file.write(string_to_add + "\n")
    itp_file.write("\n")
    for line in extracted_data:
        itp_file.write(line)

