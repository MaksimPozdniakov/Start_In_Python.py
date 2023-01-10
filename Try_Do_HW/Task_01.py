import random

def create_degree(degree):
    dict_degrees = {0: '⁰', 1: '¹', 2: '²', 3: '³', 4: '⁴', 5: '⁵', 6: '⁶', 7: '⁷', 8: '⁸', 9: '⁹'}
    result = ''
    while degree > 0:
        result = dict_degrees[degree % 10] + result
        degree = degree // 10
    return result
def create_equation(degree) -> str:
    equation_dict = {}
    for i in range(degree, -1, -1):
        equation_dict[i] = 'x' + create_degree(i)

    new_equation = []
    for i in equation_dict.values():
        digit = random.randint(-100, 100)
        new_equation.append(f'{digit} * {i}')

    new_equation = ' + '.join(new_equation) + ' = 0'

    return new_equation

my_degree = int(input('Введите максимальную степень: '))

my_equation1 = create_equation(my_degree)
my_equation1 = my_equation1.replace(' *', '*').replace('* ', '*').replace('*', '').replace('+ -', '- ')\
    .replace('x ', ' ')



# my_equation2 = create_equation(my_degree)
# my_equation2 = my_equation2.replace(' *', '*').replace('* ', '*').replace('*', '').replace('+ -', '- ')\
#     .replace('x¹ ', 'x ')

print(my_equation1)
# print(my_equation2)

def new_dict(new_equation: str) -> dict:

    new_equation = new_equation.replace('x', ' x').replace('+', '').replace('-', '').split()[:-2]
    new_equation.append('x⁰')
    new_equation = str(new_equation)
    dict_equation = {}

    for i in new_equation:
        if new_equation.find('x'):
            dict_equation[i] = None

    return dict_equation

dict_equation = new_dict(my_equation1)
print(dict_equation)



