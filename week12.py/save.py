import os 

def items():
    for item in f:
        yield item
sourceDir = os.path.dirname(__file__)
filePath = os.path.join(sourceDir, "this is it.txt")
f = open(filePath)
for item in items():
    print(item)