from tkinter import *
class book():
    L2 = []
    L3 = []
    def __init__(self):                             #метод записывает данные из исходного файла
        self.f1 = open('Вицукаева_данные.txt', 'r') #в список по строкам и создаёт еще один список,
        self.L = self.f1.readlines()                #состоящий из каждого слова в строке по отдельности
        self.f1.close()
        for self.i in self.L:
            self.L2 = self.i.split(';')
            self.L3 = self.L3 + self.L2
    def opr(self):
        self.mx1 = 0
        self.mx2 = 0
        self.mx3 = 0                                  #метод определяет самое длинное слово среди каждого из столбцов 
        for self.i in range(5,len(self.L3)+5,5):    #"название", "автор" и "издательство", после этого к каждому слову из этих столбцов дописывает
            if len(self.L3[self.i-5])>self.mx1:     #количество пробелов так, чтобы длдина каждой строки была равна длине максимальной
                self.mx1 = len(self.L3[self.i-5])   
        for self.i in range(5,len(self.L3)+5,5):
            if len(self.L3[self.i-4])>self.mx2:
                self.mx2 = len(self.L3[self.i-4])
        for self.i in range(5,len(self.L3)+5,5):
            if len(self.L3[self.i-3])>self.mx3:
                self.mx3 = len(self.L3[self.i-3])
        for self.i in range(5, len(self.L3)+5, 5):
            self.y1 = len(self.L3[self.i - 5])
            self.y2 = len(self.L3[self.i - 4])
            self.y3 = len(self.L3[self.i - 3])
            self.y11 = self.mx1 - self.y1
            self.y21 = self.mx2 - self.y2
            self.y31 = self.mx3 - self.y3
            while self.y11 != 0:
                self.L3[self.i - 5] = self.L3[self.i - 5] + ' '
                self.y11 = self.y11 - 1
            while self.y21 != 0:
                self.L3[self.i - 4] = self.L3[self.i - 4] + ' '
                self.y21 = self.y21 - 1
            while self.y31 != 0:
                self.L3[self.i - 3] = self.L3[self.i - 3] + ' '
                self.y31 = self.y31 - 1
    def __str__(self):                              #выводит на экран имя файла
        self.str11 = str(self.f1.name)
        b2.delete(0,END)
        b2.insert(0, str(self.str11))
    def vivod(self):                                #с помощью табуляции выравниваем текст, полученный в методе opr() по строкам
        self.L4 = ''
        for self.i in range(5,len(self.L3)+5,5):
            self.x = self.L3[self.i-5] + "\t" + self.L3[self.i-4] + "\t" + self.L3[self.i-3] + "\t" + self.L3[self.i-2] + "\t" + self.L3[self.i-1]
            self.L4 = self.L4 + self.x
    def file(self):                                 #записывает в файл информацию
        self.f2 = open('Вицукаева_данные_запись.txt', 'w')
        self.f2.writelines(self.L4)
        self.f2.close()
    def mx(self):                                   #ищет название книги с максимальной ценой
        self.mx4 = 0
        for self.i in range(9,len(self.L3),5):
            self.f = int(self.L3[self.i])
            if self.f>self.mx4:
                self.mx4 = self.f
                self.naz = self.L3[self.i - 4]
        b4.delete(0,END)
        b4.insert(0, self.naz)
        b5.delete(0,END)
        b5.insert(0, self.mx4)
    def izd(self):                                  #ищет название издательства по названию книги
        self.nazv = str(b6.get())
        self.pro = 0
        for self.i in range(len(self.L3)):
            if self.L3[self.i].find(self.nazv) != -1:
                self.pro = 1
                self.i1 = self.i
        if self.pro == 1:
            b7.delete(0,END)
            b7.insert(0, self.L3[self.i1 + 2])
        else:
                self.izd2 = 'Книга не найдена'
                b7.delete(0,END)
                b7.insert(0, self.izd2)                
    def kol(self):                                  #определяет нужно ли докупить книги с заданным названием
        self.nazv = str(b8.get())
        self.pro2 = 0
        for self.i in range(len(self.L3)):
            if self.L3[self.i].find(self.nazv) != -1:
                self.pro2 = 1
                self.i2 = self.i
        if (self.pro2 == 1) and (int(self.L3[self.i2 + 3])<50) and (int(self.L3[self.i2 + 3])>0):
            self.kol2 = 'Необходимо докупить'
            b9.delete(0,END)
            b9.insert(0, self.kol2)
        elif (self.pro2 == 1) and (int(self.L3[self.i2 + 3])>=50):
            self.kol3 = 'Книг достаточное количество'
            b9.delete(0,END)
            b9.insert(0, self.kol3)
        elif (self.pro2 == 1) and (int(self.L3[self.i2 + 3]) == 50):
            self.kol4 = 'Книг осталось мало'
            b9.delete(0,END)
            b9.insert(0, self.kol4)
        else:
            self.kol4 = 'Книга не найдена'
            b9.delete(0,END)
            b9.insert(0, self.kol4)
