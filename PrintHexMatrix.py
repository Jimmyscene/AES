def PrintHexMatrix(Matrix):
	for row in Matrix:
		print "[",
		for cell in row:
			print format(cell)+",",
		print "]"
