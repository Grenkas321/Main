array = eval(input())
if (len(array)%2):
    print("ERROR!!!!")
len_new = len(array)//2
new_arr = array[len_new:]

answer = new_arr[-1::-2]
print(answer)
