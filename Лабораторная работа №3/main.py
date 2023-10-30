import json


def input_strings():
    with open('F1.txt', 'w') as f1:
        while True:
            line = input("Введите строку (пустая строка для завершения ввода): ")
            if not line:
                break
            f1.write(line + '\n')


def filter_strings():
    with open('F2.txt', 'w') as f2:
        with open('F1.txt', 'r') as f1:
            for line in f1:
                if not any(char.isdigit() for char in line):
                    f2.write(line)


def count_words_in_last_line():
    with open('F2.txt', 'r') as f2:
        lines = f2.readlines()
        if lines:
            last_line = lines[-1]
            words = len(last_line.split())
            print(f"Количество слов в последней строке файла F2: {words}")
        else:
            print("Файл F2 пуст.")


def process_bank_clients():
    with open('Клиент банка.txt', 'r') as file:
        zero_balance_clients = []
        total_investment = 0

        for line in file:
            parts = line.split()
            if len(parts) == 3:
                name, balance, _ = parts
                balance = int(balance)
                total_investment += balance
                if balance == 0:
                    zero_balance_clients.append(name)

        if zero_balance_clients:
            print("Клиенты с нулевым балансом:")
            for client in zero_balance_clients:
                print(client)
        else:
            print("Нет клиентов с нулевым балансом.")

        print(f"Общая сумма вложений всех клиентов: {total_investment}")


def process_subjects():
    with open('предметы.txt', 'r') as file:
        subjects_dict = {}

        for line in file:
            parts = line.split(':')
            if len(parts) == 2:
                subject_name, details = parts
                lesson_counts = [int(count.split('(')[0]) for count in details.split()]

                total_lessons = sum(lesson_counts)
                subjects_dict[subject_name.strip()] = total_lessons

        print("Словарь с количеством занятий по предметам:")
        print(subjects_dict)


def process_firms():
    data = [
        "firm_1 ООО 10000 5000",
        "firm_2 ЗАО 8000 5000",
        "firm_3 ИП 1500 2000",
    ]

    with open("firm_data.txt", "w") as file:
        for line in data:
            file.write(line + "\n")

    firm_data = []
    with open("firm_data.txt", "r") as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 4:
                name, ownership, revenue, costs = parts
                profit = int(revenue) - int(costs)
                if profit >= 0:
                    firm_data.append({name: profit})

    total_profit = 0
    num_profitable_firms = 0

    for firm in firm_data:
        profit = list(firm.values())[0]
        total_profit += profit
        num_profitable_firms += 1

    average_profit = total_profit / num_profitable_firms if num_profitable_firms > 0 else 0

    result_list = [dict(average_profit=average_profit)]
    for firm in firm_data:
        result_list[0].update(firm)

    with open("firm_data.json", "w") as json_file:
        json.dump(result_list, json_file, ensure_ascii=False, indent=4)

    print("Список и средняя прибыль сохранены в файле 'firm_data.json'.")


def main_menu():
    while True:
        print("Меню:")
        print("1. Ввести строки в файл F1")
        print("2. Фильтровать строки и записать в файл F2")
        print("3. Подсчитать количество слов в последней строке файла F2")
        print("4. Обработать клиентов банка")
        print("5. Обработать предметы")
        print("6. Обработать фирмы")
        print("7. Выход")

        choice = input("Выберите опцию: ")

        if choice == '1':
            input_strings()
        elif choice == '2':
            filter_strings()
        elif choice == '3':
            count_words_in_last_line()
        elif choice == '4':
            process_bank_clients()
        elif choice == '5':
            process_subjects()
        elif choice == '6':
            process_firms()
        elif choice == '7':
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")


if __name__ == "__main__":
    main_menu()
