# how much space it takes in the computer


n = [None] * 1000

# O(1) space complexity
# not taking any more space of what is already taken
# just returns the existing array
def simple_function(n):
    return n


# O(n) space complexity, depends on the 
# size of the array as the input increases
def make_another_array(n):
    inner_array = []

    for i in n:
        inner_array.append(i)

    return inner_array


# O(n^2) O of n squared
def make_matrix(n):
    matrix = []

    for item in n:
        row = []

        for i in n:
            row.append(i * 2)

        matrix.append(row)


def factorial(n):
    if n == 0: 
        return 1

    return n * factorial(n - 1)

factorial(3)
# 3 * 2 * 1 * 1
