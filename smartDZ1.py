# прроверка корректности записи строк или числа\

while True:
    age = input("age : ")
    if not age.isdigit():
        print ("hyinya, vse po novoy")
    else:
        print("vse norm")
        break
print("zakon4ili")

while True:
    name = input("name :")
    if name.isdigit():
        print("hyinya, povtoryi")
    else:
        print("vse norm")
        break
print("ahyenno, teper zakon4ili")
