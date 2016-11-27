f = open("counts_tiny.txt")
fre = open("result.txt")

for line in f:
	real_count = (line.strip()).split("\t")
	fre_count = fre.readline().strip().split("\t")
	err = (float(fre_count[1]) - float(real_count[1])) / int(real_count[1])
	if err < 1:
		print("%d" % real_count[0])
f.close()
fre.close()