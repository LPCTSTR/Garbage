import random


def quicksort(seq):
    if len(seq) < 2:
        return seq
    else:
        base = seq[0]
        left = [elem for elem in seq[1:] if elem < base]
        right = [elem for elem in seq[1:] if elem > base]
        return quicksort(left) + [base] + quicksort(right)


def bubble_sort(seq):
    length = len(seq) - 1
    count = 1
    i = 0
    while i < length:
        j = 0
        flag = 1
        while j < length - i:
            if seq[j] > seq[j + 1]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
                flag = 0
            j += 1
        if flag:
            break
        count += 1
        print("第", count, "回: ", seq)
        i += 1
    return seq


def bubble_sort_v2(seq):
    length = len(seq) - 1
    i = 0
    count = 1
    while i < length:
        j = length
        flag = 1
        while j > i:
            if seq[j - 1] > seq[j]:
                seq[j], seq[j - 1] = seq[j - 1], seq[j]
                flag = 0
            j -= 1
        if flag:
            break
        count += 1
        print("第", count, "回: ", seq)
        i += 1
    return seq


def func(seq):
    for i in range(0, len(seq) - 1):
        flag = 1
        # rangeの使い方には、僕はちょっと間違った
        # range(a,b,step)となると、変化の範囲は[a,b)となり、すなわち、ｂが取れられないということです。
        for j in range(len(seq) - 1, i, -1):
            if seq[j - 1] > seq[j]:
                seq[j], seq[j - 1] = seq[j - 1], seq[j]
                flag = 0
        if flag:
            break

    return seq


if __name__ == '__main__':
    data = [i for i in range(1, 10)]
    random.shuffle(data)
    print("元のデータ:", data)
    print("並び替え:", func(data))
