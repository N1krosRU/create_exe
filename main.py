import datetime

name = input("Input your name: ")
print(f"Hello {name}, i am Python")
now = datetime.datetime.now()
print(f"Current time: {now.hour} hour {now.minute} minutes")
input('Press ENTER to exit')

# Для начала установи pyinstaller:
# pip install pyinstaller

# Перейди в папку в с проектом и выполни:
# pyinstaller main.py
# -F > создание всего проекта в одном файле .exe
# -i "D:\python\projects\create_exe\hacker.ico" > добавление иконки к экзешнику
# -w > прячет консоль при выполнении программы

# Пример создания файла .exe:
# pyinstaller -F -i "D:\python\projects\create_exe\hacker.ico" main.py
