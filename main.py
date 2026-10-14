"""S = input("enter an string:")
rev = ""

for i in range(len(S) -1,-1,-1):
    rev = rev + S[irev]

print(rev)"""

"""numbers = [1,2,3,4,5,7,7,9,70]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(largest)"""

"""numbers = [1,2,3,4,5,7,7,9,70]
target = 75

for i in range(len(numbers)):
    for j in range(i, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(f"{numbers[i]} + {numbers[j]} = {target}")"""

"""def large(numbers, largest):
    largest = numbers[0]

    for i in numbers:
        if i > largest:
            largest = i

    return largest

numbers = [10,20,30,40,50]
largest = numbers[0]
print (large(numbers, largest))"""

"""def countdown(n):
    if n == 0:
        print("done")
        return

    print(n)
    countdown(n - 1)

countdown(4)"""

"""def fib(n):
    if (n <=1):
        return n 
    return fib(n-1) + fib(n-2)

print(fib(10))"""

"""def rev(arr):
    left = 0
    right = len(arr) -1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left +=1
        right -=1

    return arr

arr = [10,20, 30, 40, 500,70]
print(rev(arr))"""

"""def sum(numbers, target):
    left = 0
    right = len(numbers) -1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return[left, right]
        elif current_sum > target:
            right -= 1
        else:
            left +=1
    return[]"""

"""def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(window_sum, max_sum)
    return max_sum

arr = [1, 2, 3, 45, 6, 7, 9]
k = 3
print(max_sum_subarray(arr, k))"""

"""def search(numbers, target):
    for i in range(len(numbers)):
        if (numbers[i] == target):
            return i
    

numbers = [10,20,30,50,70]
target = 50
print(search(numbers, target))"""

"""def binary_search(numbers, target):
    left = 0
    right = len(numbers) -1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid -1

    return -1"""

"""numbers = [10,20,30,50,70]
n = len(numbers)

for i in range(n):
    for j in range(0, n-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
print(numbers)"""

"""numbers = [10,20,30,50,70]
n = len(numbers)

for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if numbers[j] > numbers[min_index]:
            min_index = j
        numbers[j], numbers[min_index] = numbers[min_index], numbers[j]
print(numbers)"""

