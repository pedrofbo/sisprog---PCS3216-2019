from memory import Memory
from instructions import tratar


def MD(memory, address):
    print(f'{hex(int(address)).upper()[2:]} |     ', end='')
    for byte in memory[address : address + 16]:
        print(f'{hex(int(byte)).upper()[2:]}    ', end='')
    print('\n')

def MM(memory, address, value):
    memory[address] = value
    return memory

def MS(memory, address, value, length):
    memory[address : address + length] = value
    return memory

def RegUpdate(memory, command, value):
    if command[0][1:].lower() in memory.registers:
        memory.registers[command[0][1:].lower()] = value
        return memory
    elif command[0][1:] == 'PC':
        memory.PC = value
        return memory
    else:
        print('Registrador invalido!')
        return memory

def RegShow(memory, command):
    if command[0][1:].lower() in memory.registers:
        print(memory.registers[command[0][1:].lower()])
    else:
        print('Registrador invalido!')

def main(memory):
    while 1:
        command = input('Insira um comando: ')
        command = command.split()

        if 'MD' in command:
            MD(memory.memory, int(command[1], 16))
        elif 'MM' in command:
            memory.memory = MM(memory.memory, int(command[1], 16), int(command[2], 16))
        elif 'MS' in command:
            memory.memory = MS(memory.memory, int(command[1], 16), int(command[2], 16), int(command[3], 16))
        elif 'show' in command:
            memory.showMemory()
        elif 'clear' in command:
            memory.reset()
        elif 'DF' in command:
            memory.showRegisters()
        elif 'exit' in command:
            return 0
        elif '.' in command[0] and len(command) == 2:
            memory = RegUpdate(memory, command, int(command[1], 16))
        elif '.' in command[0] and len(command) == 1:
            RegShow(memory, command)

        elif 'RUN' in command[0] and len(command) == 1:
            memory = tratar(memory, memory.PC)
        elif 'RUN' in command[0] and len(command) == 2:
            memory = tratar(memory, int(command[1], 16))

        elif 'load' in command[0]:
            memory.loadMemory(command[1])

        else:
            print('Insira um comando válido!')


memory = Memory()
memory.showMemory()

main(memory)