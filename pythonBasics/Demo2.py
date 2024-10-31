values = [1, 2, "rahul", 4, 5]
# List is data that allows multiple values and can be diffent data types

print(values[0])  # 1
print(values[3])  # 4
print(values[-1])  # 5
print(values[1:3])  # [2, 'rahul']

values.insert(3, "shetty")
print(values)  # [1, 2, 'rahul', 'shetty'
values.append("END")
print(values)  # [1, 2, 'rahul', 'shetty', 4, 5, 'END']

values[2] = "IRINA"  # Updating
print(values)  # [1, 2, 'IRINA', 'shetty', 4, 5, 'END']

del values[0]
print(values)  # [2, 'IRINA', 'shetty', 4, 5, 'END']

# Tuple - Same as LIST Data type but immutable
val = [1, 2, "word", 4.5]
print(val[1])  # 2

val[2] = "WORD"
print(val)  # [1, 2, 'WORD', 4.5]

# Dictionary
dic = {"a": 2, 4: "ABC", "c": "Hello world"}

print(dic[4]) # ABC
print(dic["c"]) # Hello world

#
dict = {}
dict["firstname"] = "Mike"
dict["lastname"] = "Bond"
dict["gender"] = "Male"

print(dict)  # {'firstname': 'Mike', 'lastname': 'Bond', 'gender': 'Male'}
print(dict["lastname"])   # Bond
