def divisors(num):
    # while num < 0:
    #     assert num.isnumeric(), "Debes ingresar un número"
    divisors = []
    for i in range (1, num + 1):
        if num % i == 0:
            divisors. append(i)
    return divisors
def run():
    num = input ("Ingresa un número: ")
    assert num.isnumeric(), "Debes ingresar un número"
    print (divisors(int(num)))
    print("Terminó mi programa")


if __name__ == '__main__':
    run()