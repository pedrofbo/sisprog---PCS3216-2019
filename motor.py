from memory import Memory
from instructions import tratar
from montador import montar


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
        print(hex(int(memory.registers[command[0][1:].lower()])).upper()[2:])
    elif command[0][1:] == "PC":
        print(hex(memory.PC).upper()[2:])
    elif command[0][1:] == "CR":
        print(hex(memory.CR).upper()[2:])
    elif command[0][1:] == "RR":
        print(hex(memory.RR).upper()[2:])
    else:
        print('Registrador invalido!')

def HELP():
    print("\n   Comandos disponiveis:")
    print("show: mostra as primeiras 100 posições de memória")
    print("load <arquivo>: carrega um arquivo contendo valores hexadecimais na memoria")
    print("clear: limpa toda a memória")
    print("exit: encerra o programa")
    print("MD <endereço de memória>: mostra o valor salvo no endereço determinado e nas F psoições seguintes")
    print("MM <endereço> <valor>: salva o valor no endereço escolhido")
    print("MS <endereço inicial> <valor> <n>: salva o valor no endereço inicial e nos n-1 endereços seguintes")
    print("DF: mostra o valor salvo em todos registradores")
    print(".<registrador>: mostra o valor salvo neste registrador")
    print(".<registrador> <valor>: salva o valor no registrador escolhido")
    print("RUN: roda o programa a partir do endereço salvo em PC")
    print("RUN <endereço>: roda o programa a partir do endereço determinado \n")

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

        elif 'HE' in command[0]:
            HELP()

        elif 'load' in command[0]:
            memory.loadMemory(command[1])
        elif 'assemble' in command[0]:
            montar(command[1])

        else:
            print('Insira um comando válido! Digite HE para ver os comandos disponiveis')


memory = Memory()
memory.showMemory()

main(memory)