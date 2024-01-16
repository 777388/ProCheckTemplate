import sys
import os
checks = sys.argv[1]
firstcharmap = "test1.txt"
secondcharmap = "test.txt"
check = int(sys.argv[2])
tick = 0
model = []
errors = []
output = []
def test(x):
    try:
        return os.popen(checks+" "+x).read()
    except Exception as e:
        errors.append(x+" has an error:"+str(e)+"\r")
        pass

with open(firstcharmap, "r") as charmap:
    for line in charmap:
        for char in line:
            if (tick < check):
                model.append(char)
                tick += 1
            else:
                model.append(char)
                x = lambda x: test(x)
                (list(map(x, model)))
                model = []
                tick = 0
tick = 0
with open(secondcharmap, "r") as charmap2:
    for lines in charmap2:
        for chars in line:
            if (tick < check):
                model.append(chars)
                tick += 1
            else:
                model.append(char)
                x = lambda x: test(x)
                (list(map(x, model)))
                model = []
                tick = 0

print(errors)

print("End")

charmap.close()
charmap2.close()
