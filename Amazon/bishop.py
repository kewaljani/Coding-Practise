A= 4
B = 4

lbsetps = min(A-1,B-1)
rbsteps = min(8-A,B-1)
ltsteps = min(A-1,8-B)
rtsteps = min(8-A,8-B)
sum = lbsetps+rbsteps+ltsteps+rtsteps
print(sum) 
