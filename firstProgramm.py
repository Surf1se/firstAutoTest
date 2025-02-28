# dobavlenie i sortirovka dannih
bugReportConteinerHigh = []
bugReportConteinerLow = []

countBug = int(input("Сколько багов вы хотите добавить? "))
lvlTheBug = input("Какой уровень бага вы добвляете? low или high? ")

i = 0 # переменная для циклов
if lvlTheBug == "high":
    while i < countBug:
        i += 1
        case = input("Ввкдите название бага: ")
        bugReportConteinerHigh.append(case)
        containeraaa = bugReportConteinerHigh

elif lvlTheBug == "low":
    while i < countBug:
        i += 1
        case = input("Ввкдите название бага: ")
        bugReportConteinerLow.append(case)
        containeraaa = bugReportConteinerLow

print(f"У нас получилось багов с {lvlTheBug} приоритетом {countBug}, их названия : {containeraaa}")





