def ShiftRows(matrix):
	retmatrix=[]
	number=0
	for row in matrix:	
		temp=[]
		for x in range(len(matrix)):
			# print cell
			temp.append(row[(x+number)% len(row)])
		retmatrix.append(temp)
		number+=1
	return retmatrix
if __name__ == '__main__':
	matrix=[['AB', '8B', '89', '35'], ['05', '40', '7F', '7F'], ['18', '3F', 'F0', 'FC'], ['E4', '4E', '2F', 'C4']]
	print ShiftRows(matrix)