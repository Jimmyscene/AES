from KeyExpansion import KeyExpansion 
from getMatrix import getMatrix
'''
	Matrix is a list of lists, returns list of lists
	Inner lists are of type: String in Hex Format
'''
def AddRoundKey(matrix, key, Round):
	
	roundkey=KeyExpansion(key)[Round]
	retmatrix=[]
	for i in range(len(matrix)):
		temp=[]
		for j in range(len(matrix)):
			temp.append(format(int(matrix[i][j],16)^int(roundkey[i][j],16),'02X'))
		retmatrix.append(temp)
	return retmatrix


if __name__ == '__main__':
   	text="0123456789ABCDEFFEDCBA9876543210"
	text=getMatrix(text)
	key="0f1571c947d9e8590cb7add6af7f6798"
	print AddRoundKey(text,key,0)