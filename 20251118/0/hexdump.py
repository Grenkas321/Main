import sys

def hexdump(filename):
    try:
        with open(filename, 'rb') as file:
            offset = 0
            while True:
                chunk = file.read(16)
                if not chunk:
                    break
                
                hex_part = ' '.join(f'{b:02x}' for b in chunk)
                ascii_part = ''.join(chr(b) if 32 <= b <= 126 else '.' for b in chunk)

                print(f'{offset:08x}: {hex_part:<48} {ascii_part}')
                
                offset += len(chunk)
                
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    
    hexdump(sys.argv[1])