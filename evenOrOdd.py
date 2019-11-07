def TryExcept():
    try:
        number = int(input('type a number: '))
        if number%2 == 0:
            print(f' {number} is an even number ')
        else:
            print(f'{number} is a odd number')
    except:
        print('please type a integer number')
        TryExcept()

TryExcept()