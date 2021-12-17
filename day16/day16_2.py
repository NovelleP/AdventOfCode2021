from operator import imul
from functools import reduce
from collections import defaultdict


def read_input(file_path: str) -> str:
    with open(file_path, 'r') as fp:
        return ''.join([bit for hex in fp.read().strip() for bit in bin(int(hex, 16))[2:].zfill(4)])


def get_packet_info(packet: str) -> dict:
    version = packet[:3]
    type_id = packet[3:6]
    length = 6
    length_type_id = None
    subpackets_length = None
    subpackets_amount = None
    content = None
    if type_id == '100':
        content = ''
        for i in range(6, len(packet), 5):
            content += packet[i: i+5]
            if packet[i] == '0':
                break
        length += len(content)
    else:
        if len(packet) < 6:
            return {}
        length_type_id = packet[6]
        length += 1
        if length_type_id == '0':
            subpackets_length = int(packet[7:22], 2)
            length += 15
            content = packet[22:]
        elif length_type_id == '1':
            subpackets_amount = int(packet[7:18], 2)
            length += 11
            content = packet[18:]
    return {
        'headers': {
            'version': version,
            'type_id': type_id,
            'length_type_id': length_type_id,
            'subpackets_length': subpackets_length,
            'subpackets_amount': subpackets_amount
        },
        'content': content,
        'length': length
    }


def split_subpackets(packet: str, packets: list):
    packet_info = get_packet_info(packet)
    if not packet_info:
        return
    packets.append(packet_info)
    if packet_info['headers']['type_id'] == '100':
        header_length = sum(len(val) for val in packet_info['headers'].values() if val)
        content_length = len(packet_info['content'])
        packet = packet[header_length + content_length:]
        split_subpackets(packet, packets)
    else:
        split_subpackets(packet_info['content'], packets)


def solve(packet: str) -> int:
    packets = []
    split_subpackets(packet, packets)
    non_literals_pack_idxs = [idx for idx, p in enumerate(packets) if p['headers']['type_id'] != '100']
    for non_lit_idx in non_literals_pack_idxs[::-1]:
        packet = packets[non_lit_idx]
        if amount := packet['headers']['subpackets_amount']:
            curr_idx = non_lit_idx + 1
            childs = []
            while (curr_idx < len(packets)) and (len(childs) < amount):
                if packets[curr_idx].get('visited', False):
                    curr_idx += 1
                    continue
                childs.append(packets[curr_idx])
                curr_idx += 1
        elif childs_length := packet['headers']['subpackets_length']:
            childs = []
            curr_length = 0
            curr_idx = non_lit_idx + 1
            while (curr_idx < len(packets)) and (curr_length <= childs_length):
                if packets[curr_idx].get('visited', False):
                    curr_idx += 1
                    continue
                elif (curr_length + packets[curr_idx]['length']) > childs_length:
                    curr_idx += 1
                    continue
                childs.append(packets[curr_idx])
                curr_length += packets[curr_idx]['length']
                curr_idx += 1

        curr_vals = []
        for p in childs:
            if p.get('visited', False):
                continue
            elif p['headers']['type_id'] == '100':
                val = int(''.join([p['content'][i + 1: i + 5] for i in range(0, len(p['content']), 5)]), 2)
                p['value'] = val
            p['visited'] = True
            curr_vals.append(p['value'])

        p = packet
        if p['headers']['type_id'] == '000':
            p['value'] = (sum(curr_vals))
        elif p['headers']['type_id'] == '001':
            p['value'] = (reduce(imul, curr_vals, 1))
        elif p['headers']['type_id'] == '010':
            p['value'] = (min(curr_vals))
        elif p['headers']['type_id'] == '011':
            p['value'] = (max(curr_vals))
        elif p['headers']['type_id'] == '101':
            p['value'] = (int(curr_vals[0] > curr_vals[1]))
        elif p['headers']['type_id'] == '110':
            p['value'] = (int(curr_vals[0] < curr_vals[1]))
        elif p['headers']['type_id'] == '111':
            p['value'] = (int(curr_vals[0] == curr_vals[1]))
        p['length'] += sum(c['length'] for c in childs)

    return packets[0]['value']


if __name__ == '__main__':

    packet = read_input('input.txt')
    ans = solve(packet)
    print(ans)
