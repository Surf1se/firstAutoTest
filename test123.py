user  = ["1", "2", "3", "4"]

name = "Dasha"

person = {
    "name" : name,
    "age" : 22,
    "isAdmin" : True,
    "registration_adres" : {
        "city" : "Moscow",
        "street" : "Lybyanka",
        "house" : 5
    }
}

# person["name"] = "Marina"


"""
remove - удаляем из массива данные
append - добавляем в массив данные 

"""

user.append("123123")
user.remove("1")



print (len(user))
print (user)
print (person)
print (person["registration_adres"]["city"])