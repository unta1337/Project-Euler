def is_palindrome(s):
    return s == s[::-1]

answer = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        res = i * j

        if is_palindrome(str(res)):
            answer = max(answer, res)


print(answer)
