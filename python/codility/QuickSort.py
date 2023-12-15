import random
def quick_sort(a):

    if len(a) < 2:
        return a
    
    lower_l = []
    mid_l = []
    upper_l = []
    privot_num = a[random.randint(0, len(a)-1)]

    for i in a:
        if i < privot_num:
            lower_l.append(i)
        if i == privot_num:
            mid_l.append(i)
        if i > privot_num:
            upper_l.append(i)

    return quick_sort(lower_l) + mid_l + quick_sort(upper_l)

if __name__ == '__main__':
    a = [1,3,5,7,9,2,6,8,4]
    print(quick_sort(a))
