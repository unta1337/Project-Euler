a = 1
b = 2

answer = 0
while a <= 4000000:
    if a % 2 == 0:
        answer += a

    c = a + b
    a = b
    b = c

print(answer)
