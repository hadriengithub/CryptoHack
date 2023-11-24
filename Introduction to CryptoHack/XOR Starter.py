given="label"
key=13
print("crypto{",end="")
for x in given:
	print(chr(ord(x)^key),end="")
print("}")
