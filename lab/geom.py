v = vector([1,2,3]); w = vector([0,5,-9])
u = v.dot_product(w); u
v.norm(), w.norm();
alfa = arccos(v.dot_product(w) / v.norm() * w.norm()); alfa
A = matrix(QQ, 3,2, [[1,2],[3,4],[5,6]]); A
A.transpose()
(A.transpose()*A).inverse()
P = A * (A.transpose()*A).inverse() * A.transpose(); P
P*P==P
B = matrix(QQbar, [[1,-1,0,0], [0,1,-1,0], [0,0,1,-1], [1,1,1,1]]); B
Q, R = B.QR()
Q*R == B
Data = [[1,2], [-1,3], [4,1],[2,1],[1,.5]]
a, b, x = var('a b x'); model(x) = a*x + b
best = find_fit(Data, model, solution_dict=True); best
mnk = model.subs(best)
plot(mnk, (x,-1,6)) + points(Data, color='red', size=20)
