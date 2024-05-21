n=int(input("Enter the term :"))
if n <= 0:
   print("Invalid input. Please enter a positive integer.")
elif n == 1:
    print(0)
elif n == 2:
    print(1)
else:
     a, b = 0, 1
     for _ in range(n - 2):
            a, b = b, a + b
     print(f"The nth term of the Fibonacci series is: {b}")










