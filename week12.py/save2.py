import os 

def items (f, prefix):
    for item in f:
        if item.startswith(prefix):
            yield item
sourceDir = os.path.dirname(__file__)
filePath = os.path.join(sourceDir, "words_dictionary.json")
f = open(filePath)
for item in items(f, "b"):
    print(item)