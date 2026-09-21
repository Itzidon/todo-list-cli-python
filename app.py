import csv

todos = []


def add_one_task(title):
    todos.append(title)


def print_list():
    if len(todos) == 0:
        print("\nNo hay tareas pendientes.")
    else:
        print("\nLista de tareas:")
        for index, task in enumerate(todos, start=1):
            print(f"{index}. {task}")


def delete_task(number_to_delete):
    index = number_to_delete - 1

    if 0 <= index < len(todos):
        deleted_task = todos.pop(index)
        print(f"\nTarea eliminada: {deleted_task}")
    else:
        print("\nNúmero de tarea no válido.")


def save_todos():
    with open("todos.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        for task in todos:
            writer.writerow([task])


def load_todos():
    global todos

    try:
        with open("todos.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            todos = [row[0] for row in reader if row]
    except FileNotFoundError:
        todos = []


def main():
    load_todos()

    while True:
        print("\n--- TODO LIST ---")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Eliminar tarea")
        print("4. Salir")

        option = input("\nElige una opción: ").strip()

        if option == "1":
            title = input("Escribe la tarea: ").strip()

            if title:
                add_one_task(title)
                save_todos()
                print("\nTarea agregada.")
            else:
                print("\nLa tarea no puede estar vacía.")

        elif option == "2":
            print_list()

        elif option == "3":
            print_list()

            if len(todos) > 0:
                try:
                    number = int(input("\nNúmero de tarea a eliminar: "))
                    delete_task(number)
                    save_todos()
                except ValueError:
                    print("\nDebes escribir un número.")

        elif option == "4":
            save_todos()
            print("\nTareas guardadas. ¡Hasta luego!")
            break

        else:
            print("\nOpción no válida.")


if __name__ == "__main__":
    main()