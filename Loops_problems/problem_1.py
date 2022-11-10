num = int(input("Enter a number: "))

for i in range(num):
    if i % 2 != 0:
        print(f'{i}', end=', ')
print(num)
