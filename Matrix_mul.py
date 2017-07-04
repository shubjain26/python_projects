a = [[1,2,3],
     [4,5,6],
     [7,8,9]]

b = [[1,2,3],
     [4,5,6],
     [7,8,9]]
status = True

# calculate rows in a
a_rows = len(a)
a_cols = len(a[0])

#calculate columns in a
if status:
  for row in a:
    if len(row)!= a_cols:
      status = False
      print('matrix a is not uniform....hence cannot be multiplied')


# calculate rows in b
b_rows = len(b)
b_cols = len(b[0])

if status:
  for row in b:
    if len(row)!= b_cols:
      status = False
      print('matrix b is not uniform.....hence cannot be multiplied')

if status:
  if a_cols != b_rows:
    status = False
    print "Matrix size error, hence cannot be multiplied"
  else:
    print "matrix size OK ...can be multiplied"

# if status:
c_rows,c_cols = a_rows,b_cols

c = [[0 for i in range(3)] for j in range(3)]

if status:
  for i in range(c_rows):
    for j in range(c_cols):
      for k in range(a_cols):
        c[i][j] = c[i][j] + (a[i][k] * b[k][j])

print c
