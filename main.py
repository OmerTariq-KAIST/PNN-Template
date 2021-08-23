import numpy as np
from numpy.lib.function_base import gradient
from random import seed
from random import randint

np.random.seed(1)  #


# Global Variable


def run_PNN():
    print("PNN Program is Started........... !!!")
    # Run PNN Code from here

    print("PNN Program is Ended Successfully !!!")


def run_test():
    print("Test Program is Started........... !!!")
    # Run Test Code

    print("Test Program is Ended Successfully !!!")


# Run the main program from here
def run():
    print("Program is Started........... !!!")
    print("Run Program Here")
    run_test()
    run_PNN()
    print("Program is Ended Successfully !!!")


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('Bilal')
    run()