def do_a_bunch_of_stuff(items):
    last_idx = len(items) - 1
    print(items[last_idx])        # O(1)

    middle_idx = len(items) / 2   # O(1)
    idx = 0

# when in a loop, multiply the loop by what's below:
    while idx < middle_idx:  # O(n/2)
        print(items[idx])    # O(1)
        idx = idx + 1        # O(1)

    for num in range(2000):
        print(num)           # O(2000)


# sum all the numbers

# O(1) + O(1) + O(n/2) + O(2000)  = O(n) 
# disregard every thing else
# Use only the bigger power of n
# pay attention to the worst case



# Recursive complexity

total_times_count = 0

def count_down(n):
    global total_times_count 
    total_times_count  += 1

    if n == 0:
        return

    count_down(n - 1) # O(n) linear time
    count_down(n - 1) # O(c^n)



# O(log n)
def half(n):
    if n <= 1:
        return

    half(n / 2)







count_down(5)
print(total_times_count) # 63


