from comptester import tester

# Defining parameters
test1 = 'x*x*x*x*x*x'  # Compute x^6 by multiplication
test2 = 'x**6'  # Compute x^6 by power
iterations = 100000  # Number of times each expression is tested in a sample
samples = 100  # Number of samples to collect

# Run the test and store it in the 'test' variable
test = tester.test(test1, test2, iterations, samples)

# Print the test results to the console
# tester.tprint(test)

# Plot the test results
tester.plot(test)
