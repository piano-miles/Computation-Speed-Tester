from comptester import tester

# Defining parameters
multiplication = "x*x*x*x*x*x"  # Compute x^6 by multiplication
power = "x**6"                  # Compute x^6 by power
iteration_count = 100000        # Number of times each expression is tested in a sample
samples = 100                   # Number of samples to collect

# Run the test and store it in the 'test' variable
test = tester.test(
    expr1=multiplication,
    expr2=power,
    iters=iteration_count,
    sample_count=samples,
)

# Print the test results to the console
# tester.tprint(test)

# Plot the test results
tester.plot(test)
