import random

def create_degree(degree):
    dict_degrees = {0: '⁰', 1: '¹', 2: '²', 3: '³', 4: '⁴', 5: '⁵', 6: '⁶', 7: '⁷', 8: '⁸', 9: '⁹'}
    result = ''
    while degree > 0:
        result = dict_degrees[degree % 10] + result
        degree = degree // 10
    if degree == 0:
        degree = dict_degrees[0]
    return result

result = create_degree(0)
print(result)

# def create_equation(degree) -> str:
#     equation_dict = {}
#     for i in range(0, degree + 1):
#         equation_dict[i] = 'x' + create_degree(i)
#     print(equation_dict)
#     new_equation = []
#     for i in equation_dict.values():
#         digit = random.randint(-100, 100)
#         new_equation.append(f'{digit} * {i}')
#     new_equation.reverse()
#     new_equation = ' + '.join(new_equation) + ' = 0'
#
#     return new_equation
# my_degree = int(input('Введите максимальную степень: '))
# my_dict = create_equation(my_degree)
# my_dict = my_dict.replace(' *', '*').replace('* ', '*').replace('*', '').replace('+ -', '- ')\
#     .replace('x¹', 'x')
# print(my_dict)



# def new() -> str:
#     my_dict = {10: 87, 9: -80, 8: 84, 7: 78, 6: 13, 5: 98, 4: 57, 3: -40, 2: -41, 1: -72, 0: 70}
#
#     my_list = []
#
#     for key, value in my_dict.items():
#         my_list.append(f'{value}*x**{key}')
#     my_list = ' + '.join(my_list) + ' = 0'
#     return my_list
#
# my_list = new()
# print(my_list)



