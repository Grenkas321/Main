h = 0
gas = 0
water = 0
w = 0

while s := input():
    h += 1
    if s.find('.') == -1 and s.find('~') == -1:
        if w > 0: break
        w = s.count('#')
    gas += s.count('.')
    water += s.count('~')


V = gas + water

for i in range(w):
    if i == 0 or i == w - 1:
        print('#' * h)
        continue
    if gas > 0:
        print(f"#{'.' * (h-2)}#")
        gas -= h - 2
    else:
        print(f"#{'~' * (h-2)}#")

m = max(water, V - water)
print(f'{'.' * round(20 * (V - water) / m):20} {str(V - water) + '/' + str(V) :>5}')
print(f'{'~' * round(20 * (water / m)):20} {str(water) + '/' + str(V):>5}')
