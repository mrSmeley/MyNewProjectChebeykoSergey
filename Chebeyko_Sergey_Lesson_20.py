# ДЗ на понедельник (Chebeyko_Sergey_Lesson_20.py)
# Вы создаете БД для учета задач в команде разработки.
# Вам необходимо создать базу данных для хранения информации о задачах и их статусе.
# Каждая задача должна иметь уникальный идентификатор, название, описание и статус (выполнена или невыполнена).
# Напишите программу на языке Python, которая создает базу данных SQLite,
# добавляет в нее несколько задач и позволяет пользователю получать информацию о задачах.

import sqlite3

conn = sqlite3.connect('TheSQL_task.db')
cursor = conn.cursor()
cursor.execute(
                '''CREATE TABLE IF NOT EXISTS tasks(
                ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                TASK_NAME TEXT, 
                DESCRIPTION TEXT, 
                 STATUS TEXT)'''
               )

exit_cmd = ''
while exit_cmd != 'n':
    task_name = input('Enter the name of the task: ')
    task_description = input('Task description: ')
    status = input('Status (done/not done): ')
    cursor.execute('''INSERT INTO tasks(TASK_NAME, DESCRIPTION, STATUS) VALUES(?,?,?)''', (task_name, task_description, status))
    conn.commit()
    exit_cmd= input('The data are entered in the table tasks! \n Continue(Enter)/Exit(n)')

cursor.execute('''SELECT * FROM tasks''')
data = cursor.fetchall()
for task in data:
    print(*task, sep=' / ')
conn.close()