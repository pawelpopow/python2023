array = [32, 65, 20]

array[0] = 80
array[1] = 76

new = array.copy()

new.sort()

if __name__ == '__main__':
    print(new)
    print(array)
    print(f'Nie pozortowana tablica {array} oraz pozortowana tablica {new}')
