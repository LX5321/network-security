import itertools


def splitter(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def multiplier(array):
    print(array)
    for i in range(2):
        mul = 0
        for j in range(2):
            mul = matrix[i][j]*array[i][j]+mul
            print(matrix[i][j],array[i][j])
            print(mul, "\n")
    return mul


charList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
            "y", "z"]

# define matrix
global matrix
matrix = [[7, 8], [1, 1]]
print(matrix)

# get text from user for key
key = input('Enter Key: ')

# remove spaces from key
key = key.replace(" ", "")

# convert user input into numbers
numberGrid = []
for x in key:
    numberGrid.append(charList.index(x))

# call splitter and convert into 2 matrix
numberGrid = list(splitter(numberGrid, 2))

print(multiplier(numberGrid))
