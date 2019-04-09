file = open('stream.txt', 'r')
out = open('done.txt', 'w')
lines = []
while True:
    char = file.read(27)
    if not char:
        break
    print(char)
    voltage, current = char[9:14], char[15:20]

print(lines)
lines1 = []
for i in lines:
    res = []
    for j in i:
        num = "0x"
        for k in j:
            num += k
        print(num)
        try:
            res.append(int(num, 16))
        except:
            pass
    lines1.append(res)

for i in lines1:
    try: 
	s = i[1]
	if (s & 0x8000) == 0x8000:
	    s = -((s^0xffff) + 1)
        out.write("%d %d\n" % (i[0], s))
    except:
        pass
        
file.close()
out.close()

#def s16(value):
#    return -(value & 0x8000) | (value & 0x7fff)

