# Todo List CLI con Python

Aplicación de línea de comandos desarrollada en Python para gestionar una lista de tareas.

## Funcionalidades

- Agregar nuevas tareas
- Mostrar las tareas con posición numérica
- Eliminar una tarea por su número
- Guardar las tareas en `todos.csv`
- Cargar las tareas guardadas al volver a ejecutar el programa
- Agregar varias tareas durante una misma ejecución

## Tecnologías

- Python 3
- Librería estándar de Python
- CSV para persistencia de datos

## Cómo ejecutar

Desde esta carpeta, ejecuta:

python main.py

Aparecerá un menú con estas opciones:

1. Agregar tarea
2. Ver tareas
3. Eliminar tarea
4. Guardar tareas
5. Cargar tareas
6. Salir

## Funciones principales

- add_one_task(title)
- print_list()
- delete_task(number_to_delete)
- save_todos()
- load_todos()

El archivo todos.csv se genera automáticamente al guardar tareas.
