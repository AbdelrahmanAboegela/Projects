ABDELRAHMAN ASHRAF 320220168 SEC9 

num = input("Enter a list of numbers separated by commas: ").split(",")
pos = 0
neg = 0

for i in num:
    if int(i) >= 0:
        pos += 1
    else:
        neg += 1

print("pos =", pos, ", neg =", neg)

-------------------------------------------------------------------
num = input("Enter a list of numbers separated by commas: ").split(",")
even = 0
odd = 0

for i in num:
    if int(i) % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even =", even, ", odd =", odd)

--------------------------------------------------------------------
lst = input("Enter a list of numbers separated by commas: ").split(",")
duplicates = []

for i in lst:
    if lst.count(i) > 1 and i not in duplicates:
        duplicates.append(i)

print("output_list =", duplicates)

----------------------------------------------------------------------

lst = []
n = int(input("Enter the number of sublists: "))
for i in range(n):
    sub_lst = input(f"Enter the space-separated elements of sublist {i+1}: ").split()
    lst.append([int(e) for e in sub_lst])

rev_sorted_lst = [sorted(sub_lst, reverse=True) for sub_lst in lst][::-1]

print("The original list is :", lst)
print("The reverse sorted Matrix is :", rev_sorted_lst)

------------------------------------------------------------------------

lst = []
n = int(input("Enter the number of tuples in the list: "))
for i in range(n):
    tpl = tuple(map(int, input(f"Enter the space-separated elements of tuple {i+1}: ").split()))
    lst.append(tpl)

val = int(input("Enter the value to replace the last element of each tuple: "))

new_lst = [tpl[:-1] + (val,) for tpl in lst]

print("The original list is :", lst)
print("The modified list is :", new_lst)

-------------------------------------------------------------------------

lst = []
n = int(input("Enter the number of tuples in the list: "))
for i in range(n):
    tpl = tuple(input(f"Enter the elements of tuple {i+1} separated by comma: ").split(','))
    lst.append(tpl)

sorted_lst = sorted(lst, key=lambda x: float(x[1]), reverse=True)

print("The original list is :", lst)
print("The sorted list is :", sorted_lst)

-------------------------------------------------------------------------
print(input("Enter a string: ").replace("#"," ").replace("$"," ").replace(","," ").split())

-------------------------------------------------------------------------

def our_replace(main_str, pattern, replace_with):
    return replace_with.join(main_str.split(pattern))

main_str, pattern, replace_with = input("Enter main string, pattern, and replace string separated by space: ").split()

result = our_replace(main_str, pattern, replace_with)

print(result)


