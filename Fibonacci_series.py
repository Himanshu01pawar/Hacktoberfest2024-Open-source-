def fibonacci(n):
    fib_series = [0, 1]
    for i in range(2, n):
        next_num = fib_series[i-1] + fib_series[i-2]
        fib_series.append(next_num)
    return fib_series

# Get input from user
num_terms = int(input("Enter the number of terms in the Fibonacci series: "))

# Generate the Fibonacci series
if num_terms <= 0:
    print("Please enter a positive integer.")
elif num_terms == 1:
    print([0])
else:
    fib_series = fibonacci(num_terms)
    print(f"Fibonacci series with {num_terms} terms: {fib_series}")
