
content = list(input("provide a word or sentence \n"))

vowels = ['a','e','i','o','u']
number = 0

for word in content:

    if word in vowels:
        number += 1
    else:
        number

print(content)
print(f'number of vowels is {number}')