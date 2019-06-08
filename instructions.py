from memory import Memory

def MOVE(memory, operand):

    return memory

def ADD(org, dest):
    dest = dest + org
    return dest

def operando(code):
    if len(bin(code)[2:]) == 1:
        codigo = '000' + bin(code)[2:]
    elif len(bin(code)[2:]) == 2:
        codigo = '00' + bin(code)[2:]
    elif len(bin(code)[2:]) == 3:
        codigo = '0' + bin(code)[2:]
    else:
        codigo = bin(code)[2:]

    if codigo[0:2] == "00":
        if codigo[2:] == "00":
            return 'd0'
        elif codigo[2:] == "01":
            return 'd1'
        elif codigo[2:] == "10":
            return 'd2'
        elif codigo[2:] == "11":
            return 'd3'
    elif codigo[0:2] == "01":
        if codigo[2:] == "00":
            return 'a0'
        elif codigo[2:] == "01":
            return 'a1'
        elif codigo[2:] == "10":
            return 'a2'
        elif codigo[2:] == "11":
            return 'a3'
    elif codigo[0:2] == "10":
        return 'address'
    elif codigo[0:2] == "11":
        return 'constant'
    else:
        return 'invalido'


def tratar(memory, inicio):
    memory.PC = inicio
    PC = memory.PC
    mem = memory.memory
    while mem[PC] != 240:
        operando1 = operando(int(mem[PC + 1] / 16))
        operando2 = operando(int(mem[PC + 1] % 16))
        memory.CR = operando1

        if mem[PC] == int("10", 16):
            if operando1 in memory.registers:
                operando1 = memory.registers[operando1]
            elif operando1 == 'address':
                operando1 = int(mem[int(mem[PC + 2])])
            elif operando1 == 'constant':
                operando1 = int(mem[PC + 2])

            if operando2 in memory.registers:
                memory.registers[operando2] = operando1
            elif operando2 == 'address':
                memory.memory[int(operando2, 16)] = operando1
            memory.PC = memory.PC + 3
            PC += 3

    return memory