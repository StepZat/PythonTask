# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input()
oct = ip.split('.')
flag = True
r = range(0,256)
for item in oct:
#    print("Число - {0}, Является ли числом - {1}, входит в нужный диапазон - {2}". format(item, item.isdigit(), int(item) in r))
    if not item.isdigit() or int(item) not in range(0,256):
        flag = False
if len(oct)==4 and flag == True:
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
else:
    print("Неправильный IP-адрес")
