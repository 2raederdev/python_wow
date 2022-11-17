def such_wow():
    for num in range(1,101):
        if num % 3 == 0 and num % 5 == 0:
            print('SuchWow')
        elif num % 3 == 0:
            print('Such')
        elif num % 5 == 0:
            print('Wow')
        else:
            print(num)
        

def short_such_wow():
    such_wow_arr = ['Such' * (i % 3 == 0) + 'Wow' * (i % 5 == 0) or str(i) for i in range(1,101)]
    print('\n'.join(such_wow_arr))


if __name__ == "__main__":
    short_such_wow()