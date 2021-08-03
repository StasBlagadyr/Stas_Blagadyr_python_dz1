name = input("Введите ваше имя: ")
name2 = input("Введите вашу фамилию: ")
age = int(input("Ваш возраст: "))
weight = int(input("Ваш вес: "))

if age <= 30 and (weight >= 50 and weight <= 80):
    print(name + " " + name2 + ",", str(age), "лет(год)" + ",", "вес", str(weight), "- Вы в неплохой форме")
elif age <= 30 and weight < 40:
    print(name + " " + name2 + ",", str(age), "лет(год)" + ",", "вес", str(weight), "- нужно набирать вес")
elif age < 20 and weight > 60:
    print(name + " " + name2 + ",", str(age), "лет" + ",", "вес", str(weight), "- вы очень молоды и с таким весом стоит обратиться к врчу")
elif age <= 30 and weight > 100:
    print(name + " " + name2 + ",", str(age), "лет(год)" + ",", "вес", str(weight), "- нужно сбрасывать вес")
elif (age > 30 and age <= 40) and (weight < 50 or weight > 120):
    print(name + " " + name2 + ",", str(age), "лет(год)" + ",", "вес", str(weight), "- следует заняться собой")
elif (age > 30 and age <= 40) and (weight >= 50 and weight <= 120):
    print(name + " " + name2 + ",", str(age), "лет(год)" + ",", "вес", str(weight), "- вы в норме")
elif age > 40 and (weight >= 50 and weight <= 120):
    print(name + " " + name2 + ",", str(age), "лет(год)" + ",", "вес", str(weight), "- вы в норме")
else:
    print("Введите информацию еще раз!")







