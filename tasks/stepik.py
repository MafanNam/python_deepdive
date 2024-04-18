# 1
n = int(input())
fields = []

for i in range(n):
    field = input()
    fields.append(field)

k = int(input())
words_search = []

for i in range(k):
    word = input().lower()
    words_search.append(word)

res = []

for field in fields:
    flag = False
    for word in words_search:
        if word in field.lower():
            flag = True
        else:
            flag = False
            break
    if flag:
        res.append(field)

print(*res, sep='\n')

# 2
n = int(input())
fields = [input() for i in range(n)]

k = int(input())
words_search = [input().lower() for i in range(k)]

res = []

for field in fields:
    if all(word in field.lower() for word in words_search):
        res.append(field)

print(*res, sep='\n')

# 3
fields = [input() for i in range(int(input()))]
words_search = [input().lower() for i in range(int(input()))]

res = [field for field in fields if all(word in field.lower() for word in words_search)]
print(res, sep='\n')

# 4
fields = [input() for i in range(int(input()))]
words_search = [input().lower() for i in range(int(input()))]
[print(field) for field in fields if all(word in field.lower() for word in words_search)]
