from typing import List, Tuple
import numpy as np


class Packet:
    def __init__(self, data: str):
        self.version = Packet.bin2int(data[0:3])
        self.type_id = Packet.bin2int(data[3:6])
        self.is_literal = (self.type_id == 4)

        if self.is_literal:
            self.header = data[0:6]
            self.content, self.value = Packet.get_literal_value(data[6:])
            self.children = []

        else:
            self.length_type = Packet.bin2int(data[6])
            lengths = [15,11]
            offset = lengths[self.length_type]
            self.header = data[0:7 + offset]
            self.sub_packet_length = Packet.bin2int(data[7: 7 + offset])
            self.content, self.children = Packet.decode(data[7 + offset:], self.length_type, self.sub_packet_length)
            self.value = Packet.evaluate(self.type_id, self.children)

        self.data = self.header + self.content
        self.len = len(self.data)

    @staticmethod
    def decode(content: str, length_type: int, packet_length: int) -> Tuple[str, list]:
        used_data = ''
        children = []
        count = 0
        while True:

            child = Packet(content)
            children.append(child)
            content = content[child.len:]
            used_data += child.data

            if length_type == 0:
                count += child.len
            if length_type == 1:
                count += 1

            if count == packet_length:
                return used_data, children

    @staticmethod
    def evaluate(type_id: int, children: list) -> int:
        funcs = {
            0: lambda list: sum(list),
            1: lambda list: np.prod(list),
            2: lambda list: min(list),
            3: lambda list: max(list),
            5: lambda list: int(list[0] > list[1]),
            6: lambda list: int(list[0] < list[1]),
            7: lambda list: int(list[0] == list[1]),
        }
        return funcs[type_id]([child.value for child in children])

    # read different parts of data
    @staticmethod
    def bin2int(data: str) -> int:
        sum = 0
        for idx, char in enumerate(data[::-1]):
            sum += int(char) * 2**idx
        return sum

    @classmethod
    def get_literal_value(cls, content: str) -> Tuple[str, int]:
        literal_bin = ''
        packet_end = False
        idx = 0
        while not packet_end:
            literal_bin += content[1 + (idx * 5): 5 + (idx * 5)]
            if content[idx * 5] == '0':
                packet_end = True
            idx += 1
        content = content[:len(literal_bin) + idx]
        return content, cls.bin2int(literal_bin)
