import numpy,time
matrix = [[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]
size = len(matrix)

t1 = time.monotonic()
M = numpy.matrix(matrix)
mDet = numpy.linalg.det(M)
print (mDet);
t2 = time.monotonic()

def determinant (matrix,n):
	if (n==2):
		return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix [1] [0] 
	else:
		total = 0
		sign = 1
		for x in range (0,n):
			subMatrix = list()
			for r in range (1,n):
				t = list()
				for c in range (0, n):
					t.append(matrix[r][c])
				subMatrix.append(t)
			for row in subMatrix:
				del row[x]
			total += (sign*matrix[0][x]*determinant(subMatrix,n-1))
			sign*=-1;
		return total

a = determinant(matrix,size)
print (a);
t3 = time.monotonic()
print (a,t2-t1, "<-numpy", t3-t2, "<-recursive")
print ("numpy is ", (t3 - t2) /(t2 - t1) ,"times faster")

