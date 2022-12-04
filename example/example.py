import comptester

# Defining parameters
test1 = 'x*x*x'  # Multiplication
test2 = 'x**3'  # Power
iterations = 100000
samples = 100

# Run the test
test = comptester.test(test1, test2, iterations, samples)

# Print the test results to the console
# comptester.tprint(test)

# Plot the test results
comptester.plot(test)