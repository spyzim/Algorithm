n=input()
sum=0

for i in range(len(n)):
    sum+=int(n[i])

print(sum)

"""
answer = 0
while n > 10:
    r = n % 10
    answer += r
    n = n // 10

answer += n
print(answer)
"""