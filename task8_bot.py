# Задание

# Напишите консольного бота помощника, который будет распознавать команды, вводимые с клавиатуры, и отвечать согласно введенной команде.

# Бот помощник должен стать для нас прототипом приложения-ассистента. Приложение-ассистент в первом приближении должен уметь работать с книгой контактов и календарем. В этой домашней работе сосредоточимся на интерфейсе самого бота. Наиболее простой и удобный на начальном этапе разработки интерфейс - это консольное приложение CLI(Command Line Interface). CLI достаточно просто реализовать. Любой CLI состоит из трех основных элементов:

#     Парсер команд. Часть, которая отвечает за разбор введенных пользователем строк, выделение из строки ключевых слов и модификаторов команд.
#     Функции обработчики команд — набор функций, которые ещё называют handler, они отвечают за непосредственное выполнение команд.
#     Цикл запрос-ответ. Эта часть приложения отвечает за получение от пользователя данных и возврат пользователю ответа от функции-handlerа.

# На первом этапе наш бот-ассистент должен уметь сохранять имя и номер телефона, находить номер телефона по имени, изменять записанный номер телефона, выводить в консоль все записи, которые сохранил. Чтобы реализовать такую несложную логику, воспользуемся словарем. В словаре будем хранить имя пользователя как ключ и номер телефона как значение.
# Условия

# Бот должен находиться в бесконечном цикле, ожидая команды пользователя.
#  Бот завершает свою работу, если встречает слова: .
#   Бот не чувствительный к регистру вводимых команд.
#    Бот принимает команды:
#         "hello", отвечает в консоль "How can I help you?"
#         "add ...". По этой команде бот сохраняет в памяти(в словаре например) новый контакт. Вместо ... пользователь вводит имя и номер телефона, обязательно через пробел.
#         "change ..." По этой команде бот сохраняет в памяти новый номер телефона для существующего контакта. Вместо ... пользователь вводит имя и номер телефона, обязательно через пробел.
#         "phone ...." По этой команде бот выводит в консоль номер телефона для указанного контакта. Вместо ... пользователь вводит имя контакта, чей номер нужно показать.
#         "show all". По этой команде бот выводит все сохраненные контакты с номерами телефонов в консоль.
#         "good bye", "close", "exit" по любой из этих команд бот завершает свою роботу после того, как выведет в консоль "Good bye!".
#     Все ошибки пользовательского ввода должны обрабатываться при помощи декоратора input_error. Этот декоратор отвечает за возврат пользователю сообщений вида "Enter user name", "Give me name and phone please" и т.п. Декоратор input_error должен обрабатывать исключения, которые возникают в функциях-handler(KeyError, ValueError, IndexError) и возвращать соответствующий ответ пользователю.
#     Логика команд реализована в отдельных функциях и эти функции принимают на вход одну или несколько строк и возвращают строку.
#     Вся логика взаимодействия с пользователем реализована в функции main, все print и input происходят только там.

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Invalid command. Please try again."
        except ValueError:
            return "Invalid input. Please try again."
        except IndexError:
            return "Invalid command. Please try again."
    return wrapper


contacts = {}


@input_error
def add_contact(name, phone):
    contacts[name] = phone
    return "Contact added successfully."


@input_error
def change_phone(name, phone):
    contacts[name] = phone
    return "Phone number updated successfully."


@input_error
def get_phone(name):
    return contacts[name]


@input_error
def show_all_contacts():
    if not contacts:
        return "No contacts found."
    result = "Contacts:\n"
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result


def main():
    print("Welcome to the Assistant Bot!")
    while True:
        command = input("Enter a command: ").lower()

        if command == "hello":
            print("How can I help you?")
        elif command.startswith("add "):
            _, name, phone = command.split(" ")
            print(add_contact(name, phone))
        elif command.startswith("change "):
            _, name, phone = command.split(" ")
            print(change_phone(name, phone))
        elif command.startswith("phone "):
            _, name = command.split(" ")
            print(get_phone(name))
        elif command == "show all":
            print(show_all_contacts())
        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
