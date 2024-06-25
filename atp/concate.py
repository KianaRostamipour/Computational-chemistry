"""
This script concatenates atom type sections from multiple .itp files into a single file.
It searches for '[ atomtypes ]' sections in the input files and extracts lines until the '[ moleculetype ]' section or end of the file.
The extracted atom types are written to a final output file named 'final.txt'.
"""
import os
import os
def extract_atomtypes(input_file_path, lines):
    atomtypes_lines = []
    found_atomtypes = False
    for line in lines:
        if line.strip() == '[ atomtypes ]':
            found_atomtypes = True
        elif line.strip() == '[ moleculetype ]':
            break
        elif found_atomtypes and line.strip():
            atomtypes_lines.append(line)
    return atomtypes_lines
def concatenate_files(input_files, output_file):
    with open(output_file, 'w') as outfile:
        for fname in input_files:
            with open(fname) as infile:
                lines = infile.readlines()
                atomtypes_lines = extract_atomtypes(fname, lines)
                for line in atomtypes_lines:
                    outfile.write(line)
itp_files = [f for f in os.listdir() if f.endswith('.itp')]
concatenated_file = "final.txt"
concatenate_files(itp_files, concatenated_file)


