n=int(input())
result=""
for i in range(1,n+1):
    output=2*i-1
    result=result+","+str(output)
print(result[1:])