def fib(n):
    a=0
    b=1
    
    if n==1:
        print(a,end=' ')
    
    else :
        print(a,end=' ')
        print(b,end=' ')
        
        for i in range(2,n):
            c=a+b
            print(c,end=' ')
            a=b
            b=c
fib(5)            