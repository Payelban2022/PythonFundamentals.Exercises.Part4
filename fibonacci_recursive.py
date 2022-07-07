def recur_fibonacci(n):
    if n <= 1:
        return n
    else:
        return (recur_fibonacci(n-1) + recur_fibonacci(n-2))
nterms = int(input("How many terms"))
if nterms <= 0:
    print("Please enter a positive no.")
else:
    print("Fibonacci Sequence:")
    for i in range(nterms):
        print(recur_fibonacci(i))

