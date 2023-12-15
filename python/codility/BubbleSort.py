def bubble_sort(a):
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    return a

def reverse_bubble_sort(a):
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] < a[j]:
                a[i], a[j] = a[j], a[i]
    return a
if __name__ == '__main__':
    a = [1,4,2,3,5,9,8,6,7]
    print(bubble_sort(a))
    print(reverse_bubble_sort(a))
