z=2+3*I;
z.conjugate()
bool(z.real()==(z+z.conjugate())/2)
bool(z.imag()==(z-z.conjugate())/(2*I))
bool(z.abs()==sqrt(z*z.conjugate()))
arg(z)
R.<z> = CC[] # wielomian nad cialem C
w=z^2+1
w.factor()
x = PolynomialRing(RationalField(), 'x').gen() # pierscien wielomianow nad cialem R
w = (x^3 - 1)^2-(x^2-1)^2
w.factor()
w1 = 3*x^3 + x
w2 = 9*x*(x+1)
w1.gcd(w2) # NWD wielomianow w1 oraz w2

