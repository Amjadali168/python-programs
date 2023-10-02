# pass by reference
# def func(list):
#     list[0] = 1
#     list[2] = 5
#     return

# list = [4,6,8,9]
# (func(list))
# print(list)

# # unpacking of element from multiple argument
# def func(x, y, z, a):
#     print(x)
#     print(y)
#     print(z)
#     print(a)
    
#     return

# list = [4,6,8,9]
# (func(*list))

def func(*params):
    for i in params:
        print(i)
    return


list = [9, 8, 3, 2]
func(*list)