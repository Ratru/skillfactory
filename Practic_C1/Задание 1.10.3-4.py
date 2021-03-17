# Задание 1.10.3

class User:
    def __init__(self, name, surname, city, balance=0):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def get_info_full(self):
        return f"Клиент «{self.name} {self.surname}». Город: {self.city}. Баланс: {self.balance} руб."

    def get_info(self):
        return f"{self.name} {self.surname} - г.{self.city}"


user1 = User("Иван", "Петров", "Москва", 50)
print(user1.get_info_full())
print("\n")
# Задание 1.10.4

user2 = User("Николай", "Смирнов", "Москва", )
user3 = User("Александр", "Лазарев", "Новосибирск", 150)
user4 = User("Иван", "Аксёнов", "Санкт-Петербург", )
user5 = User("Петр", "Исаев", "Уфа", 550)

user = [user1, user2, user3, user4, user5, ]
for sur in user:
    print(sur.get_info())
