number_id = "".join(list(map(str, input().strip().split('-'))))
sum_number_id = 0
for i in range(len(number_id), 1, -1):
  sum_number_id += int(number_id[13-i]) * i
sum_number_id %= 11
sum_number_id = 11 - sum_number_id if sum_number_id > 1 else 1 - sum_number_id
result = "Wrong NO." if (sum_number_id != int(number_id[-1])) else "Maybe right"
print(result)