import math

w, h = 7, 7
Movie = [[0 for x in range(w)] for y in range(h)] 

Movie[1][0] = 1
Movie[2][0] = 2
Movie[3][0] = 3
Movie[4][0] = 4
Movie[5][0] = 5
Movie[6][0] = 6

Movie[1][1] = 2
Movie[1][4] = 4
Movie[1][5] = 5

Movie[2][1] = 5
Movie[2][3] = 4
Movie[2][6] = 1

Movie[3][3] = 5
Movie[3][5] = 2

Movie[4][2] = 1
Movie[4][4] = 5
Movie[4][6] = 4

Movie[5][3] = 4
Movie[5][6] = 2

Movie[6][1] = 4
Movie[6][2] = 5
Movie[6][4] = 1

def cekTetangga(A):
	X =[]
	for i in xrange(1,7):
		if Movie[A][i] != 0:
			for j in xrange(1,7):
				if j != A:
					if Movie[j][i] != 0:				
						cek = False							
						for l in xrange(0,len(X)):
							if X[l] == Movie[j][0]:
								cek = True
						if cek == False :
							X.append(Movie[j][0])
	return X

# print cekTetangga(4)

def cekAverage(A):
	x = 0.0
	y = 0
	for i in xrange(1,7):
		if Movie[A][i] != 0:
			x = x + Movie[A][i]
			y = y + 1
	return x/y

# print cekAverage(3)

def cekSim(A,B):
	x = 0.0
	ya = 0.0
	yb = 0.0
	yy = 0.0
	for i in xrange(1,7):
		if Movie[A][i] != 0 :
			if Movie[B][i] != 0:
				x = x + ((Movie[A][i] - cekAverage(A))*(Movie[B][i] - cekAverage(B)))
				ya = ya + (Movie[A][i] - cekAverage(A))**2
				yb = yb + (Movie[B][i] - cekAverage(B))**2	
	yy = math.sqrt(ya * yb)
	if x == 0:
		return 0
	else :
		return x/yy

# print cekSim(4,2)

def predictRating(A,B):
	avg = cekAverage(A)
	x = 0.0
	y = 0.0
	tetangga = cekTetangga(A)
	panjang = len(tetangga)
	for j in xrange(0,panjang):
		y = y + abs(cekSim(A,tetangga[j]))
		if Movie[tetangga[j]][B] != 0 :
			x = x + (cekSim(A,tetangga[j])*(Movie[tetangga[j]][B]-cekAverage(tetangga[j])))		
	if Movie[A][B] != 0 :
		return Movie[A][B]
	else :
		return (x/y)+avg

print predictRating(4,1)
