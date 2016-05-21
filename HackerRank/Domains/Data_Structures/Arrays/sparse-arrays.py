#!/usr/bin/env python3

N = int(input())

memory = []
for each in range(N):
    memory.append(input())

Q = int(input())
for each in range(Q):
    query = input()
    if query not in memory:
        print(0)
    else:
        print(
            memory.count(query)
        )
