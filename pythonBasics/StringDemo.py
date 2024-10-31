str = "HelloNereHaifofjo73FGGiwfnfvkdv.com"
str1 = "Consulting firm"
str3 = "Hello"

print(str[1])  # e

print(str[1:5])  # ello   if you want substring in python

print(str + str1)  # concatenation

print(str3 in str)  # True   substring check

var = str.split(".")  # ['HelloNereHaifofjo73FGGiwfnfvkdv', 'com']

print(var)
print(var[0])  # HelloNereHaifofjo73FGGiwfnfvkdv

str4 = "    grear "
print(str4.strip())  # grear
print(str4.lstrip())  # grear    удаляет пробелы
print(str4.rstrip())  #
