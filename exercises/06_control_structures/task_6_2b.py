# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
flag = True
while flag == True:
    ip = input("Введите адрес: ")
    oct = ip.split('.')
    for item in oct:
        if not item.isdigit() or int(item) not in range(0,256) or len(oct)!=4:
            flag = False
    if flag == True:
        if int(oct[0])>=1 and int(oct[0])<=223 and len(oct)==4:
            print("unicast")
        elif int(oct[0])>=224 and int(oct[0])<=239:
            print("multicast")
        elif ip == "255.255.255.255":
            print("local broadcast")
        elif ip == "0.0.0.0":
            print("unassigned")
        else:
            print("unused")
        break
    else:
        print("Неправильный IP-адрес")
