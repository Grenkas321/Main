import random
import struct

with open('data.bin', 'wb') as f:
    for i in range(10):
        float_val = random.random()
        bytes_val = bytes(random.sample(range(256), 3))
        int_val = random.randrange(10000)

        packed_data = struct.pack('f3si', float_val, bytes_val, int_val)
        f.write(packed_data)


triples = []
with open('data.bin', 'rb') as f:
    while True:
        data = f.read(12)
        if not data:
            break

        float_val, bytes_val, int_val = struct.unpack('f3si', data)
        triples.append((float_val, bytes_val, int_val))

for i, (f_val, b_val, i_val) in enumerate(triples, 1):
    print(f"{i}: float={f_val:.6f}, bytes={b_val}, int={i_val}")

with open('data_network.bin', 'wb') as f:
    for float_val, bytes_val, int_val in triples:
        packed_data = struct.pack('f3si', float_val, bytes_val, int_val)
        f.write(packed_data)

