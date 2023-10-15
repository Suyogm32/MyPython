inp1 = input("Enter the list 1\n")
inp2 = input("Enter the list 2\n")

lst1 = list(map(int, inp1.split(" ")))
lst2 = list(map(int, inp2.split(" ")))


def is_sublist(lst1, lst2):
    matched = False
    for i in range(len(lst1) - len(lst2) + 1):
        if lst1[i] == lst2[0]:
            matched = True
            for j in range(len(lst2)):
                if lst1[i + j] != lst2[j]:
                    matched = False

    return matched


print(is_sublist(lst1, lst2))