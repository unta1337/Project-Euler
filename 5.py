from math import lcm

answer = 1
for i in range(1, 21):
    answer = lcm(answer, i)

print(answer)
