import os 

def items (f, prefix, diction):
    for item in f:
        if item.startswith(prefix) or diction in item:
            yield item + ":)"
sourceDir = os.path.dirname(__file__)
filePath = os.path.join(sourceDir, "words_dictionary.json")
f = open(filePath)
for item in items(f,"l", "x"):
    print(item)
f.close
