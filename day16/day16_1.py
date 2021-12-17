def read_input(file_path: str) -> str:
    with open(file_path, 'r') as fp:
        return ''.join([bit for hex in fp.read().strip() for bit in bin(int(hex, 16))[2:].zfill(4)])


def get_packet_info(packet: str) -> dict:
    version = packet[:3]
    type_id = packet[3:6]
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
    else:
        if len(packet) < 6:
            return {}
        length_type_id = packet[6]
        if length_type_id == '0':
            subpackets_length = int(packet[7:22], 2)
            content = packet[22:]
        elif length_type_id == '1':
            subpackets_amount = int(packet[7:18], 2)
            content = packet[18:]
    return {
        'headers': {
            'version': version,
            'type_id': type_id,
            'length_type_id': length_type_id,
            'subpackets_length': subpackets_length,
            'subpackets_amount': subpackets_amount
        },
        'content': content
    }


def split_subpackets(packet: str, subpackets: list[dict]):
    packet_info = get_packet_info(packet)
    if not packet_info:
        return
    subpackets.append(packet_info)
    if packet_info['headers']['type_id'] == '100':
        header_length = sum(len(val) for val in packet_info['headers'].values() if val)
        content_length = len(packet_info['content'])
        packet = packet[header_length + content_length:]
        split_subpackets(packet, subpackets)
    else:
        split_subpackets(packet_info['content'], subpackets)


def solve(packet: str) -> int:
    subpackets = []
    split_subpackets(packet, subpackets)
    return sum(int(d['headers']['version'], 2) for d in subpackets)


if __name__ == '__main__':

    packet = read_input('input.txt')
    ans = solve(packet)
    print(ans)
