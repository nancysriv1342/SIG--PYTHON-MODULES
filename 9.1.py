def read_lines(fname,n,mode='r+'):
	with open(fname) as f:
		for i in range(n):
			print(f.readline())

read_lines('file.txt',2)

def readnline(fname,lines,mode='r+'):
	with open(fname) as f:
		li = [ next(f) for i in range(lines)]
	print(li)

readnline('file.txt',1)
