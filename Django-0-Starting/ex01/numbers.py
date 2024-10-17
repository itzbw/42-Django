def numbers():
    file = open('numbers.txt', 'r')
    numbers = file.read().replace(',','\n')
    print(numbers)

if __name__ == '__main__':
    numbers()