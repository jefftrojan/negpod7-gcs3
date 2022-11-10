string = input("Enter a word: ").lower().strip()
vowels = ['a', 'e', 'i', 'o', 'u','y']
for i in string:
    if i not in vowels:
        print(i, end=', ')
    else:
        continue