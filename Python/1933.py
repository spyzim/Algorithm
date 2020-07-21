# 간단한 N 의 약수

N = int(input())

for i in range(N):
    if N % (i+1) == 0:
        print(i+1, end=" ")

# 튜플로 짝을 맺은 후, sort 로 오름차순 정렬을 하여 출력하는 것 -> 파이토닉
