# Big o
# nlog2N

def merge_sort(a):
    if len(a) < 2:
        # when there is only 1 in  the list
        return a

    mid = len(a) // 2

    return merge(merge_sort(a[:mid]), merge_sort(a[mid:]))


def merge(l1,l2):
    if not len(l1): return l2
    if not len(l2): return l1

    merge_list = []
    l1_i = l2_i = 0
    while len(merge_list) < len(l1) + len(l2):
        if l1[l1_i] <= l2[l2_i]:
            merge_list.append(l1[l1_i])
            l1_i += 1

        else:
            merge_list.append(l2[l2_i])
            l2_i += 1

        if l1_i == len(l1):
            merge_list.extend(l2[l2_i:])
            break

        if l2_i == len(l2):
            merge_list.extend(l1[l1_i:])
            break

    return merge_list






if __name__ == '__main__':
    a = [1,3,5,7,9,2,6,8,4]
    print(merge_sort(a))
