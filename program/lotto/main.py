import random
import math

lotto_size = 7

lotto_arr = []
i = 0
while i != lotto_size:
    num = math.trunc(random.random() * 45 + 1)
    if num in lotto_arr:
        continue
    lotto_arr.append(num)
    i += 1

input_arr = []
i = 0
while i != lotto_size:
    message = str(i + 1) + "번째숫자를 입력하세요:"
    input_num = int(input(message))

    if input_num in input_arr:
        print("중복된 숫자입니다. 다시 입력해주세요.")
        continue
    if input_num > 45:
        print("숫자는 45를 넘을 수 없습니다.")
        continue

    input_arr.append(input_num)
    i += 1

match_number_count = 0
for i in range(0, 7):
    if input_arr[i] in lotto_arr:
        match_number_count += 1

print(str(match_number_count) + "개의 번호가 맞았습니다.")
print("당첨 번호: ", lotto_arr)
print("입력 번호: ", input_arr)
