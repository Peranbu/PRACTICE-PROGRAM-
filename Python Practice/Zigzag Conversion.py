def convert(s,numRows):
  if numRows==1 or numRows>=len(s):
    return s
  rows=[[] for row in range(numRows)]
  index=0
  step=-1
  for char in s:
    rows[index].append(char)    #
    if index==0:
      step=1
    elif index==numRows-1:
      step=-1
    index+=step
  for i in range(numRows):
    rows[i]=''.join(rows[i])
  return ''.join(rows)  #

s=input(" ")
numRows=int(input(" "))
print(convert(s,numRows))

#input == PAYPALISHIRING
#rows=4
#output == PINALSIGYAHRPI

P    I    N 
A  L S  I G 
Y A  H R
P    I
