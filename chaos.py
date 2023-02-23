# File: chaos.py
# A simple program illustrating chaotic (mathematical) behavior.
import math

def main(args: list[str]) -> int:
    print('This program illustrates a chaotic function.')
    filename: str = input('Please enter a filename to read seeds from: ')

    EPSILON: float = 0.000001 # Really small value

    try:
        with open(filename, 'r') as infile:
            with open('chaos-out.txt', 'w') as outfile:
                for line in infile.readlines():
                    try:
                        numbers: list[str] = line.split()
                        #if len(numbers) < 2:
                        #    raise ValueError()
                        x: float = float(numbers[0]) # Seed.  Functions as an accumulator variable.
                        if x < 0 or x > 1:
                            raise ValueError('Seed ' + str(x) + ' must be in the range 0 < x < 1.')
                        n: int = int(numbers[1])     # Number of iterations
                    except IndexError: # Fewer than two numbers
                        print('PROBLEM: input line "' + line[:-1] + '" does not have *two* numbers.')
                    except ValueError as e: # One of the numbers wasn't a number
                        if e.args[0].startswith('could not convert') or e.args[0].startswith('invalid literal'): # One of the numbers wasn't a number
                            print('PROBLEM: input line "' + line[:-1] + '" does not have two *numbers*.')
                        else:
                            print(e.args[0])
                    else:

                        # Clamp x to the range [0, 1], in case the user didn't
                        # x = min(x, 1 - EPSILON) # Handles x too big
                        # x = max(x, 0 + EPSILON) # Handles x too small

                        outfile.write('\n')
                        outfile.write(' i\t    x\n')
                        outfile.write('-' * 20 + '\n')
                        # Loop (definite)
                        # for i in range(n): # i is an int
                        # Indefinite-loop equivalent
                        i: int = 0
                        while i < n:
                            # Each time through the loop, the accumulator variable
                            # is modified to include the next piece of answer.
                            x = 3.9 * x * (1 - x)
                            outfile.write('{0:>3d}\t{1:0.6f}\n'.format(i+1,x))
                        
                            # For indefinite loop.
                            # Forget this (easy to do!), and you have an infinite loop.
                            i = i + 1

    except FileNotFoundError: # input file couldn't be found
        print('File "' + filename +'" could not be found.  Did you mistype the filename?')
    except IOError as e: # General I/O errors when reading or writing the files
        print(e)

    return 0  # Conventional return value for successful completion

if __name__ == '__main__':
    import sys
    main(sys.argv)
