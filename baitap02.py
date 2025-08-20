# 1. Write a Python program to calculate the length of a string.
import string
from itertools import count

chuoi=input("nhập một chuỗi:")
x= len(chuoi)
print("độ dài chuỗi=",x)


# 2. Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
from collections import Counter

y= "google.com"
freq = Counter(y)
print(dict(freq))


# 3. Write a Python program to get a string made of the first 2 and last 2 characters of a given
# string. If the string length is less than 2, return the empty string instead.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String
a= input("nhập một chuỗi:")
if len(a) < 2:
    result = ""
else:
    result = a[:2] + a[-2:]
print("kết quả:",result)


# 4. Write a Python program to get a string from a given string where all occurrences of its first
# char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'
d= "restart"
result= d[0] + d[1:].replace(d[0], "$")
print(result)

# 5. Write a Python program to get a single string from two given strings, separated by a space and
# swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz
e= "abc"
f= "xyz"
new_e= f[:2] + e[2:]
new_f= e[:2] + f[2:]
result= new_e + " " + new_f
print(result)


# 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If
# the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is
# less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'
h= "abc"
if len(h) < 3:
    result= h
elif h.endswith("ing"):
    result= h + "ly"
else:
    result= h + "ing"
print(result)


# 7. Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given
# string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the
# resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'
b= input("nhập một chuỗi:")
position_not= b.find("not")
position_poor= b.find("poor")
if position_not != -1 and position_poor != -1 and position_not < position_poor:
    b = b[:position_not] + "good" + b[position_poor + 4:]
print("kết quả:",b)


# 8. Write a Python function that takes a list of words and return the longest word and the length
# of the longest one.
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9
words= ["sad","exercises","love","happy","bore"]
longest_word= max(words, key=len)
length= len(longest_word)
print("từ dài nhất:",longest_word)
print("độ dài từ dài nhất:",length)


# 9. Write a Python program to remove the nth index character from a nonempty string
j= "Python"
n= 2
result= j[:n] + j[n + 1:]
print("chuỗi chính thức:",j)
print("chuỗi sau khi xoá ký tự thứ 2:",result)



# 10. Write a Python program to change a given string to a newly string where the first and last
# chars have been exchanged.
c= input("nhập một chuỗi:")
if len(c) <= 1:
    result= c
else:
    result= c[-1] + c[1:-1] + c[0]
print("kết quả:",result)



# 11. Write a Python program to remove characters that have odd index values in a given string.
l= input("nhập một chuỗi:")
result= l[::2]
print("kết quả từ ở vị trí số lẻ bị xoá:",result)


# 12. Write a Python program to count the occurrences of each word in a given sentence.
from collections import Counter

k= input("nhập một chuỗi:")
words = k.lower().split()
counts = Counter(words)
print(counts)


# 13. Write a Python script that takes input from the user and displays that input back in upper
# and lower cases.
m= input("nhập một chuỗi:")
print("chữ in hoa:",m.upper())
print("chữ viết thường:",m.lower())


# 14. Write a Python program that accepts a comma-separated sequence of words as input and
# prints the distinct words in sorted form (alphanumerically).
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white,red
n= input("nhập chuỗi từ(cách nhau dấu phẩy):")
words = [w.strip() for w in n.split(",")]
distinct_words = sorted(set(words))
print(",".join(distinct_words))



# 15. Write a Python function to create an HTML string with tags around the word(s).
# Sample function and result :
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
tag= input("nhập tag:")
text= input("nhập text:")
result= f"<{tag}>{text}</{tag}>"
print("kết quả:",result)



# 16. Write a Python function to insert a string in the middle of a string.
# Sample function and result :
# insert_sting_middle('[[]]<<>>', ' Python') -> [[Python]]
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
frame= input("nhập khung:")
word= input("nhập từ trong khung:")
mid = len(frame) // 2
result = frame[:mid] + word + frame[mid:]
print("kết quả:",result)



