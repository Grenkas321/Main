import pickle
import sys

class SerCls:
    def __init__(self):
        self.lst = [1, 2, 3]
        self.dct = {'a': 1, 'b': 2}
        self.num = 42
        self.st = "Hello World"

ser = SerCls()
print("Исходный объект:")
print(f"lst: {ser.lst}, dct: {ser.dct}, num: {ser.num}, st: {ser.st}")

serialized = pickle.dumps(ser)
print(f"\nСериализованная строка: {serialized}")

del ser

ser1 = pickle.loads(serialized)
print("\nВосстановленный объект ser1:")
print(f"lst: {ser1.lst}, dct: {ser1.dct}, num: {ser1.num}, st: {ser1.st}")


saved_serialized = serialized

del SerCls
del ser1

try:
    temp = pickle.loads(saved_serialized)
except Exception as e:
    print(f"Ошибка при десериализации после удаления класса: {e}")

class SerCls:
    def __init__(self):
        self.lst = [1, 2, 3]
        self.dct = {'a': 1, 'b': 2}
        self.num = 42
        self.st = "Hello World"

ser2 = pickle.loads(saved_serialized)
print("\nВосстановленный объект ser2 после пересоздания класса:")
print(f"lst: {ser2.lst}, dct: {ser2.dct}, num: {ser2.num}, st: {ser2.st}")


del SerCls
del ser2

class SerCls:
    pass

try:
    ser3 = pickle.loads(saved_serialized)
except Exception as e:
    print(f"Ошибка при десериализации с пустым классом: {e}")
