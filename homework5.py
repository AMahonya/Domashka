immutable_var = 'aple',15,True
print (immutable_var)
#immutable_var[3] = False
# В кортеже нельзя изменить
# или добавить какой либо элемент
# так как в кортеже это не поддерживаеться,
# и предназначен он в коде для того что бы
# случайно не изменить какие то важные данные
# или данные которые не стоит менять
# однако если бы в кортеже были бы указаны данные
# в виде СПИСКА то данные относящиеся к списку
# мы бы могли изменить
        # naprimer
#immutable_var = ['aple'],15,True
#print (immutable_var)
#immutable_var[0][0] = 'banana'
#print (immutable_var)
mutable_list = [15,False,'univer']
mutable_list[0] = 358
mutable_list[1] = True
mutable_list[2] = 'Учебное заведение'
print(mutable_list)