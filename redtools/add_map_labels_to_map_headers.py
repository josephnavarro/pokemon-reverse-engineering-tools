# editor: Joey Navarro
# date: 2023
# purpose: insert labels into map headers
import sys
import os


DEFAULT_FILENAME: str = os.path.join("..", "pokered.asm")

asm = None
asm_lines = []  # Globally mutated in place


def load_asm(filename: str = DEFAULT_FILENAME) -> None:
    global asm
    global asm_lines
    with open(filename, "r") as f:
        asm = f.read()
    asm_lines = asm.split("\n")


def find_with_start_of_line(name: str) -> bool:
    global asm_lines
    name_len: int = len(name)

    for line in asm_lines:
        line_len: int = len(line)
        if (line_len > name_len) and (": " in line):
            if line[:name_len] == name:
                return True
    return False


def process_lines() -> None:
    global asm
    global asm_lines

    for line in asm_lines:  # type: str
        if not ("_h:" in line):
            continue
        else:
            index: int = asm_lines.index(line)
            name: str = line.split("_h:")[0]

            if "Blocks" in asm_lines[index + 3]:
                continue
            else:
                if not find_with_start_of_line(f"{name}Blocks:"):
                    continue
                else:
                    orig_line = asm_lines[index + 3]
                    fixed_line = orig_line.split(",")
                    fixed_line[0] = f"    dw {name}Blocks"
                    fixed_line = ",".join(fixed_line)
                    asm_lines[index + 3] = fixed_line


if __name__ == "__main__":
    load_asm()
    process_lines()
    sys.stdout.write("\n".join(asm_lines))
