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
        if (sys.argv[3] != None):
            print(checks+x+str(sys.argv[3]))
            return os.popen(checks+x+str(sys.argv[3])).read()
        else:
            print(checks+x.strip())
            return os.popen(checks+x).read()
    except Exception as e:
        errors.append(str(x)+" has an error:"+str(e)+"\r")
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
        for chars in lines:
            if (tick < check):
                model.append(chars)
                tick += 1
            else:
                model.append(chars)
                x = lambda x: test(x)
                (list(map(x, model)))
                model = []
                tick = 0
tick = 0
if (sys.argv[4] != None):
    with open(sys.argv[4], "r") as lead:
        for crossed in lead:
            if (tick < check):
                model.append(crossed)
                tick += 1
            else:
                model.append(crossed)
                x = lambda x: test(x)
                (list(map(x, model)))
                model = []
                tick = 0
else:
    pass
x = lambda x: test(x)
(list(map(x, model)))
print(errors)

print("End")
lead.close()
charmap.close()
charmap2.close()
