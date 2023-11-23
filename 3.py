def fnc(a, **b):
  sum = 0
  for k in b:
    print(k)
    sum += k
    print(sum)
  return sum

result = fnc(10, k=1, m=2, n=3, j=4)
print(result)