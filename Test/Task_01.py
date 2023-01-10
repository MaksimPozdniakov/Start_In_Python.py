from c_task_01 import create_equation
from Coding import decode

if __name__ == '__main__':
    equation = create_equation()
    print(equation)
    new_equation = decode(equation)
    print(new_equation)
