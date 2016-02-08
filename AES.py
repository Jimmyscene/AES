from PrintHexMatrix import PrintHexMatrix 
from getMatrix import getMatrix
from AddRoundKey import AddRoundKey
from MixCols import MixCols
from ShiftRows import ShiftRows
from SubBytes import SubBytes
def AES(Key, Matrix):
	state=AddRoundKey(Matrix,Key,0)

	for x in range(1,10):
			state=AddRoundKey(MixCols(ShiftRows(SubBytes(state))),Key,x)
	return AddRoundKey(ShiftRows(SubBytes(state)),key,10)

if __name__ == '__main__':
	text="000102030405060708090A0B0C0D0E0F"
	text=getMatrix(text)

	key="01010101010101010101010101010101"
	PrintHexMatrix(AES(key,text))