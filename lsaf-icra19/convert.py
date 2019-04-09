import sys

if len(sys.argv) < 3:
    print 'python convert [input file] [output file]'
    exit(1)

ifile = open(sys.argv[1], 'r')
ofile = open(sys.argv[2], 'w')

voltages, currents = [], []
while True:
    char = ifile.read(27)
    if not char:
        break
    v_str, c_str = char[9:14], char[18:23]
    voltage, current = '0x' + ''.join(v_str.split(' ')), '0x' + ''.join(c_str.split(' '))
    voltages.append(voltage)
    currents.append(current)
ifile.close()

for i, vol in enumerate(voltages):
    try:
        voltages[i] = int(vol, 16)
    except Exception as e:
        voltages[i] = 0

for i, cur in enumerate(currents):
    try:
        val = int(cur, 16)
        if val > 0x7FFF:
            val = -((0xFFFF ^ val) + 1)
        currents[i] = val
    except Exception as e:
        currents[i] = 0

power = -1
for i in range(len(voltages)):
    if currents[i] > 0:
        continue
    power = max(power, abs(voltages[i] * currents[i]) / 1000000.0)
    ofile.write('%d,%d,%.2f\n' % (voltages[i], currents[i], abs(voltages[i] * currents[i]) / 1000000.0))

ofile.close()
