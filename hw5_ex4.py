def input_error(func):  #декоратор input_error для обробки помилок введення
    def inner(*args, **kwargs): #виклик функції, яка обробляється декоратором
        try:
            return func(*args, **kwargs)
        except KeyError: #якщо ключ у словнику не знайдено
            return "Please provide a valid command."
        except ValueError: # якщо невірно введені дані
            return "Invalid input format."
        except IndexError: #якщо нехватає кількості аргументів
            return "Insufficient arguments provided."
    return inner

contacts = {} #створюємо словник для зюерігання контаків

@input_error
def add_contact(args): #ф-ція для додавання контатктів
    if not args:
        return "Enter the argument for the command"
    if len(args) < 2:
        return "Please provide both name and phone number."
    name, phone = args
    contacts[name] = phone #додаємо контакт до словнику
    return "Contact added."

@input_error
def retrieve_contact(args): #ф-ція для пошуку контакту за ім*ям
    if not args:
        return "Enter the argument for the command"
    name = args[0]
    if name in contacts: # повернення контакту, якщо він знайдений
        return f"{name}: {contacts[name]}"
    else: #якщо контакт не знайдено, виводимо повідомлення
        return "Contact not found."

@input_error
def list_all_contacts(): # ф-ція для виведення всіх контактів
    if not contacts:
        return "No contacts available." 
    #створюємо рядок з усіма контактами (ім*я, номер)
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def change_contact(args):  #ф-ція для зміни інформації про контакт
    if len(args) < 2:
        return "Please provide both name and new phone number."
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact information updated."
    else:
        return "Contact not found."

def main(): # основна ф-ція програми
    while True: #запит команди від користувачв
        command = input("Enter a command: ").strip().split(maxsplit=1)
        if not command:
            continue
        action = command[0]
        #розділемо команди на дію і аргументи
        args = command[1].split() if len(command) > 1 else []

        if action == "add": # виклик ф-ції для додавання контакту
            print(add_contact(args))
        elif action == "phone": #пошук контакту 
            print(retrieve_contact(args))
        elif action == "all": #виклик ф-ції для виведення всіх контаків
            print(list_all_contacts())
        elif action == "change":  
            print(change_contact(args))  #обробка команди "change"
        elif action == "exit":
            break #вихід з програми
        else:
            print("Invalid command. Please try again.") # додаємо повідомлення про введену невідому команлу

if __name__ == "__main__":
    main()