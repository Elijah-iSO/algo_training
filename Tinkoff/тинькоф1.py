T = 'TINKOFF'

count = int(input())

for i in range(count):
    letters = str(input())
    if letters.translate({ord(i): None for i in T}) or len(letters) > len(T):
        print('No')
    else:
        print('Yes')
