def swapInArray( A, i, j ):
	A[i], A[j] = A[j], A[i]
		
def partition( A, p, r ):
	x = A[r]
	i = p-1
	for j in range( p, r ):
		if A[j] <= x:
			i += 1
			swapInArray( A, i, j )
	swapInArray( A, i+1, r )
	return i+1
		
def quickSort( A, p, r ):
	if p < r:
		q = partition( A, p, r )
		quickSort( A, p, q-1 )
		quickSort( A, q+1, r )
		
def readArrayFromFile( fName ):
	f = open( fName, "r" )
	A = []
	for line in f:
		A.append( int( line.rstrip() ) )
	return A
	
def writeArrayToFile( A, fName ):
	f = open( fName, "w" )
	for x in A:
		f.write( str(x) + "\n" )
	f.close()

if __name__ == "__main__":
	inputFile = "input.txt"
	outputFile = "output.txt"
	A = readArrayFromFile( inputFile )
	quickSort( A, 0, len(A)-1 )
	writeArrayToFile( A, outputFile )