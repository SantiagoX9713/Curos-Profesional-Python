# Quitar duplicados de una lista
def remove_duplicates(my_list):
    without_duplicates = []
    for i in my_list:
        if i not in without_duplicates:
            without_duplicates.append(i)
    return without_duplicates


def remove_duplicates_sets(my_list):
    new_list = set(my_list)
    return list(new_list)


if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5, 5, 4, 1, ]
    print(remove_duplicates(my_list))
    print(remove_duplicates_sets(my_list))