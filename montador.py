import pandas as pd

def adicional(string):
    add = 2
    for character in string:
        if character == '$' or character == '#':
            add += 1
    return add

def primeiroPasso(assembly, PC):
    assembly['operandos'].fillna(value = '0', inplace=True)
    assembly['adicional'] = assembly['operandos'].apply(adicional)

    address = []
    address.append(PC)
    address.append(PC)
    nlinhas = len(assembly)
    i = 2
    while i < nlinhas:
        address.append(address[i - 1] + assembly['adicional'][i - 1])
        i += 1
    assembly['endereço'] = address
    assembly['endereço'] = assembly['endereço'].apply(lambda x: hex(int(x)).upper()[2:])
    return assembly

def segundoPasso(assembly, PC):
    comandos = {
        'MOVE': '10',
        'MOVEA': '11',
        'ADD': '20',
        'ADDA': '21',
        'SUB': '30',
        'SUBA': '31',
        'JUMP': '40',
        'CMP': '50',
        'CMPA': '51',
        'BEQ': '61',
        'BNE': '62',
        'BHI': '63',
        'BLT': '64',
        'MULT': '70',
        'BSR': '80',
        'RTS': '81',
        'end': 'F0'
    }
    operandos = {
        'd0': '0',
        'd1': '1',
        'd2': '2',
        'd3': '3',
        'a0': '4',
        'a1': '5',
        'a2': '6',
        'a3': '7',
        '$': '8',
        '#': 'C'
    }
    programa = hex(PC).upper()[2:] + " "
    nlinhas = len(assembly)
    i = 1
    while i < nlinhas:
        if assembly['comando'][i] in comandos:
            programa += comandos[assembly['comando'][i]] + " "
        op = assembly['operandos'][i].lower().split(",")
        if op[0] in operandos:
            programa += operandos[op[0]]
            if op[1] in operandos:
                programa += operandos[op[1]] + " "
            elif '$' in op[0]:
                programa += operandos[op[1][0]] + " "
        elif '$' in op[0] or '#' in op[0]:
            programa += operandos[op[0][0]]
            if op[1] in operandos:
                programa += operandos[op[1]] + " "
            elif '$' in op[0] or '#' in op[0]:
                programa += operandos[op[1][0]] + " "
        elif op[0] != '0':
            y = assembly[assembly['label'] == op[0]]['endereço'].max()
            programa += str(y) + " "
        if assembly['adicional'][i] == 3:
            if '$' in op[0] or '#' in op[0]:
                programa += op[0][1:].upper() + " "
            elif '$' in op[1] or '#' in op[1]:
                programa += op[1][1:].upper() + " "
        elif assembly['adicional'][i] == 4:
            programa += op[0][1:].upper() + " "
            programa += op[1][1:].upper() + " "

        i += 1

    print(f'\n{programa}')
    return programa


def montar(arquivo):
    file = 'assembly/' + arquivo
    assembly = pd.read_csv(open(file, "r"), sep = "\t", header = None)
    assembly.columns = "label comando operandos".split()
    print(assembly)

    PC = int(assembly[assembly['comando'] == 'org']['operandos'][0][1:], 16)
    assembly = primeiroPasso(assembly, PC)
    print(assembly)
    programa = segundoPasso(assembly, PC)

    open('programas/' + arquivo, "w").write(programa)