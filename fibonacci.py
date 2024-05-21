#To print fibonacci series

n = int(input("Enter th term :"))
a=0
b=1
print(a,end=' ')
print(b,end=' ')

if n<=0:
  print("write a positive number")

elif n==1:
  print(0)

else:
  for _ in range(2,n):
    c = a+b
    a = b
    b = c
    print(c,end=' ')

#To print the nth term of fibonacci series

# n = int(input("Enter the term"))

# if n<= 0:
#   print("invalid input please enter a positive integer")
# elif n== 1:
#   print(0)
# elif n== 2:
#   print(1)
# else:
#   a,b = 0, 1
#   for _ in range(n-2):
#     a,b = b, a+b
#   print(f"The nth term of the fibonacci series is: {b}")        

