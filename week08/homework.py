import os 

sourceDir = os.path.dirname(__file__)

text = f = open(os.path.join(sourceDir, "week8-05input.txt"))
lines = f.readlines()
for line in lines:
 words = text.split(" ")
print(f"Words: {len(words)}")
f.close()