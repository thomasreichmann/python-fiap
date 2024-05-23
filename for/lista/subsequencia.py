def sub_sequence(full_list, sub_list):
    indexes_found = []

    matches = 0
    for i in range(len(full_list)):
        if i + len(sub_list) - 1 > len(full_list) - 1:
            break

        check = []
        for j in range(len(sub_list)):
            check.append(full_list[i + j])

        if check == sub_list:
            indexes_found.append(i)
            matches += 1

    print(f"matches found: {matches}")
    print(f"at indexes: {indexes_found}")


lista = [0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1]
sub = [0, 0, 1]

sub_sequence(lista, sub)
