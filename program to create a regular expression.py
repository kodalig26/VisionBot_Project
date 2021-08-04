import re
s = input()
PATTERN = re.compile(r'^(0|1(01*0)*1)*$')
res = PATTERN.findall(s)
if res:
	print("True")
else:
	print("False")