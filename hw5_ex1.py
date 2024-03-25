def caching_fibonacci():    
    cache = {} #створюємо порожній словник для кешування результатів обчислень

    def fibonacci(n): #базові випадки: 0-те число fibonacci - 0, 1-ше - 1
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:  #перевірим, чи число вже збережено у кеші
            return cache[n]
        else:
            result = fibonacci(n - 1) + fibonacci(n - 2)   #обчислення числа fibonacci та збереження його у кеші
            cache[n] = result  #зберігаємо результат у кеші
            return result

    return fibonacci

fib = caching_fibonacci() #отримуємо ф-цію fibonacci
print(fib(10))  #виведе 55
print(fib(15))  #виведе 610