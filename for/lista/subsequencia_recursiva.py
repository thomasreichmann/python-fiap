lista = [0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1]
sequencia = [0, 0, 1]


def subsequence(full_list, seq, count=0):
    if len(full_list) < len(seq):
        return count

    if full_list[:len(seq)] == seq:
        count += 1

    full_list.pop(0)
    return subsequence(full_list, seq, count)


conut = subsequence(lista, sequencia)
print(conut)
