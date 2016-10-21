filename = "Countries"
f = open(filename + ".txt", 'r')
lines = f.readlines()
f.close()

print lines

outText = filename + " = [\n"

for line in lines:
    if line[0] == '#':
        outText += "          "+line
    elif line != '\n':
        outText += "          " + '"'
        for c in line:
            if c == '\n' or c == '(':
                outText += '",\n'
                break
            else:
                outText += c

outText = outText[:-2] + "]"
  
print outText

f = open(filename+".py", 'w')
f.write(outText)
f.close()
