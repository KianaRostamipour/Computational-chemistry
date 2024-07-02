"""
This script updates an atom types file by appending new entries extracted from a specified text file. It processes the data, derives atomic weights based on the atom type, and formats it for inclusion in the atom types file.
Determines the atomic weight based on the initial character of your ligand atom type.
"""
final_output_file = 'final.txt'
atomtypes_file = 'atomtypes.atp'
string_to_add = ";added by Kiana"
with open(final_output_file, 'r') as file:
    data_to_add = file.readlines()[1:] 
def get_second_column_value(first_column):
    if first_column.startswith('c'):
        return '  12.01000'
    elif first_column.startswith('h'):
        return '   1.00800'
    elif first_column.startswith('s'):
        return '  32.06000'
    elif first_column.startswith('o'):
        return '  16.00000'
    elif first_column.startswith('n'):
        return '  14.01000'
    elif first_column.startswith('f'):
        return '  19.00000'    
    else:
        return '   error'  
extracted_data = [' ' + line.split()[0] + get_second_column_value(line.split()[0]) + '\n' for line in data_to_add]
with open(atomtypes_file, 'a') as file:
    file.write(string_to_add + "\n")
    file.write("\n")
    for line in extracted_data:
        file.write(line)

