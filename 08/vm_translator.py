import sys
import os
from parser import Parser

def parse_vm_file(input_file_path: str) -> list:
    #if source is a folder, handle every vm file separately
    if not ".vm" in input_file_path:
        print("not vm file!!!")
        return []
    #if source is a vm file
    file_name = os.path.basename(input_file_path).split(".vm")[0]
    raw_commands = []
    asm_codes = []
    with open(input_file_path, "r") as file:
        for row in file:
            raw_commands.append(row)
    p = Parser(raw_commands, file_name)
    p.run_first_pass()
    p.run_second_pass()
    asm_codes = p.get_asm_codes()
    return asm_codes

def main():
    #open and save file
    if len(sys.argv) != 3:
        sys.exit("Wrong input")
    input_path = sys.argv[1]
    out_file_path = sys.argv[2]
    asm_codes = []
    if ".vm" not in input_path:
        # add init code. 
        # assume a dummy function frame (size=5) is pushed to stack before calling Sys.init
        asm_codes = [f"@{256+5}", "D=A", "@SP", "M=D", "@Sys.init", "0;JMP"]
        for file_name in os.listdir(input_path):
            if file_name.endswith('.vm'):
                file_path = os.path.join(input_path, file_name)
                print(file_path)
                asm_codes.extend(parse_vm_file(file_path))
    else:
        asm_codes = parse_vm_file(input_path)
    
    with open(out_file_path, 'w', newline='\n') as file:
        for line in asm_codes:
            file.write(f"{line}\n")

main()