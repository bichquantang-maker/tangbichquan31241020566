import random
from operator import itemgetter
list= []
for item in range(10):
    list.append(random.randint(1,20))

def print_list():
    for item in list:
        print(item, end=',')
# 1. Write a Python program to sum all the items in a list.
def ex_01():
    sum= 0
    for ỉtem in list:
        sum += item
    print("\ntổng các số trong list:",sum)

# 2. Write a Python program to multiply all the items in a list.
def ex_02():
    product= 1
    for item in list:
        product *= item
    print("tích các số trong list:",product)

# 3. Write a Python program to get the largest number from a list.
def ex_03():
    largest= list[0]
    for item in list:
        if item > largest:
            largest = item
    print("số lớn nhất trong list:",largest)

# 4. Write a Python program to get the smallest number from a list.
def ex_04():
    smallest = list[0]
    for item in list:
        if item < smallest:
            smallest = item
    print("số nhỏ nhất trong list:",smallest)

# 5. Write a Python program to count the number of strings from a given list of
# strings. The string length is 2 or more and the first and last characters are the
# same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
def ex_05():
    chuoi= input("nhập một chuỗi:").split()
    count = 0
    for item in chuoi:
        if len(item) >= 2 and item[0] == item[-1]:
            count += 1
    print("kết quả:",count)

# 6. Write a Python program to get a list, sorted in increasing order by the last
# element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
def ex_06():
    chuoi1= [(2,5), (1,2), (4,4), (2,3), (2,1)]
    chuoi1.sort(key=lambda x:x[-1])
    print("kết quả:",chuoi1)

# 7. Write a Python program to remove duplicates from a list.
def ex_07():
    num= [2,2,1,0,2,0,0,6]
    unique= []
    [unique.append(x) for x in num if x not in unique]
    print("kết quả:",unique)

# 8. Write a Python program to check if a list is empty or not.
def ex_08():
    my_list = []
    print("list rỗng" if not my_list else "list không rỗng")

# 9. Write a Python program to clone or copy a list.
def ex_09():
    num= [2,2,1,0,2,0,0,6]
    copy_num= num.copy()
    print("original:",num)
    print("copied:",copy_num)

# 10. Write a Python program to find the list of words that are longer than n from a
# given list of words.
def ex_10():
    words= ["happy","interesting","love","sad","redamancy","hi"]
    n = 3
    result= [word for word in words if len(word) > n]
    print("các từ dài hơn n:",result)

# 11. Write a Python function that takes two lists and returns True if they have at
# least one common member.
def ex_11():
    lst1= [2,1,0,6]
    lst2= [3,1,2,7]
    print(bool(set(lst1) & set(lst2)))

# 12. Write a Python program to print a specified list after removing the 0th, 4th
# and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']
def ex_12():
    colors= ['red','green','white','black','pink','yellow']
    del colors[5]
    del colors[4]
    del colors[0]
    print("kết quả:",colors)

# 13. Write a Python program to generate a 3*4*6 3D array each element is *.
def ex_13():
    array= [[['*' for _ in range(6)] for _ in range(4)] for _ in range(3)]
    for i in array:
        for j in i:
            print(j)
        print()

# 14. Write a Python program to print the numbers of a specified list after removing
# even numbers from it.
def ex_14():
    numbers= [1,2,3,4,5,6,7,8,9,10]
    result= [num for num in numbers if num % 2 != 0]
    print("sau khi bỏ số chẵn:",result)

# 15. Write a Python program to shuffle and print a specified list.
def ex_15():
    numbers= [1,2,3,4,5,6,7,8]
    random.shuffle(numbers)
    print("sau khi xáo trộn:",numbers)

# 16. Write a Python program to generate and print a list of the first and last 5
# elements where the values are square numbers between 1 and 30 (both
# included).
def ex_16():
    squares= [i ** 2 for i in range(1, 31)]
    result= squares[:5] + squares[-5:]
    print("5 số đầu và 5 số cuối là:",result)

# 17. Write a Python program to check if each number is prime in a given list of
# numbers. Return True if all numbers are prime otherwise False.
# Sample Data:
# ([0, 3, 4, 7, 9]) -> False
# ([3, 5, 7, 13]) -> True
# ([1, 5, 3]) -> False
def ex_17():
    numbers= [3,5,7,13]
    result= all(
        num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))
        for num in numbers)
    print(result)

# 18. Write a Python program to generate all permutations of a list in Python.
def ex_18():
    import itertools
    lst5= [1,2,3]
    for p in itertools.permutations(lst5):
        print(p)

