# num = int("42") # 42
# name = str(123) # "123"
# data = list("abc") # ['a', 'b', 'c']
# data = dict(a=1, b=2) # {'a': 1, 'b': 2}
# print(type(num)) # <class 'int'>

# abs(-9) # 9
# max([1, 3, 7]) # 7
# min([1, 3, 7]) # 1
# round(3.14159,2) # 3.14
# sum(divmod([1, 2, 3])) # 6

for i, v in enumerate(["a", "b"]):
    print(i, v)  # 0 a , 1 b

len([10, 20, 30])  # 3

list(map(str, [1, 2, 3]))  # ['1', '2', '3']

sorted([3, 1, 2])  # [1, 2, 3]

list(zip([1, 2], ["a", "b"]))  # [(1,'a'), (2,'b')]
