#Get your basics right - Implement selection sort algorithm in python. The function accepts a
#list in the input and returns a sorted list.
#E.g.
#Input f1([5,416,54,21,6135,15,741]) should
#Return [5, 15, 21, 54, 416, 741, 6135]

def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

# Test the function
input_list = [5, 416, 54, 21, 6135, 15, 741]
sorted_list = selection_sort(input_list)
print(sorted_list)
