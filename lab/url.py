A = matrix(QQ, [[1,0,2,3], [1,3,2,0], [2,0,4,9]])
b = vector([2,5,10])
X = A.augment(b, subdivide=True).rref()
x0 = vector([-4, 3, 0, 2])
A*x0 == b #spr
A.right_kernel() #r-nia jednorodne
sol = vector([-2, 0, 1, 0])
A*sol == 0 #spr
a = var('a')
sol = x0 + a * sol
A*sol == b #spr