# 19. Write a Python program to calculate the difference between the two lists.
def ex_19():
    lst6= [1,2,3,4]
    lst7= [3,4,5,6]
    diff1= []
    for x in lst6:
        if x not in lst7:
            diff1.append(x)
    diff2= []
    for x in lst7:
        if x not in lst6:
            diff2.append(x)
    print("lst6 - lst7:",diff1)
    print("lst7 - lst6:",diff2)

# 20. Write a Python program to access the index of a list.
def ex_20():
    lst8= ['Tang','Bich','Quan','AS']
    for i in range(len(lst8)):
        print("index:",i, "value:",lst8[i])

# 21. Write a Python program to convert a list of characters into a string.
def ex_21():
   chars= ['P','y','t','h','o','n']
   string= ""
   for ch in chars:
       string += ch
   print("kết quả:",string)

# 22. Write a Python program to find the index of an item in a specified list.
def ex_22():
    colors= ['red','green','white','black','pink']
    print(colors.index('black'))
    print(colors.index('pink'))

# 23. Write a Python program to flatten a shallow list
def ex_23():
    shallow_list= [[1, 2], [3, 4], [5, 6]]
    flat_list= sum(shallow_list,[])
    print(flat_list)

# 24. Write a Python program to append a list to the second list.
def ex_24():
    lst9= [1,2,3]
    lst10= ['a','b','c']
    lst10.append(lst9)
    print(lst10)

# 25. Write a Python program to select an item randomly from a list.
def ex_25():
    item= [11,22,33,44,55,66,77,88,99]
    print(random.choice(item))

# 26. Write a Python program to check whether two lists are circularly identical.
def ex_26():
    lst11= [1,2,3,1]
    lst12= [3,1,1,2]
    circle= lst12 in (lst11 * 2)
    print(circle)

# 27. Write a Python program to find the secondsmallest number in a list.
def ex_27():
    numbers= [2,3,1,6,8,7]
    second_smallest= min([x for x in numbers if x != min(numbers)])
    print("second smallest:",second_smallest)
# 28. Write a Python program to find the secondlargest number in a list.
def ex_28():
    numbers= [2,3,1,6,8,7]
    second_largest= max([x for x in numbers if x != max(numbers)])
    print("second largest:",second_largest)
# 29. Write a Python program to get unique values from a list.
def ex_29():
    numbers= [1,2,3,2,4,1,5]
    unique_values= []
    for x in numbers:
        if x not in unique_values:
            unique_values.append(x)
    print(unique_values)

# 30. Write a Python program to get the frequency of elements in a list.
def ex_30():
    from collections import Counter
    numbers= [1,1,2,2,3,4,4,4,5,5,5,5,5]
    freq= Counter(numbers)
    print(freq)

# 31. Write a Python program to count the number of elements in a list within a
# specified range.
def ex_31():
    numbers= [18,22,30,33,42,44,55,66]
    low, high= 25, 50
    count= 0
    for n in numbers:
        if low <= n <= high:
            count += 1
    print("count:",count)

# 32. Write a Python program to check whether a list contains a sublist.
def ex_32():
    main_list= [1,2,3,4,5,6]
    sub_list= [2,3,4,5]
    result= str(sub_list)[1:-1] in str(main_list)
    print(result)

# 33. Write a Python program to generate all sublists of a list.
def ex_33():
    my_list= [1, 2, 3]
    sublists= [my_list[i:j] for i in range(len(my_list)) for j in range(i + 1, len(my_list) + 1)]
    print(sublists)

# 34. Write a Python program that uses the Sieve of Eratosthenes method to
# compute prime numbers up to a specified number.
# Note: In mathematics, the sieve of Eratosthenes, (Ancient Greek: κόσκινον
# Ἐρατοσθένους, kóskinon Eratosthénous) one of a number of prime number
# sieves, is a simple, ancient algorithm for finding all prime numbers up to any
# given limit.
def ex_34():
    n= 40
    primes= [i for i in range(2, n + 1)]
    for a in primes:
        primes = [x for x in primes if x == a or x % a != 0]
    print(primes)

# 35. Write a Python program to create a list by concatenating a given list with a
# range from 1 to n.
# Sample list : ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
def ex_35():
    lst= ['p','q']
    n= 5
    result= [x + str(i) for i in range(1, n + 1) for x in lst]
    print(result)

# 36. Write a Python program to get a variable with an identification number or
# string.
def ex_36():
    x= "Python"
    y= "Hello"
    print("ID of x:",id(x))
    print("ID of y:",id(y))

# 37. Write a Python program to find common items in two lists.
def ex_37():
    lst1= [2,1,6,8]
    lst2= [6,8,7,9]
    common= []
    for i in lst1:
        if i in lst2 and i not in common:
            common.append(i)
    print(common)

