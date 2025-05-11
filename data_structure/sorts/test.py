# coding=utf-8
"""
统一测试
"""
from utils import generate_array
from bubblesort import bubblesort
from selectsort import selectsort
from quicksort import quicksort
from mergesort import mergesort


def test_sort(sortfunc):
    print(f'=========== start: {sortfunc.__name__} ===========')
    for n in [10, 33, 66]:
        arr = generate_array(n)
        correct_arr = sorted(arr)

        sorted_arr = sortfunc(arr)

        status = '√' if correct_arr == sorted_arr else '×'

        print(f'[{status}] {arr} => {sorted_arr}')


if __name__ == "__main__":
    test_sort(bubblesort)
    test_sort(selectsort)
    test_sort(quicksort)
    test_sort(mergesort)
