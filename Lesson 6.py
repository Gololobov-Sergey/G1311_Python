
# print("Open file")
# try:
#     a = int(input("Enter number: "))
#     b = int(input("Enter number: "))
#     if b == 0:
#         raise ValueError("Invalid argument. b = 0!")
#     print(a/b)
#     print("Save to file")
# except Exception as ex:
#     print(ex)
# finally:
#     print("File close")

#
# def checker(st):
#     if type(st) != str:
#         raise TypeError(f"{st} not string!")
#     return st
#
# a = "mama"
# checker(a)


# result = []
# def divider(a, b):
#     if a < b:
#         raise ValueError
#     if b > 100:
#         raise IndexError
#     return a/b
#
# data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8 : 4}
# for key in data:
#     res = divider(key, data[kem])
#     result.append(res)
#
# print(result)


names = {"Alex": "10-12", "Oleg": "13-15", "Mark": "10-12"}
print(names["Marks"])