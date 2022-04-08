def main():
    
    # cube = {}

    # for i in range(1, 101):
    #     if i % 3 !=0:
    #         cube[i] = i**3

    cube = {i: round(i**0.5, 4) for i in range(1,1001) if i % 3 !=0}


    print(cube) #imprimir lista

if __name__ == '__main__':
    main()