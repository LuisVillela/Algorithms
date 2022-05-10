'''
Testing algorithms
'''
from brute_force import divisors_of_n, pin_unlock, sum_of_first_n_nums
from lists import largest_num_in_list, list_merge
from recursion import countdown, factorial_of_n, nth_fibonacci_num, sum_of_first_n_recursive
from searching import binary_search, Linear_Search
from sorting import bubble_sort, bubble_sort_optimized, insertion_sort, selection_sort

#Brute Force
print('Divisors...')
n = 5
print(divisors_of_n.divisors(n))

print('Pin Unlock')
n = '1234' # Pin with 4 digits 
print(pin_unlock.unlock(n))

print('Sum of the First N Numbers...')
sum_of_first_n_nums.suma()

#Lists
print('Largest Number in the List...')
largest_number_in_list.searchlist([0,2,5,8,11,47,1,6])

print('Merge List...')
list_merge.list_2([1,4,8],[3,5,6]) # 2 Oredered lists into one ordered list

#Recursion
print('Countdown...')
n = 5 # Countdown number
print(countdown.countdown(n))

print('Factorial of an n Number...')
n = 5
print(factorial_of_n.factorial(n))

print('Nth Number ofthe Fibonacci Sequence...')
n = 6
print(nth_fibonacci_number.fibonacci(n))

print('Sum of N Recursive...')
n = 5 
print(sum_of_first_n_nums_recursive.sum_n(n))

#Searching
a = a = [] # List to search de element
for i in range (1, 101):
    a.append(i) 
n = len(a) # Parameter
d = 89 # Searched item
print('Binary Search...')
print(binary_search.order(a,n,d))

print('Linear Search...')
print(linear_Search.linearsearch(a,d))

#Sorting
a = a = [] # List to search de element
for i in range (1, 101):
    a.append(i) 
print('Bubble Sort...')
print(bubble_sort.bubble_sort(a))

print('Bubble Sort Optimized...')
print(bubble_sort_optimized.bubble_sort_optimized(a))

print('Insertion Sort...')
print(insertion_sort.insertion_sort(a))

print('Selection Sort...')
print(selection_sort.selection_sort(a))