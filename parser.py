import re

f = open("a.html", "r")

lines = f.readlines()
a = []
for x in lines:
	if "ctl00_ContentView_rn" in x:
		

		if "</a></td>" in x[-10:]:
			#print(x)

			r1 = re.findall(r"document\.getElementById\(\'ctl00_ContentView_rn[0-9]+", x)
			r2 = re.findall(r"rn[0-9]+", r1[0])

			a.append(r2[0][2:])

print(a)
