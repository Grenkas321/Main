import sys
import struct

name = sys.stdin.readline().strip()

try:
    f = open(name, "rb")
except OSError:
    print("NO")
    sys.exit(0)

header = f.read(12)
if len(header) < 12:
    print("NO")
    f.close()
    sys.exit(0)

chunk_id, riff_size, wave = struct.unpack("<4sI4s", header)

if chunk_id != b"RIFF" or wave != b"WAVE":
    print("NO")
    f.close()
    sys.exit(0)

audio_fmt = None
num_ch = None
sample_rate = None
bits_per_sample = None
data_size = None

while True:
    hdr = f.read(8)
    if not hdr:
        break
    if len(hdr) < 8:
        print("NO")
        f.close()
        sys.exit(0)

    sub_id, sub_size = struct.unpack("<4sI", hdr)

    if sub_id == b"fmt ":
        fmt_data = f.read(sub_size)
        if len(fmt_data) < sub_size:
            print("NO")
            f.close()
            sys.exit(0)
        if sub_size < 16:
            print("NO")
            f.close()
            sys.exit(0)

        audio_fmt, num_ch, sample_rate, byte_rate, block_align, bits_per_sample = struct.unpack(
            "<HHIIHH", fmt_data[:16]
        )
        if sub_size % 2 == 1:
            f.seek(1, 1)

    elif sub_id == b"data":
        data_size = sub_size
        if audio_fmt is not None:
            break
        skip = sub_size + (sub_size % 2)
        f.seek(skip, 1)

    else:
        skip = sub_size + (sub_size % 2)
        f.seek(skip, 1)

    if audio_fmt is not None and data_size is not None:
        break

f.close()

if audio_fmt is None or data_size is None:
    print("NO")
else:
    print(
        f"Size={riff_size}, Type={audio_fmt}, "
        f"Channels={num_ch}, Rate={sample_rate}, "
        f"Bits={bits_per_sample}, Data size={data_size}"
    )
