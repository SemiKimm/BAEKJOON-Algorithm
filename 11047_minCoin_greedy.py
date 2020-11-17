# --첫 시도 (결과는 맞지만 A의 입력 방식 다름)--
# N,K=input().split()
# N = int(N)
# K = int(K)
# A = []
# for i in range(0, N):
#     A.append(0)
#     if i == 0:
#         A[i] = 1
#         print(A[i])
#     elif i == 1:
#         A[i] = 5
#         print(A[i])
#     else:
#         if i % 2 == 0:
#             A[i] = A[i-1]*2
#         elif i % 2 == 1:
#             A[i] = A[i-1]*5
#         print(A[i])
# money = 0
# coin = 0
# l = N-1
# while money < K and l > -1:
#     if A[l] < K and K-money >= A[l]:
#         money = money+A[l]
#         coin = coin + 1
#     else:
#         l = l-1
# print(coin)

# --결과는 맞지만 채점 시간초과--
# N, K = map(int, input().split())
# A = []
# for i in range(N):
#     A.append(int(input()))
# money = 0
# coin = 0
# l = N-1
# while money < K:
#     if K-money >= A[l]:
#         money = money+A[l]
#         coin = coin + 1
#     else:
#         l = l-1
# print(coin)

#!최종 제출 정답 소스!
N, K = map(int, input().split())
A = []
for i in range(N):
    A.append(int(input()))
coin = 0
for i in range(N-1, -1, -1):
    if K == 0:
        break
    if K >= A[i]:
        coin = coin+K//A[i]
        K = K % A[i]
print(coin)
