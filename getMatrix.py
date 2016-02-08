'''
Takes a string of plaintext and converts it to a 4x4 list of lists of type: String in Hex Format
'''
def getMatrix(Plaintext):
	retmatrix=[]
	for x in range(4):
		temp=[]
		for y in range(4):
			temp.append(Plaintext[8*x+2*y]+Plaintext[8*x+2*y+1])
		retmatrix.append(temp)
	retmatrix= [list(x) for x in zip(*retmatrix)]
	return retmatrix
if __name__ == '__main__':
	print getMatrix("0123456789ABCDEFFEDCBA9876543210")