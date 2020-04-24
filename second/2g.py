
def hits (xa, ya, xb, yb) - > bool:

if xa = = xb or ya = = yb:
 return True



x_nw, y_nw = xa, ya

while x_nw > 1 and y_nw > 1:

x_nw - = 1

y_nw - = 1

if x_nw = = xb and y_nw = = yb:
 return True



x_se, y_se = xa, ya

while x_se < 8 and y_se < 8:

x_se + = 1

y_se + = 1

if x_se = = xb and y_se = = yb:

 return True



x_sw, y_sw = xa, ya

while x_sw > 1 and y_se < 8:

x_sw - = 1

y_sw + = 1

if x_sw = = xb and y_sw = = yb:

 return True

x_ne, y_ne = xa, ya

while x_ne 1:

x_ne + = 1

y_ne - = 1

if x_ne = = xb and y_ne = = yb:

 return True

return False 

inp = [int (x) for x in input () . split () ]

if hits (*inp) :

 print ('YES')

else:

 print ('NO')
