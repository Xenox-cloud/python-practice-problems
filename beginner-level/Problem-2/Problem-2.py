Input= "Data Science is awesome"
vowels= ['a', 'e', 'i', 'o', 'u']
count = 0
for x in Input.lower():
    for y in vowels:
        if x == y:
            count+=1
        else:
            pass
print(count)