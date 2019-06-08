import numpy as np
import pandas as pd
pd.set_option('display.max_columns', 16)

class Memory():
    memory = np.zeros(2048)
    registers = {
        'd0': 0,
        'd1': 0,
        'd2': 0,
        'd3': 0,
        'a0': 0,
        'a1': 0,
        'a2': 0,
        'a3': 0
    }

    PC = 0
    CR = 0


    def showMemory(self):
        col = '0 1 2 3 4 5 6 7 8 9 A B C D E F'.split()
        mem = pd.DataFrame(data=self.memory.reshape(128, 16), columns=col)
        ind = np.arange(0, 2048, 16)
        i = 0
        index = []
        for num in ind:
            index.append(hex(int(num)).upper()[2:])
            i += 1
        mem['address'] = index
        mem.set_index('address', inplace=True)
        memHex = mem.applymap(lambda x: hex(int(x)).upper()[2:])
        print(mem.head(10).applymap(lambda x: hex(int(x)).upper()[2:]))

        return memHex

    def reset(self):
        self.memory = np.zeros(2048)

    def showRegisters(self):
        print(f'PC = {hex(self.PC).upper()[2:]}  CR = {self.CR}')
        print(f"D0 = {hex(self.registers['d0']).upper()[2:]}  D1 = {hex(self.registers['d1']).upper()[2:]}\
  D2 = {hex(self.registers['d2']).upper()[2:]}  D3 = {hex(self.registers['d3']).upper()[2:]}")
        print(f"A0 = {hex(self.registers['a0']).upper()[2:]}  A1 = {hex(self.registers['a1']).upper()[2:]}\
  A2 = {hex(self.registers['a2']).upper()[2:]}  A3 = {hex(self.registers['a3']).upper()[2:]}")