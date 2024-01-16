import sys

checks = sys.argv[1]
firstcharmap = "test1.txt"
secondcharmap = "test.txt"
check = sys.argv[2]
tick = 0
model = []
with open(str(check)+"_"str(checks)+"_procheck.txt", "a") as c:
    with open(firstcharmap, "r") as charmap:
        for line in charmap:
            for char in line:
                if (tick < check):
                    model.append(char)
                    tick += 1
                else:
                    model.append(char)
                    x = lambda x: c.write(os.popen(checks+" "+x).read())
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
                    x = lambda x: c.write(os.popen(checks+" "+x).read())
                    (list(map(x, model)))
                    model = []
                    tick = 0
