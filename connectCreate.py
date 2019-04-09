import sys
import glob

ports = glob.glob('/dev/tty[A=Za-a]*')

for port in ports:
	print(port)imn


