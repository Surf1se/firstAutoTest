person = {
    "name" : "Svyat",
    "age" : "22"
}
print(person)

del person["name"] # удаляем пару из словаря по ключу
print(person)

person["name"] = "Andrey" # добавляем пару в словарь
print(person)

person["age"] = 25 # изменяем пару в словаре
print(person)

# КОРТЕЖ
# кортеж неотзя изменить после его создания
# но сожно выдернуть из него значение
coordinates = (10, 20, 30)
print(coordinates[2])