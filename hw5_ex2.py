import re
from typing import Callable


def generator_numbers(text: str):# знаходимо всі дійсні числа у тексті за допомогою регулярного виразу
    numbers = re.findall(r'(?<=\s)\d+\.\d+(?=\s)', text)  #знаходимо всі числа у форматі "цифри.цифри"
    for number in numbers:
        yield float(number)  #повертаємо кожне число у вигляді дійсного числа


def sum_profit(text: str, func: Callable):  #cтворюємо генератор і підсумовуємо всі числа і використовуємр переданий генератор
    return sum(func(text))


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 ів 324.00 доларів."
total_income = sum_profit(text, generator_numbers) #обчислюєм загальний дохід (ф-ція sum_profit і генератор generator_numbers)
print(f"Загальний дохід: {total_income}")