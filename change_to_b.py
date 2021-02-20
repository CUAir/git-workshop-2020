f = open("myfile.txt", "r")
contents = f.read()
print(contents)

results = ""
vowels = "aeiou"

for char in contents:
    if char in vowels:
        results += "b"
    else:
        results += char

e = open("myfile.txt", "w")
e.truncate(0)
e.write(results)
