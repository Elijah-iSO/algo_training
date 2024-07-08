cases = int(input())

for i in range(cases):
    d_count = int(input())
    a_i = [int(i) for i in input().split()]
    if d_count < 2 or sum(a_i) % 2 == 0:
        print('Yes')
    else:
        print('No')



# Определите, можно ли наладить контакт между какими-то парами разработчиков,
# так чтобы любые два контактировали либо напрямую,
# либо через других разработчиков.
