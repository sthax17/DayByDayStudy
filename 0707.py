# -*- coding: utf-8 -*-
"""0707.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18BI8TFOAWCzlPL2TYb9GGPhR8LtzjGdD
"""

N, X = map(int, input().split())
A = list(map(int, input().split()))
for i in range(N):
    if A[i] < X:
        print(A[i], end=" ")

n = int(input())
for i in range(1, n+1):
  print("*" * i)

n = int(input())
for i in range(1, n+1):
  print(" "*(n-i), "*"*i)

n = int(input())
for i in range(1, n+1):
  print(" "*(n-i) + "*"*i)

i = 0
while i < 6:
  a, b = map(int, input().split())  
  print(a + b)
  if i < 6:
    break
i += 1

while(True):
    A, B = list(map(int, input().split()))
    if(A == 0 and B == 0):
        break
    else:
        print(A + B)

i = 0
while i < 5:
  A, B = map(int, input().split())
  print(A + B)


  if i > 5:
    break
  i += 1

while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break

n = int(input())
num = n 
cnt = 0

while True:
  a = num // 10 
  b = num % 10
  c = (a + b) % 10
  num = (b * 10) + c

  cnt += 1

  if num == n:
    break

print(cnt)

a = int(input())
b = list(map(int,input().split()))
print(min(b), max(b))

num_list = []
for i in range(9):
  num_list.append(int(input()))

print(max(num_list))
print(num_list.index(max(num_list))+1)

a = int(input())
b = int(input())
c = int(input())
result = list(str(a * b * c))
for i in range(10):
  print(result.count(str(i)))

n = []
for i in range(10):
  a = int(input())
  b = a % 42
  n.append(b)

s = set(n)
print(len(s))