# -*- coding: utf-8 -*-
"""
Created on 2021/6/17 14:05 

@author: R.ls
"""


def bubble_sort(alist):
    """冒泡排序"""
    n = len(alist)
    for j in range(n - 1):
        for i in range(0, n - 1 - j):
            # 从头走到尾
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
    return alist


def select_sort(alist):
    """选择排序"""
    n = len(alist)
    for j in range(n - 1):
        min_index = j
        for i in range(j + 1, n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j], alist[min_index] = alist[min_index], alist[j]
    return alist


def insert_sort(alist):
    """插入排序"""
    n = len(alist)
    for j in range(1, n):
        i = j
        while i > 0:
            if alist[i] < alist[i - 1]:
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
                i -= 1
            else:
                break
    return alist


def shell_sort(alist):
    """希尔排序"""
    n = len(alist)
    gap = n // 2
    while gap > 0:
        # 插入算法 与普通的插入算法区别就是gap步长
        for j in range(gap, n):
            i = j
            while i > 0:
                if alist[i] < alist[i - 1]:
                    alist[i], alist[i - 1] = alist[i - 1], alist[i]
                    i -= 1
                else:
                    break
        # 缩短步长
        gap //= 2
    return alist


def quick_sort(alist, first, last):
    """快速排序"""
    if first >= last:
        return alist
    mid_value = alist[first]
    low = first
    high = last
    while low < high:
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
        # 从循环推出时 low==high
    alist[low] = mid_value

    # 对low左边的列表执行快速排序
    quick_sort(alist, first, low - 1)

    # 对low右边的列表执行快速排序
    quick_sort(alist, low + 1, last)

    return alist


def merge_sort(alist):
    """归并排序"""
    n = len(alist)
    if n <= 1:
        return alist
    mid = n // 2

    # left 采用归并排序后形成的有序的新的列表
    left_li = merge_sort(alist[:mid])

    # right 采用归并排序后形成的有序的新的列表
    right_li = merge_sort(alist[mid:])

    # 将两个有序的子序列合并为一个新的整体
    left_pointer, right_pointer = 0, 0
    result = []
    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] < right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1

    result += left_li[left_pointer:]
    result += right_li[right_pointer:]
    return result


def binary_search(alist, item):
    """二分查找,递归"""
    n = len(alist)
    if n > 0:
        mid = n // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search(alist[:mid], item)
        else:
            return binary_search(alist[mid + 1:], item)
    return False


def binary_search_normal(alist, item):
    """二分查找,非递归"""
    n = len(alist)
    first = 0
    last = n - 1
    while first <= last:
        mid = (first + last) // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(alist)
    # 冒泡排序 最优O(n) 最差O(n2) 稳定 相同的值不会交换位置
    #    bubble_sort = bubble_sort(alist)
    #    print(bubble_sort)

    # 选择排序 最优O(n2) 最差O(n2) 不稳定
    #    select_sort = select_sort(alist)
    #    print(select_sort)

    # 插入排序 最优O(n) 最差O(n2) 稳定
    #    insert_sort = insert_sort(alist)
    #    print(insert_sort)

    # 希尔排序 最优O(n1.3) 最差O(n2) 不稳定
    # shell_sort = shell_sort(alist)
    # print(shell_sort)

    # 重要 快速排序 最优O(nlogn) 最差O(n2) 不稳定
    quick_sort = quick_sort(alist, 0, len(alist) - 1)
    print(quick_sort)

    # 归并排序 最优O(nlogn) 最差O(nlogn) 稳定
    # merge_sort = merge_sort(alist)
    # print(merge_sort)

    # 二分查找 -- 递归
    search = binary_search(alist, 59)
    print(search)

    # search = binary_search_normal(alist, 54)
    # print(search)
