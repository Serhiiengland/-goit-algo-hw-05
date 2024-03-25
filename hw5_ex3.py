import sys

def parse_log_line(line: str) -> dict:
    parts = line.split(' ', maxsplit=5) #розбиваємо рядок логу на частини за допомогою пробілу
    if len(parts) == 6:
        return {             #Якщо розбито на правильну кількість частин, створюємо словник з інф про лог
            'date': parts[0],
            'time': parts[1],
            'level': parts[2],
            'message': parts[5].strip() #останню частину вважаємо повідомленням, удаляємо зайві пробіли
        }
    else:
        print(f"Неправильний формат рядка логу: {line}") #виводимо повідомлення про помилку, якщо рядок не містить потрібної к-ті частнин
        return {}

def load_logs(file_path: str) -> list:
    try:
        with open(file_path, 'r') as file: #відкриваєм файл для логів, завантажуємо
            logs = [parse_log_line(line) for line in file]
            return logs
    except FileNotFoundError:
        print("Файл логів не знайдено.") #якщо логів не знайдено обробляємо цей вийняток
        sys.exit(1)
    except Exception as e:
        print(f"Сталася помилка під час читання файлу: {e}")
        sys.exit(1)

def filter_logs_by_level(logs: list, level: str) -> list: #фільтруєм логи за рівнеи логування
    return [log for log in logs if log.get('level') == level]

def count_logs_by_level(logs: list) -> dict: #робимо словник для підрахунку кількості логів за кожним рівнем
    counts = {'INFO': 0, 'DEBUG': 0, 'ERROR': 0, 'WARNING': 0}
    for log in logs: # перебираємо логи та збільшуємо лічильник  на 1
        if 'level' in log:
            counts[log['level']] += 1
    return counts

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість") # виводимо заголовок для логів для кожного рівня
    print("-----------------|----------")
    for level, count in counts.items(): 
        print(f"{level:<17}| {count:<10}") # к-ть логів у сповчик

def display_logs(logs: list):
    for log in logs: # виводим всі логи
        print(log['date'], log['time'], log['level'], log['message'])

if __name__ == "__main__":   # перевіримо чи передано достатньо аргументів командного рядку
    if len(sys.argv) < 2:
        print("Використання: python main.py /шлях/до/файлу/логів [рівень_логування]")
        sys.exit(1)

    log_file = sys.argv[1] # отримуємо шлях до файлу логу з першого аргументу командного рядка
    logs = load_logs(log_file) #завантажуємо логи

    if len(sys.argv) == 2: #якщо передано 2 аргументи ком.рядка, фільтруємо логи відповідно
        counts = count_logs_by_level(logs)
        display_log_counts(counts)
    elif len(sys.argv) == 3: #якщо 3, відповідно
        level_to_filter = sys.argv[2].upper()
        filtered_logs = filter_logs_by_level(logs, level_to_filter)
        counts = count_logs_by_level(filtered_logs)
        display_log_counts(counts)
        if filtered_logs:
            print("\nДеталі логів для рівня '{}':".format(level_to_filter))
            display_logs(filtered_logs)
    else:
        print("Невірний формат команди.") #виводимо повідомлення, якщо невірний формат команди(інша к-ть аргументів)
        
        
      
#python C:\Users\liljo\OneDrive\Documents\My_repos\First_repo\Homework\goit-hw-05\hw5_ex3.py C:\Users\liljo\OneDrive\Documents\My_repos\First_repo\Homework\goit-hw-05\log_file.log
#python C:\Users\liljo\OneDrive\Documents\My_repos\First_repo\Homework\goit-hw-05\hw5_ex3.py C:\Users\liljo\OneDrive\Documents\My_repos\First_repo\Homework\goit-hw-05\log_file.log error