with open('input.txt') as f:
    DATA = f.read()

def parse_data(data):
    output = ""
    for char in data:
        try:
            byte = bin(int(char))[2:]
            while len(byte) < 4:
                byte = '0' + byte
            output += byte
        except ValueError:
            byte = bin(int('0x' + char, 0))[2:]
            while len(byte) < 4:
                byte = '0' + byte
            output += byte
    return output

def read_number(data):
    output = ''
    byte = data[:5]
    data = data[5:]
    k = 1
    while byte[0] == '1':
        output += byte[1:]
        byte = data[:5]
        data = data[5:]
        k += 1
    output += byte[1:]
    return int('0b'+output, 0), k, data

def read_one_packet(data):
    packets = []
    version = int('0b'+data[0:3], 0)
    packet_type = int('0b'+data[3:6], 0)
    if packet_type == 4:
        number, bytes_read, remaining_data = read_number(data[6:])
        bits_read = 6+ 5*bytes_read
        return {'version': version, 'packet_type': packet_type, 'value': number,
                'bits': bits_read, 'data': data[:bits_read]}, remaining_data
    else:  # packet is "operator"
        if data[6] == '0':
            length = int('0b'+data[7:7+15], 0)
            bits_read = 0
            data = data[7+15:]
            while bits_read < length:
                packet, data = read_one_packet(data)
                packets.append(packet)
                bits_read += packet['bits']
            return {'version': version, 'packet_type': packet_type, 'length': length, 'packets': packets, 'bits': bits_read + 7 + 15}, data
        if data[6] == '1':
            number = int('0b'+data[7:7+11], 0)
            packets_read = 0
            bits_read = 0
            data = data[7+11:]
            while packets_read < number:
                packet, data = read_one_packet(data)
                packets.append(packet)
                packets_read += 1
                bits_read += packet['bits']
            return {'version': version, 'packet_type': packet_type, 'number': number,
                    'packets': packets, 'bits': bits_read + 7 + 11}, data

print(read_one_packet(parse_data('D2FE28')))
print(read_one_packet(parse_data('38006F45291200')))
print(read_one_packet(parse_data('EE00D40C823060')))

def get_version_sum(packet):
    version_sum = 0
    version_sum += packet['version']
    if 'packets' in packet:
        for subpacket in packet['packets']:
            version_sum += get_version_sum(subpacket)
    return version_sum


def verify_length(packet):
    if 'length' in packet:
        total_bits = 0
        for subpacket in packet['packets']:
            total_bits += subpacket['bits']
        if total_bits != packet['length']:
            raise
    if 'packets' in packet:
        for subpacket in packet['packets']:
            if not verify_length(subpacket):
                raise
    return True

def process_packet(packet):
    if packet['packet_type'] == 4:
        return packet['value']
    elif packet['packet_type'] == 0:
        return sum([process_packet(subpacket) for subpacket in packet['packets']])
    elif packet['packet_type'] == 1:
        output = 1
        for subpacket in packet['packets']:
            output *= process_packet(subpacket)
        return output
    elif packet['packet_type'] == 2:
        return min([process_packet(subpacket) for subpacket in packet['packets']])
    elif packet['packet_type'] == 3:
        return max([process_packet(subpacket) for subpacket in packet['packets']])
    elif packet['packet_type'] == 5:
        if process_packet(packet['packets'][0]) > process_packet(packet['packets'][1]):
            return 1
        return 0
    elif packet['packet_type'] == 6:
        if process_packet(packet['packets'][0]) < process_packet(packet['packets'][1]):
            return 1
        return 0
    elif packet['packet_type'] == 7:
        if process_packet(packet['packets'][0]) == process_packet(packet['packets'][1]):
            return 1
        return 0






packets = read_one_packet(parse_data('8A004A801A8002F478'))
print(verify_length(packets[0]))
print(packets)
print(get_version_sum(packets[0]))
print(process_packet(packets[0]))
packets = read_one_packet(parse_data('620080001611562C8802118E34'))
print(verify_length(packets[0]))
print(packets)
print(get_version_sum(packets[0]))
print(process_packet(packets[0]))
packets = read_one_packet(parse_data('C0015000016115A2E0802F182340'))
print(verify_length(packets[0]))
print(packets)
print(get_version_sum(packets[0]))
print(process_packet(packets[0]))
packets = read_one_packet(parse_data('A0016C880162017C3686B18A3D4780'))
print(verify_length(packets[0]))
print(packets)
print(get_version_sum(packets[0]))
packets = read_one_packet(parse_data(DATA))
print(verify_length(packets[0]))
print(packets)
print(process_packet(packets[0]))
print(get_version_sum(packets[0]))