# 17. Write a Python function to get a string made of 4 copies of the last two characters of a
# specified string (length must be at least 2).
# Sample function and result :
# insert_end('Python') -> onononon
# insert_end('Exercises') -> eseseses
r= input("nhập một chuỗi(ít nhất 2 ký tự):")
result= r[-2:] * 4
print("kết quả:",result)


# 18. Write a Python function to get a string made of the first three characters of a specified string.
# If the length of the string is less than 3, return the original string.
# Sample function and result :
# first_three('ipy') -> ipy
# first_three(' python') -> pyt
t= input("nhập một chuỗi:")
if len(t) <= 3:
  result= t
else:
  result= t[:3]
print("kết quả:",result)



# 19. Write a Python program to get the last part of a string before a specified character.
# https://www.w3resource.com/python-exercises
# https://www.w3resource.com/python
w= input("nhập một chuỗi:")
sep= input("nhập ký tự muốn tách ra khỏi vế sau:")
print("kết quả:",w.rsplit(sep, 1)[0])



# 20. Write a Python function to reverse a string if its length is a multiple of 4.
u= input("nhập một chuỗi:")
if len(u) % 4 == 0:
    result= u[::-1]
print("kết quả:",result)



# 21. Write a Python function to convert a given string to all uppercase if it contains at least 2
# uppercase characters in the first 4 characters.
A= input("nhập một chuỗi:")
upper_count = sum(1 for c in A[:4] if c.isupper())
result = A.upper() if upper_count >= 2 else A
print("kết quả:",result)


# 22.Write a Python program to sort a string lexicographically.
B= input("nhập một chuỗi:")
result= "".join(sorted(B))
print("kết quả:",result)


# 23. Write a Python program to remove a newline in Python.
C= "Hello\nWorld\nPython\nProgram"
result= C.replace("\n", "")
print("kết quả:",result)


# 24. Write a Python program to check whether a string starts with specified characters.
D= input("nhập một chuỗi:")
prefix= input("nhập ký tự / chuỗi cần kiểm tra ở đầu:")
if D.startswith(prefix):
    print("chuỗi bắt đầu bằng:",prefix)
else:
    print("chuỗi không bắt đầu bằng:",prefix)



# 25. Write a Python program to create a Caesar encryption.
# Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's
# code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a
# type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed
# number of positions down the alphabet. For example, with a left shift of 3, D would be replaced
# by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his
# private correspondence.
E= input("nhập một chuỗi:")
shift= int(input("nhập số muốn dịch:"))
alphabet= string.ascii_lowercase
result= ""
for char in E:
    if char.lower() in alphabet:
        index= (alphabet.index(char.lower()) + shift) % 22
        result+= alphabet[index].upper() if char.isupper() else alphabet[index]
    else:
        result+= char
print("kết quả:",result)


# 26. Write a Python program to display formatted text (width=50) as output.
import textwrap

Text= """Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.Python is dynamically type-checked and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming."""
print(textwrap.fill(Text, width=50))


# 27. Write a Python program to remove existing indentation from all of the lines in a given text.
import textwrap

Text= """
           Python is a popular programming language. It was 
           created by Guido van Rossum,and released in 1991
      """
print(textwrap.dedent(Text))


# 28. Write a Python program to add prefix text to all of the lines in a string.
import textwrap

Text= """Python 
is a popular
programming language"""
print(textwrap.indent(Text, ">> "))


# 29. Write a Python program to set the indentation of the first line.
text= """Python is a popular programming language"""
print("   " + text.replace("\n", "\n"))



# 30. Write a Python program to print the following numbers up to 2 decimal places.
print(format(3.1415926,".2f"))



# 31. Write a Python program to print the following numbers up to 2 decimal places with a sign.
print(format(-3.1415926,"+.2f"))


# 32. Write a Python program to print the following positive and negative numbers with no
# decimal places.
print(format(3.1415926,".0f"), format(-3.1415926,".0f"))


# 33. Write a Python program to print the following integers with zeros to the left of the specified
# width.
print(format(2,"05d"), format(22,"05d"))


# 34. Write a Python program to print the following integers with '*' to the right of the specified
# width.
print("{:*<5}".format(2), "{:*<5}".format(222))


