import random


def bubble_sort(items):
    for i in xrange(len(items)):
        for j in xrange(len(items)-1-i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]


def insertion_sort(items):
    for k in xrange(1, len(items)):
        j = k
        while j > 0 and items[j] < items[j-1]:
            items[j], items[j-1] = items[j-1], items[j]
            j -= 1


def merge_sort(items):
    if len(items) <= 1:
        return

    n = len(items) / 2
    left = items[:n]
    right = items[n:]
    merge_sort(left)
    merge_sort(right)
    merge(items, left, right)


def merge(items, left, right):
    i = 0
    j = 0
    for k in xrange(len(items)):
        if i >= len(left):
            items[k] = right[j]
            j += 1
        elif j >= len(right):
            items[k] = left[i]
            i += 1
        elif left[i] < right[j]:
            items[k] = left[i]
            i += 1
        else:
            items[k] = right[j]
            j += 1


def quicksort(items):
    if len(items) <= 1:
        return

    pivot_idx = len(items) / 2
    left = []
    right = []

    for idx, item in enumerate(items):
        if idx == pivot_idx:
            continue
        elif item <= items[pivot_idx]:
            left.append(item)
        else:
            right.append(item)

    quicksort(left)
    quicksort(right)
    items[:] = left + [items[pivot_idx]] + right


random_items = [random.randint(-50, 100) for c in range(32)]
sorted_items = sorted(random_items)

print 'Before: ', random_items
quicksort(random_items)
print 'After : ', random_items

print sorted_items == random_items
