import json

data = json.load(open("original.json"))

def translate(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        print('Key not found !')

word = input("Enter the word you want to search : ")
output = translate(word.lower())
if type(output) == list:
    count = 1
    for item in output:
        print(f"{count}). {item}")
        count += 1
else:
    print(output)