# 35. Write a Python program to display a number with a comma separator.
num= 12345678910
print("{:,}".format(num))

# 36. Write a Python program to format a number with a percentage.
num= 0.22
print("{:.2%}".format(num))


# 37. Write a Python program to display a number in left, right, and center aligned with a width of
# 10.
num = 2210
print("{:<10}".format(num))
print("{:>10}".format(num))
print("{:^10}".format(num))


# 38. Write a Python program to count occurrences of a substring in a string.
text= "Python is hard, and Python is interesting"
substring= "Python"
count = text.count(substring)
print(f"số lần xuất hiện của '{substring}':", count)


# 39. Write a Python program to reverse a string.
P= input("nhập một chuỗi:")
print(P[::-1])


# 40. Write a Python program to reverse words in a string.
S= input("nhập một chuỗi:")
result= " ".join(reversed(S.split()))
print("kết quả:",result)


# 41. Write a Python program to strip a set of characters from a string.
F= "Hello World"
chars= "ueoaiUEOAI"
result= ""
for ch in F:
    if ch not in chars:
        result+= ch
print("kết quả:",result)



# 42. Write a Python program to count repeated characters in a string.
# Sample string: 'thequickbrownfoxjumpsoverthelazydog'
# Expected output :
# o 4
# e 3
# u 2
# h 2
# r 2
# t 2
G= "thequickbrownforjumpsoverthelazydog"
count= {}
for ch in G:
    counts[ch]= counts.get(ch,0) + 1
for ch, count in counts.items():
    if count > 1:
     print(ch, count)


# 43. Write a Python program to print the square and cube symbols in the area of a rectangle and
# the volume of a cylinder.
# Sample output:
# The area of the rectangle is 1256.66cm2
# The volume of the cylinder is 1254.725cm3
import math
lengthR= 55.802
widthR= 22.52
areaR= lengthR * widthR

radiusC= 5
heightC= 15.976
pi= 3.1415926
volumeC= math.pi * radiusC**2 * heightC
print(f"the area of the rectangle is {areaR:.2f}cm\u00b2")
print(f"the volume of the cylinder is {volumeC:.3f}cm\u00b3")


# 44. Write a Python program to print the index of a character in a string.
# Sample string: w3resource
# Expected output:
# Current character w position at 0
# Current character 3 position at 1
# Current character r position at 2
# - - - - - - - - - - - - - - - - - - - - - - - - -
# Current character c position at 8
# Current character e position at 9
S= "w3resource"
for index in range(len(S)):
     print(f"Current character {S[index]} position at {index}")


# 45. Write a Python program to check whether a string contains all letters of the alphabet.
P= "the quick brown fox jumps over the lazy dog".lower()
alphabet= "abcdefghijklmnopqrstuvwxyz"
if all(ch in P for ch in alphabet):
    print("the string contains all letters of the alphabet")
else:
    print("the string doesn't contain all letters of the alphabet")



# 46. Write a Python program to convert a given string into a list of words.
# Sample Output:
# ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']
# ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']
Q= "the quick brown fox jumps over the lazy dog"
words= Q.split()
print(words)


# 47. Write a Python program to lowercase the first n characters in a string.
H= "PYTHONPROGRAM"
n= 6
result= H[:n].lower() + H[n:]
print("n ký tự đầu tiên về chữ thường:",result)



# 48. Write a Python program to swap commas and dots in a string.
# Sample string: "32.054,23"
# Expected Output: "32,054.23"
K= "32.054,23"
table= str.maketrans(".,", ",.")
result= K.translate(table)
print("kết quả:",result)



# 49. Write a Python program to count and display vowels in text.
U= "the quick brown fox jumps over the lazy dog"
vowels= "euoaiEUOAI"
find= [ch for ch in U.lower() if ch in vowels]
print("vowels:", " ".join(find))
print("total vowels:", len(find))


# 50. Write a Python program to split a string on the last occurrence of the delimiter.
T= "python-programing-exercises"
delimiter= "-"
seperate= T.rsplit(delimiter, 1)
print("kết quả:",seperate)