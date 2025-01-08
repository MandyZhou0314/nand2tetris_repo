import sys
import os
sys.path.insert(0, "../parser")
from parser import Parser

def parse_vm_file(inputFileStr: str) -> list:
    #if source is a folder, handle every vm file separately
    if not ".vm" in inputFileStr:
        print("not vm file!!!")
        return []
    #if source is a vm file
    fileName = os.path.basename(inputFileStr).split(".vm")[0]
    raw_commands = []
    asm_codes = []
    with open(inputFileStr, "r") as file:
        for row in file:
            raw_commands.append(row)
    p = Parser(raw_commands, fileName)
    p.run_first_pass()
    p.run_second_pass()
    asm_codes = p.get_asm_codes()
    return asm_codes

def main():
    #open and save file
    if len(sys.argv) != 3:
        sys.exit("Wrong input")
    inputPath = sys.argv[1]
    outFileStr = sys.argv[2]
    asm_codes = []
    if ".vm" not in inputPath:
        
        asm_codes += ["@256", "D=A", "@SP", "M=D"]
        p = Parser(["call Sys.init 0"], "aa")
        p.run_first_pass()
        p.run_second_pass()
        asm_codes += p.get_asm_codes()
        
        for filename in os.listdir(inputPath):
            if filename.endswith('.vm'):
                file_path = os.path.join(inputPath, filename)
                print(file_path)
                asm_codes.extend(parse_vm_file(file_path))
        
    else:
        asm_codes = parse_vm_file(inputPath)
    
    with open(outFileStr, 'w', newline='\n') as file:
        for line in asm_codes:
            file.write(f"{line}\n")

main()