# 1. split half
# 2.

count = 0


def swap(nums):
    if len(nums) <= 2:
        is_greate(nums[0], nums[1])


def inversion_count_sort(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                count += 1
    return nums, count


def split_half(nums):
    global count
    if len(nums) > 2:
        return split_half(nums[: len(nums) // 2]), split_half(nums[len(nums) // 2:])
    elif len(nums) == 2:
        a, count_a = inversion_count_sort(nums[0])
        b, count_b = inversion_count_sort(nums[1])
        total = count_a + count_b
    else:
        return nums


def is_greate(first, second):
    return first > second


def merged_arr_count(left_arr, right_arr):
    new_arr = []
    count = 0
    i = 0
    j = 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            new_arr.append(left_arr[i])
            i += 1
        else:
            new_arr.append(right_arr[j])
            j += 1
            count += len(left_arr) - i

    while i < len(left_arr):
        new_arr.append(left_arr[i])
        i += 1
        # count += 1

    while j < len(right_arr):
        new_arr.append(right_arr[j])
        j += 1
    return new_arr.copy(), count


def inversion_count(arr):
    if len(arr) == 1:
        return arr, 0
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            return [arr[1], arr[0]], 1
        return arr, 0
    elif len(arr) > 2:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        left_arr, count_left = inversion_count(left)
        right_arr, count_right = inversion_count(right)

        total_count = count_left + count_right
        merged_arr, merge_count = merged_arr_count(left_arr, right_arr)
        return merged_arr, total_count + merge_count
    return arr, 0


def merged_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # Recursive call on each half
        merged_sort(left)
        merged_sort(right)

        # two iterators for traversing the halves
        i = 0
        j = 0

        # Iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # For all the remanining values
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def bubble_sort(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                count += 1
    print(f"Total swap: {count}")


if __name__ == '__main__':
    new_arr1 = [54044, 14108, 79294, 29649, 25260, 60660, 2995, 53777]
    ans = 2407905288
    with open('IntegerArray.txt', 'r') as f:
        num_array = [int(num) for num in f.read().strip().split('\n')]

        # merged_sort(num_array)
        # bubble_sort(num_array)
        arr, count = inversion_count(num_array)
        print(f'Total swap: {count}')
        print(arr)

        # arr, count = inversion_count([7,20,1,2,6,3])
        # print(arr)

        # print(split_half(num_array))
        # print(f'Count: {count}')

        # total = len(num_array)
        #
        # first_half = num_array[:total//2]
        # second_half = num_array[total//2:]
        #
        # a = swap(first_half)
        # b = swap(second_half)
