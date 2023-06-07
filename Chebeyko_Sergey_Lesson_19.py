#ДЗ на четверг (Chebeyko_Sergey_Lesson_19.py)
# Класс Company:
# Создайте класс Company
# Создайте статическое свойство levels, которое будет содержать (как словарь) все уровни квалификации программиста: 1:junior, 2:middle, 3:senior, 4:lead.
# Создайте метод __init__(), внутри которого будут определены два protected свойства: 1) _index - передается параметром и 2) _level - принимает из словаря levels значение с ключом _index
# init(self, index)
# self._index = index
# self.level = levels[index]
# Создайте метод _level_up(), который будет переводить программиста на следующий уровень
# Создайте метод is_lead(), который будет проверять, что программист достиг последней квалификации
# Класс Programmer:
# Создайте класс Programmer
# Создайте метод __init__(), внутри которого будут определены 3 динамических свойства: 1) name - передается параметром, является публичным, 2)age - возраст 3) level – уровень квалификации на основе словаря из Company
# Создайте метод work(), который заставляет программиста работать, что позволяет ему становиться более квалифицированным с помощью метода _level_up() родительского класса
# Создайте мeтод info(), который выведет информацию о вас: имя, возраст, квалификацию
# Создайте статический метод knowledge_base(), который выведет в консоль справку по программированию (просто любой текст).

# Вызовите справку по программированию
# Создайте объекты классов Company и Programmer
# Используя объект класса Programmer, повысьте свой уровень квалификации
# Дойдите до уровня lead
class Company:
    level = {
                1: 'junior',
                2: 'middle',
                3: 'senior',
                4: 'lead'
             }

    def __init__(self, index):
        self._index = index
        self._level = Company.level[self._index]

    def _level_up(self):
        if self.is_lead():
            print('Вы и так уже "Лучший", куда Больше?')
        else:
            self._index += 1
            print('Поздравляю! Вы повысили уровень до: ', Company.level[self._index])


    def is_lead(self):
        if self._index == len(Company.level):
            return True
        else:
            return False

class Programmer(Company):

    def __init__(self, name, age, level):
        super().__init__(level)
        self.name = name
        self.age = age
        self.level = level

    def work(self):
        self._level_up()

    def info(self):
        print(f'Name: {self.name} \nAge: {self.age} \nLevel: {Company.level[self.level]}')
    @staticmethod
    def knowledge_base():
        print('База знаний по программированию!')

Programmer.knowledge_base()

Dobronom = Company(1)
Person_1 = Programmer('Chebeyko', 33, 1)

Person_1.info()
Person_1.work()
Person_1.work()
Person_1.work()
Person_1.work()
