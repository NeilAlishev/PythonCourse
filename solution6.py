def my_function(n, k):
    if n > 20:
        return 0

    s = 0
    for i in range(1, n):
        if i % 2 == 0:
            s += i ** k

    return s

# функция, в которой мы тестируем my_function
def main():
    print(my_function(21, 5)) # => 0
    print(my_function(7, 2)) # => 56
    print(my_function(20, 15)) # => 8071572893847552000


main()