# 38. Write a Python program to change the position of every n-th value to the
# (n+1)th in a list.
# Sample list: [0,1,2,3,4,5]
# Expected Output: [1, 0, 3, 2, 5, 4]
def ex_38():
    lst= [0,1,2,3,4,5]
    for i in range(0, len(lst) - 1, 2):
        lst[i], lst[i + 1] = lst[i + 1], lst[i]
    print(lst)

# 39. Write a Python program to convert a list of multiple integers into a single
# integer.
# Sample list: [11, 33, 50]
# Expected Output: 113350
def ex_39():
    lst= [22,10,2006]
    a= ""
    for i in lst:
        a += str(i)
    num= int(a)
    print(num)

# 40. Write a Python program to split a list based on the first character of a word.
def ex_40():
    words= ["strawberry","orange","peach","cherry","blueberry"]
    result= {}
    for a in words:
        result.setdefault(a[0],[]).append(a)
    print(result)

# 41. Write a Python program to create multiple lists.
def ex_41():
    lists= []
    for i in range(4):
        lists.append([])
    print(lists)

# 42. Write a Python program to find missing and additional values in two lists.
# Sample data : Missing values in second list: b,a,c
# Additional values in second list: g,h
def ex_42():
    lst1= ['a','b','c','d','e','f']
    lst2= ['d','e','f','g','h']
    missing= [i for i in lst1 if i not in lst2]
    additional= [i for i in lst2 if i not in lst1]
    print("missing values in second list:",missing)
    print("additional values in second list:",additional)

# 43. Write a Python program to split a list into different variables.
def ex_43():
    my_list= [1,2,3]
    a,b,c = my_list
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")

# 44. Write a Python program to generate groups of five consecutive numbers in a
# list.
def ex_44():
    my_list= [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
    groups= [my_list[i:i + 5] for i in range(0, len(my_list), 5)]
    print(groups)

# 45. Write a Python program to convert a pair of values into a sorted unique array.
def ex_45():
    pairs= [(3,1), (4,2), (2,3)]
    unique_sorted= sorted(set([x for pair in pairs for x in pair]))
    print(unique_sorted)

# 46. Write a Python program to select the odd items from a list.
def ex_46():
    num= [1,2,3,4,5,6,7,8,9]
    odd_numbers= [x for x in num if x % 2 != 0]
    print(odd_numbers)

# 47. Write a Python program to insert an element before each element of a list.
def ex_47():
    lst= [1,2,3]
    element_insert= 2
    new_list= []
    for x in lst:
        new_list.append(element_insert)
        new_list.append(x)
    print(new_list)

# 48. Write a Python program to print nested lists (each list on a new line) using
# the print() function.
def ex_48():
    nested_list= [[1,2,3],[4,5,6],[7,8,9]]
    print(*nested_list,sep="\n")

# 49. Write a Python program to convert a list to a list of dictionaries.
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000",
# "#800000", "#FFFF00"]
# Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name':
# 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'},
# {'color_name': 'Yellow', 'color_code': '#FFFF00'}]
def ex_49():
    color_names= ["black","red","maroon","yellow"]
    color_codes= ["#000000", "#ff0000", "#800000", "#ffff00"]
    result= [{"color_name":name, "color_code":code} for name, code in zip(color_names, color_codes)]
    print(result)

# 50. Write a Python program to sort a list of nested dictionaries
def ex_50():
    people= [
        {"name": "Quan", "age": 18},
        {"name": "Dieu", "age": 18},
        {"name": "Giau", "age": 18},
        {"name": "Nha", "age": 18}
    ]
    sorted_people= sorted(people, key=lambda x: x['age'])
    print(sorted_people)

if __name__ == '__main__':
    print_list()
    ex_01()
    ex_02()
    ex_03()
    ex_04()
    ex_05()
    ex_06()
    ex_07()
    ex_08()
    ex_09()
    ex_10()
    ex_11()
    ex_12()
    ex_13()
    ex_14()
    ex_15()
    ex_16()
    ex_17()
    ex_18()
    ex_19()
    ex_20()
    ex_21()
    ex_22()
    ex_23()
    ex_24()
    ex_25()
    ex_26()
    ex_27()
    ex_28()
    ex_29()
    ex_30()
    ex_31()
    ex_32()
    ex_33()
    ex_34()
    ex_35()
    ex_36()
    ex_37()
    ex_38()
    ex_39()
    ex_40()
    ex_41()
    ex_42()
    ex_43()
    ex_44()
    ex_45()
    ex_46()
    ex_47()
    ex_48()
    ex_49()
    ex_50()


