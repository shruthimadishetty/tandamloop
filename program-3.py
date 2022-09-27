def series(n):
    if n<=2:
        return 1
    else:
        result=""
        for i in range(1,n+1):
            output=2*i-1
            result=result+","+str(output)
    return result[1:]
n=int(input())
print(series(n))