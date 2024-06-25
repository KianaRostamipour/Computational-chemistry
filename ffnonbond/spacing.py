"""
This script reads atom type data from 'output.itp' and appends it to 'ffnonbonded.itp'.
It writes a section header ";LIG" to 'ffnonbonded.itp', processes lines with at least 8 columns,
and formats them before appending. Lines with fewer than 8 columns are written as they are.
"""
input_file = "output.itp" 
output_file = "ffnonbonded.itp" 
with open(input_file, 'r') as infile, open(output_file, 'a') as outfile:  
    outfile.write(";LIG\n")  
    for line in infile:
        columns = line.split()
        if len(columns) >= 8:
            modified_line = f"{columns[0]}   {columns[1]}   {columns[2]}      {columns[3]}     {columns[4]}       {columns[5]}    {columns[6]}  {columns[7]}\n"
            outfile.write(modified_line)
        else:
            outfile.write(line)