#---------------------------
def sozd():                 #пользовательская функция, которая позволяет создать объект класса
    l1 = book()
    l1.__str__()
    
def file1():                #пользовательская функция, которая позволяет записать данные в файл
    l1 = book()
    l1.opr()
    l1.vivod()
    l1.file()

def mx1():                  #пользовательская функция, которая позволяет найти книгу с максимальной ценой
    l1 = book()
    l1.mx()
    
def izd1():                 #пользовательская функция, которая позволяет найти издательство книги по названию
    l1 = book()
    l1.izd()
    
def kol1():                 #пользовательская функция, которая позволяет проверить наличие книг в магазинах
    l1 = book()
    l1.kol()

root = Tk()

root.title('Книжный магазин «Червячок»')

z0 = Label(root, text = ' ', font = 'consolas 8')
z0.grid(row = 0, column = 0, sticky = W)

z1 = Label(root, text = ' ', font = 'consolas 8')
z1.grid(row = 14, column = 3, sticky = W)

a1 = Button(root, text = 'Создать объект и вывести имя файла', font = 'consolas 8', command = sozd)
a1.grid(row = 1, column = 1, columnspan = 2, sticky = W)

a2 = Label(root, text = 'Имя файла', font = 'consolas 8')
a2.grid(row = 2, column = 1, sticky = W, pady = "4")

b2 = Entry(root, width = "35")
b2.grid(row = 2, column = 2, pady = "4")

c3 = Button(root, text = 'Вывести данные в файл', font = 'consolas 8', command = file1)
c3.grid(row = 3, column = 1, sticky = W)

a4 = Label(root, text = 'Название', font = 'consolas 8')
a4.grid(row = 4, column = 1, sticky = W, pady = "4")

b4 = Entry(root, width = "35")
b4.grid(row = 4, column = 2, pady = "4")

a5 = Label(root, text = 'Цена', font = 'consolas 8')
a5.grid(row = 5, column = 1, sticky = W, pady = "4")

b5 = Entry(root, width = "35")
b5.grid(row = 5, column = 2, pady = "4")

c5 = Button(root, text = 'Вывести максимальную цену и название', font = 'consolas 8', command = mx1)
c5.grid(row = 6, column = 1, columnspan = 2, sticky = W)

a6 = Label(root, text = 'Введите название', font = 'consolas 8')
a6.grid(row = 7, column = 1, sticky = W, pady = "4")

b6 = Entry(root, width = "35")
b6.grid(row = 7, column = 2, sticky = N, pady = "4")

a7 = Label(root, text = 'Издательство', font = 'consolas 8')
a7.grid(row = 8, column = 1, sticky = W, pady = "4")

b7 = Entry(root, width = "35")
b7.grid(row = 8, column = 2, sticky = N, pady = "4")

c7 = Button(root, text = 'Проверить издательство', font = 'consolas 8', command = izd1)
c7.grid(row = 9, column = 1, sticky = W)

a8 = Label(root, text = 'Введите название', font = 'consolas 8')
a8.grid(row = 10, column = 1, sticky = W, pady = "4")

b8 = Entry(root, width = "35")
b8.grid(row = 10, column = 2, sticky = N, pady = "4")

a9 = Label(root, text = 'Количество', font = 'consolas 8')
a9.grid(row = 11, column = 1, sticky = W, pady = "4")

b9 = Entry(root, width = "35")
b9.grid(row = 11, column = 2, sticky = N, pady = "4")

c9 = Button(root, text = 'Проверить наличие', font = 'consolas 8', command = kol1)
c9.grid(row = 12, column = 1, sticky = W, pady = "4")

Bt = Button(root, text="Выход", font = 'consolas 8', command = root.quit)
Bt.grid(row = 13, column = 1, columnspan = 2, sticky = N)

root.mainloop()
root.destroy()