numbers=range(10)  # it takes the numeber from 0 to 9


def print_numbers(num):
    for n in num:
        print(n,end=' ')
even_numbers=numbers[::2]
print('\nThe even number are:  ')
print_numbers(even_numbers)


reverese_numbers=numbers[::-1]
print('\nThe reverese number are:  ')
print_numbers(reverese_numbers)

range_numbers=numbers[1:3]
print('\nThe numbers from range 1 to 3 are:  ')
print_numbers(range_numbers)

slice_numbers=range(10)[slice(0, 10, 2)]
print('\nThe sliced numbers from range 1 to 10 are:  ')
print_numbers(slice_numbers)




