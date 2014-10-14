n = raw_input("Enter the number")
l = r = n
s1 = ""

def f1(l, r, s1):
	if r == 0:
		print s1
		return
	if l>0:
		f1(l-1, r, s1 + '(')
		if l < r:
			f1(l, r-1, s1 + ')')
	else:
		f1(l, r-1, s1 + ')') 



f1(int(l), int(r), '')
