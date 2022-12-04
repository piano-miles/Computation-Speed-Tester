# Computation-Speed-Tester
A simple python module to test the computation speed of different expressions.
 - E.g., does `x*x*x*x*x*x` or `x**6` run faster?

## Dependencies
Uses random, time, matplotlib, and tqdm. To install dependencies, run `python3 -m pip install matplotlib tqdm` in the commandline.

## Usage
See the `main.py` file for an example of how to use the module. 
 - The `test` method will perform a test given two expressions, a number of iterations per expression per sample, and a number of total samples to run.
 - The `tprint` method will print the data from the test.
 - The `plot` method will plot the data so you can see visually how the expressions compare against each other and a control.
