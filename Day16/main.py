from packet import Packet

with open('input.txt') as f:
    data = f.readline().strip()


def hex2bin(hex_string: str) -> str:
    bin_conversion = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'}
    new_string = ''
    for char in hex_string:
        new_string += bin_conversion[char]
    return new_string


data = hex2bin(data)

packet = Packet(data)


def add_versions(packet):
    count = 0
    count += packet.version
    for child in packet.children:
        count += add_versions(child)
    return count


print(f'Solution to part 1: {add_versions(packet)}')

print(f'Solution to part 2: {packet.value}')
