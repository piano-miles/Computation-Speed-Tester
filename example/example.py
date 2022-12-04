from comptester import tester

# Defining parameters
test1 = 'x*x*x'  # Multiplication
test2 = 'x**3'  # Power
iterations = 100000
samples = 100

# Run the test
test = tester.test(test1, test2, iterations, samples)

# Print the test results to the console
# tester.tprint(test)

# Plot the test results
tester.plot(test)