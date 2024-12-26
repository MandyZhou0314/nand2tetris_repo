import sys
import os
sys.path.insert(0, "../parser")
from parser import Parser

def main():
    #open and save file
    if len(sys.argv) != 3:
        sys.exit("Wrong input")
    inputFileStr = sys.argv[1]
    fileName = os.path.basename(inputFileStr).split(".vm")[0]
    outFileStr = sys.argv[2]
    raw_commands = []
    asm_codes = []
    with open(inputFileStr, "r") as file:
        for row in file:
            raw_commands.append(row)
    p = Parser(raw_commands, fileName)
    p.run_first_pass()
    p.run_second_pass()
    asm_codes = p.get_asm_codes()
    with open(outFileStr, 'w', newline='\n') as file:
        for line in asm_codes:
            file.write(f"{line}\n")

main()