import os 

sourceDir = os.path.dirname(__file__)
text = f = open(os.path.join(sourceDir, "week8-05input.txt"))
words = text.split("")
lines = f.readlines()
for line in lines:
    print(f"Words: {len(words)}")
f.close()