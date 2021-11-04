def divisor(num):
    assert num >= 0, "debes ingresar un número positivo"
    divisor = [i for i in range(1, num +1) if num % i == 0]
    return divisor


def run():
    num = input('Ingresa un número: ')
    assert num.isnumeric() and int(num) > 0, "Debes ingresar un número"
    print(divisor(int(num)))
    print("Terminó mi programa")
        

if __name__ == '__main__':
    run()