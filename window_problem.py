# import dependencies
from math import ceil, floor


# returns a tuple that shows the proper domain regarding the input parameters
def create_tuple(current_page, number_all_pages, window_size):
    if current_page <= window_size / 2:
        return (1, window_size)
    if current_page >= (number_all_pages - window_size / 2):
        return (number_all_pages - window_size + 1, number_all_pages)
    return (current_page-window_size / 2, current_page+window_size / 2)


# generate a range in regard of the input domain
def create_list(current_page, number_all_pages, window_size):
    (start, end) = create_tuple(current_page, number_all_pages, window_size)

    return [n for n in range(ceil(start), floor(end) + 1)]


def assert_value(thing, expected):
    if thing != expected:
        print(f"expected: {expected} but got {thing}")
    else:
        print(f"Passed {thing}")


assert_value(create_list(1, 100, 5), [1, 2, 3, 4, 5])
assert_value(create_list(2, 100, 5), [1, 2, 3, 4, 5])
assert_value(create_list(3, 100, 5), [1, 2, 3, 4, 5])
assert_value(create_list(4, 100, 5), [2, 3, 4, 5, 6])
assert_value(create_list(5, 100, 5), [3, 4, 5, 6, 7])

assert_value(create_list(50, 100, 5), [48, 49, 50, 51, 52])

assert_value(create_list(99, 100, 5), [96, 97, 98, 99, 100])
assert_value(create_list(100, 100, 5), [96, 97, 98, 99, 100])
