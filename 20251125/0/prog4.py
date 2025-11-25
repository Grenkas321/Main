def interpret(line: str):
    parts = line.split()
    match parts:
        case ["mov", r1, r2]:
            print(f"moving {r2} to {r1}")
        case [("push" | "pop") as op, *regs] if regs:
            print(f"{op}ing {' '.join(regs)}")
        case [cmd, r1]:
            print(f"making {cmd} with {r1}")
        case _:
            print("Parse error")
