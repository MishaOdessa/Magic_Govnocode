import tkinter as tk
from tkinter import messagebox
import os
import sys

win2 = tk.Tk()
win2.geometry("500x500")
win2.title("ПРЕДЫСТОРИЯ")

# Функция y, которая была не определена
def y():
  win2.destroy()

def e():
  win1.destroy()

# lbl=tk.Label(win2, text = "Это произошло ровно сто лет назад или раньше, или позже, мир сотрясли великие землетрясения открывшие разлом, которые показали путь демонам и все эти события перевернули мир. Произошло это около Синих гор. Они начали порабощать территории, уничтожая всё на своём пути, так они дошли до Темерии. Темерия осознав, всю сложность ситуации, решила создать альянс с Глорианой, Соденом, Каэдвеном. Они согласились, спустя время, создать армию, которая попытается отбить замок Элландер(имеющий большое стратегическое значение). Армия прибыла в город Хагге, и через неделю отправилась в первый рейд. Рейд не увенчался успехом, войско разгромили, выжило лишь 100 человек из 4000. Те кто выжили, смогли принести трофеи чудищ и странные кристаллы, наполненные светом, в них была какае-то странная эссенция. После изучения кристаллов стало понятно, что кристаллы имеют магическую силу, ученые начали экспериментировать, и выяснилось, что они дают магические способности. Было понятно, что это единственный способ победить демонов и использовать их для нашей армии, но это давало колоссальную нагрузку на тело. Демоны не сидели на месте и продвигались на запад, захватив город Хагге и замок Каррерас, они были в 90 километрах от Вызимы. Решающие сражение за Вызиму прошло в степях Бренна, армия демонов составляла около 1700, армия людей была примерно 2800 человек. Сражение закончилось поражением демонов, но какой ценой? Спустя некоторое время демонов отбросили за Венгерберг. За этот период времени погибло 150000 людей. Люди все лучше изучали магию и она стала их главным оружием, магия требовала ману. Появилась нежить.Стало известно, что демоны боятся солнца. ").pack()

lbl = tk.Label(win2,text="Это произошло ровно сто лет назад или раньше, или позже, мир сотрясли").pack()

lbl = tk.Label(win2,text="великие землятрясения открывшие разлом, которые показали путь демонам ").pack()

lbl = tk.Label(win2,text="и все эти события превернули мир. Произошло это около Синих гор.  Они ").pack()

lbl = tk.Label(win2,text=
  "начали порабощать територии уничтожая всё на своём пути, так они дошли").pack()

lbl = tk.Label(win2,text="до Темерии. Темерия осознав, всю сложность ситуации решила создать").pack()

lbl = tk.Label(win2,text="альянс с Глорианой, Соденом, Каэдвеном. Они согласились, спустя время, ").pack()

lbl = tk.Label(win2,text="создать армию, которая попытается отбить замок Элландер(имеющий ").pack()

lbl = tk.Label(win2,text="большое стратегическое значение). Армия прибыла в город Хагге,  и через").pack()

lbl = tk.Label(win2,text=" неделю отправилась в первый рейд. Рейд не увенчался успехом, войско").pack()

lbl = tk.Label(win2,text="разгромили, выжило лишь 100 человек из 4000.  Те кто выжили,").pack()

lbl = tk.Label(win2,text="смогли принести трафеи чудищ и странные кристаллы, наполненные светом,").pack()

lbl = tk.Label(win2,text=" в них была какае-то странная эссенция. После изучения кристаллов стало").pack()

lbl = tk.Label(win2,text="понятно, что кристаллы имеют магическую силу, ученые начали").pack()

lbl = tk.Label(win2,text="экспериментировать, и выяснилось, что они дают магические способности.").pack()

lbl = tk.Label(
  win2,
  text="Было понятно, что это единственый способ победить демонов").pack()

lbl = tk.Label(win2,text="и использовать их нашей армии, но это давало колоссальную нагрузку ").pack()

lbl = tk.Label(win2,text="на тело. Демоны не сидели на месте и продвигались на запад, захватив").pack()
lbl = tk.Label(win2,text="город Хагге и замок Каррерас, они были в 90 километрах от Вызимы.").pack()

lbl = tk.Label(win2,text=" Решающие сражение за Вызиму прошло в степях Бренна, армия демонов ").pack()

lbl = tk.Label(win2,text="составляла около 1700, армия людей была примерно 2800 человек. Сраже-").pack()

lbl = tk.Label(win2,text="ние закончилось поражением демонов,но какой ценой? Спустя").pack()

lbl = tk.Label(win2,text="некоторое время демонов отбросили за Венгерберг. За этот период времени").pack()

lbl = tk.Label(win2,text=" погибло 150000 людей. Люди все лучше изучали магию и она стала их ").pack()

lbl = tk.Label(win2,text="главным оружием, магия требовала ману. Появилась нежить. ").pack()

lbl = tk.Label(win2,text="Стало известно, что демоны боятся солнца.").pack()

tk.Button(win2, text="продолжить", bd=5, command=y).pack()

win1 = tk.Tk()
win1.geometry("500x500")
win1.title("ПЕРВАЯ ГЛАВА - НАЧАЛО")

lbl = tk.Label(win1, text="ГЛАВА ПЕРВАЯ - НАЧАЛО").pack()

lbl = tk.Label(win1,text=
  "  Вы новичок рыцарского ордена 'Oчистителей' по имени Фубуки и вы можете "
).pack()

lbl = tk.Label(win1, text="выбрать себе магию:").pack()

rtr = tk.StringVar()

#tk.Entry(win1, textvariable = rtr).pack()


def e():
  win1.destroy()


fram = tk.Frame(win1)
tk.Button(fram, text="  огня  ", bd=5, command=e).grid(column=1,
row=1,
stick="wens",
padx=5,
pady=5)
tk.Button(fram, text="земли(не сделано)", bd=5, command=e).grid(column=2,
row=1,
stick="wens",
padx=5,
pady=5)
tk.Button(fram, text="льда(не сделано)", bd=5, command=e).grid(column=1,
row=2,
stick="wens",
padx=5,
pady=5)
tk.Button(fram, text="молнии(не сделано)", bd=5, command=e).grid(column=2,row=2,stick="wens",padx=5,pady=5)

fram.pack()


def q():
  messagebox.showinfo(
    "Огонь",
    "огненная орба - маленький огненый шарик (средняя атака), огненный поток - огонь из руки, которая выжигает всё на своём пути(ближняя атака), свечка - а что вы думаете?Обычная свечка только из пальца(вообще не атака, просто чтобы в темноте видно было)."
  )


def w():
  messagebox.showinfo(
    "земля",
    "каменная стена - стена из под земли(защита), подземный шип - шип который поевляеться из под земли(смешаная атака), бронежилет - на вашей броне поебляеться земля которая усиливает вашу броню(защита)"
  )


def r():
  messagebox.showinfo(
    "лёд",
    "морозное дыхание - лёд из руки, который замораживает и сковывает движение(ближния атака), леденой осколок - маленький ледяной осколок(средняя атака), морозная рука - замораживает прикосновением(разные могут быть ситуации)"
  )


def t():
  messagebox.showinfo(
    "молния",
    "вспышка - скачёк на растояние 1,5 метра (перемещение), разряд - маленький молненый шарик(средния атака), флешка - цепляется к поверхности,когда что-то приближается взрывается и ослепляет(ловушка) "
  )


lbl = tk.Label(win1, text="Магия огня даёт: огненная орба, огненный поток, свечка").pack()

tk.Button(win1, text="точнее", bd=5, command=q).pack()

lbl1 = tk.Label(win1,text="Магия земли даёт: каменная стена, подземный шип, бронежилет").pack()

tk.Button(win1, text="точнее", bd=5, command=w).pack()

lbl = tk.Label(win1,text="Магия льда даёт: морозное дыхание, леденой осколок, морозная рука"
).pack()

tk.Button(win1, text="точнее", bd=5, command=r).pack()

lbl = tk.Label(win1, text="Магия молнии даёт: вспышка, разряд, флешка").pack()

tk.Button(win1, text="точнее", bd=5, command=t).pack()

#--------------------------------------------------------------------

#------------------------------------------------------------------------------------------

win3 = tk.Tk()
win3.geometry("500x500")
win3.title("ПЕРВАЯ ГЛАВА - НАЧАЛО")

lbl = tk.Label(win3, text="Сегодня мой первый день в ордене.").pack()
lbl = tk.Label(win3, text="Как мне сказали:'чтоб в шесть был как штык в главной зале.'").pack()
lbl = tk.Label(win3,text="Территория ордина находилась в главном замке, вход на неё разрешался "
).pack()
lbl = tk.Label(win3, text="лишь членам ордена и королевской знати.").pack()
lbl1 = tk.Label(win3,text="'Эй мелкий! Как тебя там, Фубуки'. 'Иди сюда'").pack()


def ehdfhg():
  win3.destroy()
  win4.destroy()


def edhf():
  win3.destroy()
  win5.destroy()


fram3 = tk.Frame(win3)

#tk.Button(fram3, text="  Подойти  ",bd=5,command= ehfg ).grid(column=1,row=1,stick="wens",padx=5, pady=5)
tk.Button(fram3, text="'Ты кто такой? '", bd=5,command=ehdfhg).grid(column=1, row=1, stick="wens", padx=5, pady=5)
tk.Button(fram3, text="  'Я?' ", bd=5, command=edhf).grid(column=2,
row=1,
stick="wens",
padx=5,
pady=5)
#tk.Button(fram3, text="проигнорировать",bd=5,command = ehewt ).grid(column=2,row=2,stick="wens",padx=5, pady=5)

fram3.pack()

#--я---------------------------------------------

win4 = tk.Tk()
win4.geometry("500x500")
win4.title("ПЕРВАЯ ГЛАВА - НАЧАЛО")

lbl = tk.Label(win4, text="'Нет я. Ты, конечно а кто еще? '").pack()
lbl = tk.Label(win4, text="'Я твой напарник, моё имя Сэм, сегодня мы").pack()
lbl = tk.Label(win4, text="идём патрулировать восточную часть города.'").pack()
lbl = tk.Label(win4, text="'Просто слушайся моих приказов и все пройдёт нормально.").pack()
lbl = tk.Label(win4, text="Я понятно объясняю?'").pack()

#  os.execl(sys.executable, sys.executable, *sys.argv)
# ^ для смертей

fram4 = tk.Frame(win4)


def ttrrr():
  win4.destroy()
  win6.destroy()


def ttrrrr():
  win4.destroy()
  win7.destroy()


tk.Button(fram4, text="С чего это?", bd=5, command=ttrrr).grid(column=1,
row=1,
stick="wens",
padx=5,
pady=5)

tk.Button(fram4, text="Да.", bd=5, command=ttrrrr).grid(column=1,row=2,
stick="wens",
padx=5,
pady=5)

fram4.pack()

#ты кто такой-------------------------

win5 = tk.Tk()
win5.geometry("500x500")
win5.title("ПЕРВАЯ ГЛАВА - НАЧАЛО")

lbl = tk.Label(win5,text="'Привет я твой напарник, моё имя Сэм, сегодня мы").pack()
lbl = tk.Label(win5, text="идём патрулировать восточную часть города.'").pack()
lbl = tk.Label(win5, text="'Просто слушайся моих приказов и все пройдёт нормально.").pack()

fram5 = tk.Frame(win5)


def ttrr():
  win5.destroy()
  win6.destroy()


def ttr():
  win5.destroy()
  win7.destroy()


tk.Button(fram5, text="С чего это?", bd=5, command=ttrr).grid(column=1,
row=1,
stick="wens",
padx=5,
pady=5)

tk.Button(fram5, text="Хорошо.", bd=5, command=ttr).grid(column=1,
row=2,
stick="wens",
padx=5,
pady=5)

fram5.pack()
#------------------------------------


def dfsh():
  win7.destroy()


win7 = tk.Tk()
win7.geometry("500x500")
win7.title("ПЕРВАЯ ГЛАВА - НАЧАЛО")

lbl = tk.Label(win7, text="'Потому что я старше тебя салага!'").pack()

tk.Button(win7, text="дальше", bd=5, command=dfsh).pack()

win6 = tk.Tk()
win6.geometry("500x500")
win6.title("ПЕРВАЯ ГЛАВА - НАЧАЛО")


def ghdh():
  win6.destroy()


lbl = tk.Label(win6, text="'Отлично тогда давай выступаем.'").pack()

tk.Button(win6, text="дальше", bd=5, command=ghdh).pack()

win8 = tk.Tk()
win8.geometry("500x500")
win8.title("ПЕРВАЯ ГЛАВА - НАЧАЛО")

lbl = tk.Label(win8,text="Восточная часть Вызимы была довольно бедной - узенькие улицы,").pack()
lbl = tk.Label(win8,text="маленькие бедные дома, такое ощущение что стоит хлопнуть дверью").pack()
lbl = tk.Label(win8,text="и они развалятся, но зато тут всё дешевле, чем в других местах").pack()
lbl = tk.Label(win8,text="города. Конечно тут мало товаров но при этом тараканы отменно свежи.").pack()
#lbl=tk.Label(win8, text = "Восточная часть Вызимы была довольно бедной: узенькие улици, маленькие бедные дома такое ощущение что стоит хлопнуть дверью и они разваляться, но зато тут всё дешевле чем в других частях города конечно тут мало товаров но зато тараканы отменно свежи.").pack()
lbl = tk.Label(win8,text="'Эй, видишь, там валяеться алкаш, только пол седьмого а уже напился.'").pack()
lbl = tk.Label(win8, text="'Пойди и пни его.'").pack()

fram6 = tk.Frame(win8)


def drfyh():
  win8.destroy()


def drhgh():
  win8.destroy()
  win9.destroy()
  win11.destroy()
  win12.destroy()
  win13.destroy()
  win14.destroy()
  win15.destroy()
  win16.destroy()
  win17.destroy()
  win18.destroy()
  win19.destroy()
  win20.destroy()
  win21.destroy()
  win22.destroy()
  win23.destroy()
  win24.destroy()
  win25.destroy()
  win26.destroy()
  win27.destroy()
  win28.destroy()
  win29.destroy()
  win30.destroy()
  win31.destroy()
  win32.destroy()
  win33.destroy()
  win34.destroy()
  win35.destroy()
  
tk.Button(fram6, text="Пнуть", bd=5, command=drhgh).grid(column=1,
row=1,
stick="wens",
padx=5,
pady=5)
tk.Button(fram6, text="Чего‽", bd=5, command=drfyh).grid(column=2,
row=1,
stick="wens",
padx=5,
pady=5)
#tk.Button(fram6, text="'А может сразу ему горло перерезать?'",bd=5,command=ttr).grid(column=1,row=2,columnspan=2,stick="wens",padx=5, pady=5)

fram6.pack()

win9 = tk.Tk()
win9.geometry("500x500")
win9.title("ПЕРВАЯ ГЛАВА - НАЧАЛО")

lbl = tk.Label(win9, text="Того, делай что приказывают!").pack()


def gjd():
  win9.destroy()
  win11.destroy()
  win13.destroy()
  win12.destroy()
  win14.destroy()
  win15.destroy()
  win16.destroy()
  win17.destroy()
  win18.destroy()
  win19.destroy()
  win20.destroy()
  win21.destroy()
  win22.destroy()
  win23.destroy()
  win24.destroy()
  win25.destroy()
  win26.destroy()
  win27.destroy()
  win28.destroy()
  win29.destroy()
  win30.destroy()
  win31.destroy()
  win32.destroy()
  win33.destroy()
  win34.destroy()
  win35.destroy()

def gfh():
  win9.destroy()
  win10.destroy()
  

fram7 = tk.Frame(win9)
tk.Button(fram7, text="Пнуть", bd=5, command=gjd).grid(column=1,row=1,stick="wens",padx=5,pady=5)
tk.Button(fram7, text="Нет.", bd=5, command=gfh).grid(column=2,row=1,stick="wens",padx=5,pady=5)

fram7.pack()
win10 = tk.Tk()
win10.geometry("500x500")
win10.title("ПЕРВАЯ ГЛАВА - НАЧАЛО")

def ttdg():
  win10.destroy()
  #win11.destroy()
  
lbl = tk.Label(win10, text="'Отлично салага.'").pack()
lbl = tk.Label(win10,text="Так и проходило патрулирование, мы избивали пьяниц и занимались всякой").pack()
lbl = tk.Label(win10,text="другой ерундой, никогда не думал что буду тут таким заниматься.").pack()

tk.Button(win10, text="Дальше", bd=5, command=ttdg).pack()

win11 = tk.Tk()
win11.geometry("500x500")
win11.title("ПЕРВАЯ ГЛАВА - НАЧАЛО")

lbl = tk.Label(win11, text="'Тогда я сам, Вообше с тебя толку нет '").pack()

fram9 = tk.Frame(win11)

def ddg():
  win11.destroy()
  win13.destroy()
  win14.destroy()
  win15.destroy()
  win16.destroy()
  win17.destroy()
  win18.destroy()
  win19.destroy()
  win20.destroy()
  win21.destroy()
  win22.destroy()
  win23.destroy()
  win24.destroy()
  win25.destroy()
  win26.destroy()
  win27.destroy()
  win28.destroy()
  win29.destroy()
  win30.destroy()
  win31.destroy()
  win32.destroy()
  win33.destroy()
  win34.destroy()
  win35.destroy()

def ddh():
  win11.destroy()
  



tk.Button(fram9, text="Промолчать", bd=5, command=ddg).grid(column=1,row=1,stick="wens",padx=5,pady=5)

tk.Button(fram9, text="'Стой! Оставь его!'", bd=5, command=ddh).grid(column=2,row=1,stick="wens",padx=5,pady=5)

fram9.pack()

win13 = tk.Tk()
win13.geometry("500x500")
win13.title("ПЕРВАЯ ГЛАВА - НАЧАЛО")

lbl = tk.Label(win13, text="'Чё ты сказал дрыщ?!По морде получить хочешь!?Хочешь с ним валяться?!А!?'").pack()

fram10 = tk.Frame(win13)

def dddg():
  win13.destroy()
  win12.destroy()

def dddh():
  win13.destroy()
  win14.destroy()
  win15.destroy()
  win16.destroy()
  win17.destroy()
  win18.destroy()
  win19.destroy()
  win20.destroy()
  win21.destroy()
  win22.destroy()
  win23.destroy()
  win24.destroy()
  win25.destroy()
  win26.destroy()
  win27.destroy()
  win28.destroy()
  win29.destroy()
  win30.destroy()
  win31.destroy()
  win32.destroy()
  win33.destroy()
  win34.destroy()
  win35.destroy()
  
tk.Button(fram10, text="Начать драку", bd=5, command=dddg).grid(column=1,row=1,stick="wens",padx=5,pady=5)

tk.Button(fram10, text="Дать ему избить.", bd=5, command=dddh).grid(column=2,row=1,stick="wens",padx=5,pady=5)

fram10.pack()

win12 = tk.Tk()
win12.geometry("500x500")
win12.title("ПЕРВАЯ ГЛАВА - НАЧАЛО")

def tdd():
  win12.destroy()

lbl = tk.Label(win12, text="'Эй алкаш, ты знаешь где тут больница? Давно там был?'.").pack()
lbl = tk.Label(win12, text="'Аааа чего?'").pack()
lbl = tk.Label(win12, text="Так и проходило патрулирование, мы избивали пьяниц и занимались всякой").pack()
lbl = tk.Label(win12, text="другой ерундой, никогда не думал что буду тут таким заниматься").pack()

tk.Button(win12, text="Дальше", bd=5, command=tdd).pack()

win14 = tk.Tk()
win14.geometry("500x500")
win14.title("ПЕРВАЯ ГЛАВА - НАЧАЛО")

lbl = tk.Label(win14, text="Враг стоит в блоке, ваше действие:").pack()

fram11 = tk.Frame(win14)

def ddgbi():
  win14.destroy()
  win15.destroy()
  win16.destroy()

def ddydsi():
  win14.destroy()
  win17.destroy()
  win16.destroy()

def dguii():
  win14.destroy()
  win15.destroy()
  win17.destroy()

tk.Button(fram11, text="стоять в блоке и говорить: иди сюда, петушара", bd=5, command=dguii).grid(column=1,row=1,columnspan=2,stick="wens",padx=5,pady=5)
tk.Button(fram11, text="использовать магию(огненная орба, пламя)", bd=5, command=ddgbi).grid(column=1,row=2,columnspan=2,stick="wens",padx=5,pady=5)
tk.Button(fram11, text="начать атаковать", bd=5, command=ddydsi).grid(column=1,row=3,columnspan=2,stick="wens",padx=5,pady=5)

fram11.pack()

win15 = tk.Tk()
win15.geometry("500x500")
win15.title("ПЕРВАЯ ГЛАВА - НАЧАЛО")

lbl = tk.Label(win15, text="Вы начали атоковать и вас поймали на контратаке, вы получив по").pack()
lbl = tk.Label(win15, text="челюсти, упали на землю.").pack()

def gdfj():
  os.execl(sys.executable, sys.executable, *sys.argv)

tk.Button(win15, text="заново", bd=5, command=gdfj).pack()

win17 = tk.Tk()
win17.geometry("500x500")
win17.title("ПЕРВАЯ ГЛАВА - НАЧАЛО")

lbl = tk.Label(win17, text="Вы использовали огненную орбу, но Сэм поставил каменную стену и отро-").pack()
lbl = tk.Label(win17, text="зил вашу атаку и сразу за этим использовал подземный шип, и убивает вас.").pack()

def gdf():
  os.execl(sys.executable, sys.executable, *sys.argv)

tk.Button(win17, text="заново", bd=5, command=gdf).pack()

win16 = tk.Tk()
win16.geometry("500x500")
win16.title("ПЕРВАЯ ГЛАВА - НАЧАЛО")

lbl = tk.Label(win16, text="Сэм не выдеражал и накинулся на вас, ваши действия:").pack()

fram12 = tk.Frame(win16)

def fshc():
  win16.destroy()
  win19.destroy()
  win20.destroy()
  
def dgdji():
  win16.destroy()
  win18.destroy()
  win20.destroy()
  
def pgfi():
  win16.destroy()
  win18.destroy()
  win19.destroy()
  
tk.Button(fram12, text="блокировать удары", bd=5, command=fshc).grid(column=1,row=1,columnspan=2,stick="wens",padx=5,pady=5)
tk.Button(fram12, text="Контратаковать", bd=5, command=dgdji).grid(column=1,row=2,columnspan=2,stick="wens",padx=5,pady=5)
tk.Button(fram12, text="увернуться", bd=5, command=pgfi).grid(column=1,row=3,columnspan=2,stick="wens",padx=5,pady=5)

fram12.pack()

win18 = tk.Tk()
win18.geometry("500x500")
win18.title("ПЕРВАЯ ГЛАВА - НАЧАЛО")

lbl = tk.Label(win18, text="Вы блокируете удары но Сэм смог пробить").pack()
lbl = tk.Label(win18, text="ваш блок и выбить пару зубов он вас вырубил.").pack()

tk.Button(win18, text="заново", bd=5, command=gdf).pack()

win20 = tk.Tk()
win20.geometry("500x500")
win20.title("ПЕРВАЯ ГЛАВА - НАЧАЛО")

lbl = tk.Label(win20, text="Вы попытались увернуться, но Сэм смог вас зацепить и вы потеряли").pack()
lbl = tk.Label(win20, text="равновесие, и упали, вас вырубил.").pack()

tk.Button(win20, text="заново", bd=5, command=gdf).pack()

win19 = tk.Tk()
win19.geometry("500x500")
win19.title("ПЕРВАЯ ГЛАВА - НАЧАЛО")

lbl = tk.Label(win19, text="Вы успешно бьете его в челюсть и выбиваете пару зубов, враг упал, ").pack()
lbl = tk.Label(win19, text="ваши действия:").pack()
fram14 = tk.Frame(win19)

def fshc():
  win19.destroy()
  
def dgdji():
  win19.destroy()
  win22.destroy() 
  win27.destroy()
  win28.destroy()
  win29.destroy()
  win30.destroy()
  win31.destroy()
  win32.destroy()
  win33.destroy()
  win34.destroy()
  win35.destroy()
  
def pgfi():
  win19.destroy()
  win21.destroy() 
  win22.destroy() 
  win23.destroy() 
  win24.destroy() 
  win25.destroy() 
  win26.destroy() 
  
tk.Button(fram14, text="Пинать ногами", bd=5, command=dgdji).grid(column=1,row=1,columnspan=2,stick="wens",padx=5,pady=5)
tk.Button(fram14, text="Ничего не делать", bd=5, command=pgfi).grid(column=1,row=2,columnspan=2,stick="wens",padx=5,pady=5)
tk.Button(fram14, text=" Убить (⌒‿⌒)", bd=5, command=fshc).grid(column=1,row=3,columnspan=2,stick="wens",padx=5,pady=5)              

fram14.pack()

#Мордобой: Враг стоит в блоке, ваше действие: 1+ стоять в блоке и говорить: иди сюда петушара; 2- начать атаковать; 3- использовать магию(огненная орба, пламя).1.1 Сэм не выдеражал и накинулся на вас, ваши действия: 1- блокировать удары; 2+ Контратаковать; 3- увернуться. 2.2 Вы успешно бьете его в челюсть и выбиваете пару зубов, враг упал, ваши действия: 1- Пинать ногами; 2+ Ничего не делать; 3- Убить (⌒‿⌒)   """
# ^ текст

win22 = tk.Tk()
win22.geometry("500x500")
win22.title("ПЕРВАЯ ГЛАВА - НАЧАЛО")

lbl = tk.Label(win22, text="Вы достаёте меч и отрубаете ему голову. Во круг крик, паника и вы").pack()
lbl = tk.Label(win22, text="чувствуете удар в спину, и умераете.").pack()

lbl = tk.Label(win22, text="Помните!!! Карма сушествует.").pack()

tk.Button(win22, text="заново", bd=5, command=gdf).pack()

win27 = tk.Tk()
win27.geometry("500x500")
win27.title("ПЕРВАЯ ГЛАВА - НАЧАЛО")

lbl = tk.Label(win27, text="'Спасибо! Если бы не вы, то он от моего мужа и жывого места не оставил.'").pack()
lbl = tk.Label(win27, text="'Всё таки есть нормальные люди в ордене'").pack()
lbl = tk.Label(win27, text="'Вот возьмите тут немного, но вам пригодиться.'").pack()

def pgfi():
  win27.destroy() 
  

fram20 = tk.Frame(win27)

tk.Button(fram20, text="'Не надо'", bd=5, command=pgfi).grid(column=1,row=1,columnspan=2,stick="wens",padx=5,pady=5)
tk.Button(fram20, text="'Спасибо'", bd=5, command=pgfi).grid(column=1,row=2,columnspan=2,stick="wens",padx=5,pady=5)


fram20.pack()

win28 = tk.Tk()
win28.geometry("500x500")
win28.title("ПЕРВАЯ ГЛАВА - НАЧАЛО")

lbl = tk.Label(win28, text="Вы взяли Сэма на плечи и понесли в лазарет.").pack()
lbl = tk.Label(win28, text="'О! Это что за спящая красавица?'").pack()
lbl = tk.Label(win28, text="'Неужели опять с пьяницей подрался?'").pack()

fram21 = tk.Frame(win28)

def fhg():
  win28.destroy()
  win29.destroy()

def ffg():
  win28.destroy()
  win30.destroy()

tk.Button(fram21, text="'Опять?'", bd=5, command=fhg).grid(column=1,row=1,columnspan=2,stick="wens",padx=5,pady=5)
tk.Button(fram21, text="'Нет.'", bd=5, command=ffg).grid(column=1,row=2,columnspan=2,stick="wens",padx=5,pady=5)

fram21.pack()

win29 = tk.Tk()
win29.geometry("500x500")
win29.title("ПЕРВАЯ ГЛАВА - НАЧАЛО")

lbl = tk.Label(win29, text="'Хм, Странно, ладно сейчас ему дадим ").pack()
lbl = tk.Label(win29, text="Оренофоса понюхать, мигом проснёться.'").pack()

fram22 = tk.Frame(win29)

def ffgy():
  win29.destroy()
  win32.destroy()

def gsdg():
  win29.destroy()
  win31.destroy()
  
tk.Button(fram22, text="'Оренопопус? Чего?'", bd=5, command=ffgy).grid(column=1,row=1,columnspan=2,stick="wens",padx=5,pady=5)
tk.Button(fram22, text="Зделать вид, что вы поняли.", bd=5, command=gsdg).grid(column=1,row=2,columnspan=2,stick="wens",padx=5,pady=5)

fram22.pack()

win30 = tk.Tk()
win30.geometry("500x500")
win30.title("ПЕРВАЯ ГЛАВА - НАЧАЛО")

lbl = tk.Label(win30, text="'Да, он любит до них докапаться, ладно сейчас'").pack()
lbl = tk.Label(win30, text="'ему дадим Оренофоса понюхать, мигом проснётся.'").pack()

fram23 = tk.Frame(win30)

def ffgy():
  win30.destroy()
  win32.destroy()

def gdffff():
  win30.destroy()
  win31.destroy()

tk.Button(fram23, text="'Оренопопус? Чего?'", bd=5, command=ffgy).grid(column=1,row=1,columnspan=2,stick="wens",padx=5,pady=5)
tk.Button(fram23, text = "Зделать вид, что вы поняли." , bd=5, command=gdffff).grid(column=1,row=2,columnspan=2,stick="wens",padx=5,pady=5)

fram23.pack()

win31 = tk.Tk()
win31.geometry("500x500")
win31.title("ПЕРВАЯ ГЛАВА - НАЧАЛО")

lbl = tk.Label(win31, text="Не оренопопус, а оренофос, цветок такой, издаёт").pack()
lbl = tk.Label(win31, text="ужасный запах, от него и мёртвого разбудить можно").pack()
lbl = tk.Label(win31, text="Медсестра достала какой-то здоровый цветок, который вонял за три мили.").pack()
lbl = tk.Label(win31, text="Сэм проснулся, но нормально не соображал.").pack()
lbl = tk.Label(win31, text="'Оставьте его у нас пока что.'").pack()
lbl = tk.Label(win31, text="И тут заходит генерал").pack()
lbl = tk.Label(win31, text="'Так, Фубуки, бегом за мной.'").pack()

def fhs():
  win31.destroy()

tk.Button(win31, text="Идти", bd=5, command=fhs).pack()

win32 = tk.Tk()
win32.geometry("500x500")
win32.title("ПЕРВАЯ ГЛАВА - НАЧАЛО")

lbl = tk.Label(win32, text="Медсестра достала какой-то здоровый цветок, который вонял за три мили.").pack()
lbl = tk.Label(win32, text="Сэм проснулся, но нормально не соображал.").pack()
lbl = tk.Label(win32, text="'Оставьте его у нас пока что.'").pack()
lbl = tk.Label(win32, text="И тут заходит генерал").pack()
lbl = tk.Label(win32, text="'Так, Фубуки, бегом за мной.'").pack()

def fdug():
  win32.destroy()

tk.Button(win32, text="Идти", bd=5, command=fdug).pack()

win33 = tk.Tk()
win33.geometry("500x500")
win33.title("ПЕРВАЯ ГЛАВА - НАЧАЛО")

fram24 = tk.Frame(win33)

def fgfd():
  win33.destroy()
  win34.destroy()

def fddh():
  win33.destroy()

lbl = tk.Label(win33, text="'К нам поступило заявление, что Сэм пытался'").pack()
lbl = tk.Label(win33, text="избить некого гражданина на патрулировании, это так?'").pack()

tk.Button(fram24, text="'Да'", bd=5, command=fgfd).grid(column=1,row=1,columnspan=2,stick="wens",padx=5,pady=5)
tk.Button(fram24, text="'Нет'", bd=5, command=fddh).grid(column=1,row=2,columnspan=2,stick="wens",padx=5,pady=5)

fram24.pack()

win34 = tk.Tk()
win34.geometry("500x500")
win34.title("ПЕРВАЯ ГЛАВА - НАЧАЛО")

lbl = tk.Label(win34, text="'И зачем, ты, обманываешь? Ты, же тут не причём.'").pack()
lbl = tk.Label(win34, text="'Ладно, на первый раз прощаю, но поступишь так ещё раз").pack()
lbl = tk.Label(win34, text="пойдешь за ним, понял?!'").pack()

def fddh():
  win34.destroy()

tk.Button(win34, text="'Так точно.'", bd=5, command=fddh).pack()

win35 = tk.Tk()
win35.geometry("500x500")
win35.title("ПЕРВАЯ ГЛАВА - НАЧАЛО")

lbl = tk.Label(win35, text="'Так Сэма под арест а ты повышаешся до второго").pack()
lbl = tk.Label(win35, text="'уровня и вот твои 25 золотых за патрулирование.'").pack()

def fddh():
  win35.destroy()
  win36.destroy()
  
tk.Button(win35, text="'Спасибо.'", bd=5, command=fddh).pack()


win21 = tk.Tk()
win21.geometry("500x500")
win21.title("ПЕРВАЯ ГЛАВА - НАЧАЛО")

lbl = tk.Label(win21, text="Вы его пинаете и вдруг получаете по горбу, и вырубаетесь.").pack()
lbl = tk.Label(win21, text="Вы просыпаетесь в сырой комнате и слышите:").pack()
lbl = tk.Label(win21, text="'О проснулся? Что вы за балаган устроили? Вроде взрослые люди.'").pack()

fram15 = tk.Frame(win21)

def fshc():
  win21.destroy()
  win24.destroy()

def dgdji():
  win21.destroy()
  win26.destroy()
  
tk.Button(fram15, text="'Он хотел избить человека, я помешал.'", bd=5, command=fshc).grid(column=1,row=1,columnspan=2,stick="wens",padx=5,pady=5)
tk.Button(fram15, text="'Прошу прошения, такого больше не повторится'", bd=5, command=dgdji).grid(column=1,row=2,columnspan=2,stick="wens",padx=5,pady=5)

fram15.pack()

win26 = tk.Tk()
win26.geometry("500x500")
win26.title("ПЕРВАЯ ГЛАВА - НАЧАЛО")

def dgdh():
  win26.destroy()

lbl = tk.Label(win26, text="'Мы знаем, этот Сэм такая тварь, мы его столько  ").pack()
lbl = tk.Label(win26, text="предупреждали, что б он не безпределил и вот доигрался, на него заявление").pack()
lbl = tk.Label(win26, text="написали, теперь он сидеть будет.'").pack()

frammy = tk.Frame(win26)

tk.Button(frammy, text="'Что со мной будет?'", bd=5, command=dgdh).grid(column=1,row=1,columnspan=2,stick="wens",padx=5,pady=5)

tk.Button(frammy, text="'Отлично'", bd=5,command=dgdh).grid(column=1,row=2,columnspan=2,stick="wens",padx=5,pady=5)

frammy.pack()

win24 = tk.Tk()
win24.geometry("500x500")
win24.title("ПЕРВАЯ ГЛАВА - НАЧАЛО")

fram19 = tk.Frame(win24)

def fjhgvb():
  win24.destroy()

lbl = tk.Label(win24, text="'Ты поступил правильно, этот Сэм такая тварь, мы его столько  ").pack()
lbl = tk.Label(win24, text="предупреждали, что б он не безпределил и вот доигрался, на него заявление").pack()
lbl = tk.Label(win24, text="написали, теперь он сидеть будет.'").pack()

tk.Button(fram19, text="'Что со мной будет?'", bd=5, command=fjhgvb).grid(column=1,row=1,columnspan=2,stick="wens",padx=5,pady=5)
tk.Button(fram19, text="'Отлично'", bd=5, command=fjhgvb).grid(column=1,row=2,columnspan=2,stick="wens",padx=5,pady=5)

fram19.pack()

fram16 = tk.Frame(win24)

def dgewrti():
  win24.destroy()

tk.Button(fram16, text="'Что со мной будет?'", bd=5, command=dgewrti).grid(column=1,row=1,columnspan=2,stick="wens",padx=5,pady=5)
tk.Button(fram16, text="'Отлично'", bd=5, command=dgewrti).grid(column=1,row=2,columnspan=2,stick="wens",padx=5,pady=5)

fram16.pack()

win25 = tk.Tk()
win25.geometry("500x500")
win25.title("ПЕРВАЯ ГЛАВА - НАЧАЛО")

lbl = tk.Label(win25, text="'А да совсем забыл, собирайся, вешать").pack()
lbl = tk.Label(win25, text="тебя будем, за не выполнения приказа.'").pack()

fram17 = tk.Frame(win25)

def ghbk():
  win25.destroy()

tk.Button(fram17, text="'Что?!'", bd=5, command=ghbk).grid(column=1,row=1,columnspan=2,stick="wens",padx=5,pady=5)
tk.Button(fram17, text="'Вы, что совсем крышей поехали?!'", bd=5, command=ghbk).grid(column=1,row=2,columnspan=2,stick="wens",padx=5,pady=5)

fram17.pack()

lbl = tk.Label(win21, text="").pack()

win23 = tk.Tk()
win23.geometry("500x500")
win23.title("ПЕРВАЯ ГЛАВА - НАЧАЛО")

lbl = tk.Label(win23, text="Расслабься, шучу я, на тебе за дежурство").pack()
lbl = tk.Label(win23, text="25 золотых,вещи возмёшь у сторожа на выходе").pack()

fram18 = tk.Frame(win23)

def dfskh():
  win23.destroy()
  win36.destroy()
  
fram18 = tk.Frame(win23)

tk.Button(fram18, text="'Спасибо'", bd=5, command=dfskh).grid(column=1,row=2,columnspan=2,stick="wens",padx=5,pady=5)

fram18.pack()

win36 = tk.Tk()
win36.geometry("500x500")
win36.title("ПЕРВАЯ ГЛАВА - НАЧАЛО")

lbl = tk.Label(win36, text="Мы вернулись в замок и встретили генерала").pack()
lbl = tk.Label(win36, text="'Балваны! Что вы творите?! Посреди белого дня пинаете ").pack()
lbl = tk.Label(win36, text="людей, моё терпение кончилось! Сэм, ты задержан, а Ты ,Фубуки, ").pack()
lbl = tk.Label(win36, text="лишаешься зарплаты за патрулирование, бегом дальше патрулировать ").pack()
lbl = tk.Label(win36, text="в одиночку до 9 вечера! Как только закончишь, будешь'").pack()
lbl = tk.Label(win36, text="драить все доспехи в замке. Понятно?! '").pack()

fram25= tk.Frame(win36)

def tffh():
  win36.destroy()

tk.Button(fram25,text="'Так точно!.'", bd=5, command=tffh).grid(column=1,row=2,columnspan=2,stick="wens",padx=5,pady=5)

fram25.pack()

#Глава вторая - оборона замка Гингер. После событий с Сэмом, я начал патрулировать с новым напарником Кевином, все проходило гладко. Отличная новость, я получил второй уровень магии огня, а именно улучшился навык - огненная орба в огненный шар ( средняя, массовая атака), огненный поток в пламя (ближняя атака, усилилась температура огня и дальность) и появился навык огненная завеса(защита, огонь из под земли, который блокирует некоторые магические навыки). В один из дней, меня и примерно 350 ребят собрали в главном зале ордена. Нам сказали: Приказом сверху, я обязан отправить вас всех на помощь в замок Гингер. По информации замок находится под постоянными атаками примерно 3 дня, на него готовится осада, он полностью окружен. Отправка завтра, готовьтесь, когда вы будете возле блокпоста, на перекрестке, к вам присоединятся еще 100 человек. Выдвигаетесь завтра, приходите сюда же. Успокойте близких и отдыхайте. Хочу добавить, те кто не явятся, будут признаны дезертирами, и по законам венного времени пойдут на висельницу. 
#Следующий день. Я собрался, взял все самое необходимое и пошел в зал ордена. Я и все остальные выдвинулись в путь, на помощь. Это мой 1 бой, страшно, помирать вообще не хочется, ну с богом. Путь от Вызимы до замка долгий, около  360 км. 
#Первая остновка была в Каррерасе, вторая должна быть в блокпосте. Вот мы и приблежаемся к блокпосту и вдруг мы слышим взрывы, и крики. Когда мы подошли, то увидели, как демоны начали крушить блокпост. Я услышал: В атаку! Убьем демонов! Спасем всех выживших! Демоны не успели опомниться, как мы на них навалились.


win37 = tk.Tk()
win37.geometry("500x500")
win37.title("Глава вторая - оборона замка Гингер.")

lbl = tk.Label(win37, text="После событий с Сэмом, я начал патрулировать с новым напарником ").pack()
lbl = tk.Label(win37, text="Кевином, все проходило гладко. Отличная новость, я получил ").pack()
lbl = tk.Label(win37, text="второй уровень магии огня, а именно улучшился навык - огненная ").pack()
lbl = tk.Label(win37, text="орба в огненный шар ( средняя, массовая атака), огненный поток в ").pack()
lbl = tk.Label(win37, text="пламя (ближняя атака, усилилась температура огня и дальность) и ").pack()
lbl = tk.Label(win37, text="появился навык огненная завеса(защита, огонь из под земли, ").pack()
lbl = tk.Label(win37, text="который блокирует некоторые магические навыки). В один из дней, меня и примерно ").pack()
lbl = tk.Label(win37, text="350 ребят собрали в главном зале ордена. Нам сказали: Приказом ").pack()
lbl = tk.Label(win37, text="сверху, я обязан отправить вас всех на помощь в замок Гингер. По").pack()
lbl = tk.Label(win37, text="информации замок находится под постоянными атаками примерно 3 ").pack()
lbl = tk.Label(win37, text="дня, на него готовится осада, он полностью окружен. Отправка ").pack()
lbl = tk.Label(win37, text="завтра, готовьтесь, когда вы будете возле блокпоста, на ").pack()
lbl = tk.Label(win37, text="перекрестке, к вам присоединятся еще 100 человек. Выдвигаетесь ").pack()
lbl = tk.Label(win37, text="завтра, приходите сюда же. Успокойте близких и отдыхайте. Хочу ").pack()
lbl = tk.Label(win37, text="добавить, те кто не явятся, будут признаны дезертирами, и по ").pack()
lbl = tk.Label(win37, text="законам венного времени пойдут на висельницу.").pack()

fram26= tk.Frame(win37)

def tffh():
  win37.destroy()

tk.Button(fram26,text="Следующий день", bd=5, command=tffh).grid(column=1,row=2,columnspan=2,stick="wens",padx=5,pady=5)

fram26.pack()

win38 = tk.Tk()
win38.geometry("500x500")
win38.title("Глава вторая - оборона замка Гингер.")

lbl = tk.Label(win38, text="Я собрался, взял все самое необходимое и пошел в зал ордена. Я и ").pack()
lbl = tk.Label(win38, text="все остальные выдвинулись в путь, на помощь. Это мой 1 бой, ").pack()
lbl = tk.Label(win38, text="страшно, помирать вообще не хочется, ну с богом. Путь от Вызимы ").pack()
lbl = tk.Label(win38, text="до замка долгий, около  360 км.                          ").pack()
lbl = tk.Label(win38, text="Первая остновка была в Каррерасе, вторая должна быть в ").pack()
lbl = tk.Label(win38, text="блокпосте. Вот мы и приблежаемся к блокпосту и вдруг мы слышим ").pack()
lbl = tk.Label(win38, text="взрывы, и крики. Когда мы подошли, то увидели, как демоны начали ").pack()
lbl = tk.Label(win38, text="крушить блокпост. Я услышал: В атаку! Убьем демонов! Спасем всех ").pack()
lbl = tk.Label(win38, text="выживших! Демоны не успели опомниться, как мы на них навалились.").pack()
lbl = tk.Label(win38, text="Сражение начилось ночью." ).pack()
fram27= tk.Frame(win38)

def tffh():
  win38.destroy()

tk.Button(fram27,text="Вот мой 1 бой начался,", bd=5, command=tffh).grid(column=1,row=2,columnspan=2,stick="wens",padx=5,pady=5)

fram27.pack()

win39 = tk.Tk()
win39.geometry("500x500")
win39.title("Глава вторая - оборона замка Гингер.")

lbl = tk.Label(win39, text="Мы сразу набросились толпой на небольшую кучку демонов. Они  ").pack()
lbl = tk.Label(win39, text="начали защищаться. Те, кто шли в первых рядах смогли  убить ").pack()
lbl = tk.Label(win39, text="парочку, но ихнее щястье  длилось недолго, вдруг стало видно ").pack()
lbl = tk.Label(win39, text="как, некоторые поднимаются выше и начинают использовать магию, ").pack()
lbl = tk.Label(win39, text="весь первый, и второй ряд превратился в кучу опалённых,").pack()
lbl = tk.Label(win39, text="разорванных на клочья, разрезанных бездыханных тел. ").pack()

fram28= tk.Frame(win39)

def sdg():
  win39.destroy()
  win40.destroy()

def fghs():
  win39.destroy()
  win41.destroy()

tk.Button(fram28,text="Пытаться отойти назад", bd=5, command=fghs).grid(column=1,row=1,columnspan=1,stick="wens",padx=5,pady=5)
tk.Button(fram28,text="продолжать наступление", bd=5, command=sdg).grid(column=1,row=2,columnspan=2,stick="wens",padx=5,pady=5)

fram28.pack()

win40 = tk.Tk()
win40.geometry("500x500")
win40.title("Глава вторая - оборона замка Гингер.")

lbl = tk.Label(win40, text="Вы в страхе как последний трус пытаетесь отойти, но против толпы .").pack()
lbl = tk.Label(win40, text="не попрёшь и вы падаете, вас затоптали во время битвы.").pack()

tk.Button(win40, text="заново", bd=5, command=gdf).pack()

win41 = tk.Tk()
win41.geometry("500x500")
win41.title("Глава вторая - оборона замка Гингер.")

lbl = tk.Label(win41, text="Демоны опять начали использовать магию, но в них прилетает ").pack()
lbl = tk.Label(win41, text="Гарпун(Магия молнии) и слышно крик: 'Вперёд задавите их толпой, ").pack()
lbl = tk.Label(win41, text="а все кто имеет мощные дальние атаки создавайте их и атакуйте ").pack()
lbl = tk.Label(win41, text="магов, все с малым уровнем магии, и мощной защитой не дайте им ").pack()
lbl = tk.Label(win41, text="подойти к нам.' Вы стали ближе к первым рядам и видите как один ").pack()
lbl = tk.Label(win41, text="из демонов начал прорываться вперёд с помощью огненной спирали(Магия огня).").pack()

fram29= tk.Frame(win41)

def fget(): 
  win41.destroy()
  win42.destroy()

def dhg(): 
  win41.destroy()
  win43.destroy()

tk.Button(fram29,text="Оставить его и идти дальше", bd=5, command=dhg).grid(column=1,row=1,columnspan=1,stick="wens",padx=5,pady=5)
tk.Button(fram29,text="начать атаковать.", bd=5, command=fget).grid(column=1,row=2,columnspan=2,stick="wens",padx=5,pady=5)

fram29.pack()

win42 = tk.Tk()
win42.geometry("500x500")
win42.title("Глава вторая - оборона замка Гингер.")

lbl = tk.Label(win42, text="Вы начинаете помогать с другим демоном,").pack()
lbl = tk.Label(win42, text="но вдруг спираль попадает в вас и вы умираете.").pack()

tk.Button(win42, text="заново", bd=5, command=gdf).pack()

win43 = tk.Tk()
win43.geometry("500x500")
win43.title("Глава вторая - оборона замка Гингер.")

lbl = tk.Label(win43, text="Вы атакуете пламям(Магия огня), демон остановил свою атаку и ").pack()
lbl = tk.Label(win43, text="начал идти в вашу сторону, ваша атака его лишь немного ").pack()
lbl = tk.Label(win43, text="замедлила. Он готовиться к атаке.               ").pack()

fram30= tk.Frame(win43)

def dfhg(): 
  win43.destroy()
  win44.destroy()

def ddhfg(): 
  win43.destroy()
  win45.destroy()

tk.Button(fram30,text="Попробывать вонзить ему меч в горло.", bd=5, command=ddhfg).grid(column=1,row=1,columnspan=2,stick="wens",padx=5,pady=5)
tk.Button(fram30,text="Поставить огненую завесу.", bd=5, command=dfhg).grid(column=1,row=2,columnspan=2,stick="wens",padx=5,pady=5)

fram30.pack()

win44 = tk.Tk()
win44.geometry("500x500")
win44.title("Глава вторая - оборона замка Гингер.")

lbl = tk.Label(win44, text="Вы бежите на демона, но он атакует быстрее и пронзает вас.").pack()

def ddhfg(): 
  win44.destroy()
  
tk.Button(win44, text="заново", bd=5, command=gdf).pack()

win45 = tk.Tk()
win45.geometry("500x500")
win45.title("Глава вторая - оборона замка Гингер.")

lbl = tk.Label(win45, text="Вы ставите огненную завесу и вдруг она усиливаеться в ").pack()
lbl = tk.Label(win45, text="разы, демона отбросило на пару метров, и вас тоже. На ").pack()
lbl = tk.Label(win45, text="него сразу напали, но он отбросил их какой-то не ").pack()
lbl = tk.Label(win45, text="понятной магией, по крайней мере точно не огня и ").pack()
lbl = tk.Label(win45, text="побежал к вам, вдруг в него прилетает гарпун и вы ").pack()
lbl = tk.Label(win45, text="слышите:'Не ушибся малыш?'         ").pack()

fram31= tk.Frame(win45)

def sdgg(): 
  win45.destroy()
  win47.destroy()

def dgdgh(): 
  win45.destroy()
  win46.destroy()

tk.Button(fram31,text="Не спасибо", bd=5, command=sdgg).grid(column=1,row=1,columnspan=2,stick="wens",padx=5,pady=5)
tk.Button(fram31,text="Малышь? Ты, че абалдел?", bd=5, command=dgdgh).grid(column=1,row=2,columnspan=2,stick="wens",padx=5,pady=5)

fram31.pack()

win46 = tk.Tk()
win46.geometry("500x500")
win46.title("Глава вторая - оборона замка Гингер.")

lbl = tk.Label(win46, text="'На здоровье. Давай, подымайся и иди чёртиков рубить.'").pack()
lbl = tk.Label(win46, text="Вы встали и продолжили сражаться так вы смогли победить их.").pack()
lbl = tk.Label(win46, text="Потери демонов составили 200, а ваши 93 бойца.").pack()
lbl = tk.Label(win46, text="После сражения у блокпоста нас осталось 257 человек. На ").pack()
lbl = tk.Label(win46, text="половине пути к замку, мы попали в засаду демонов, как ").pack()
lbl = tk.Label(win46, text="это было: Я шел в конце армии с мечом в руках и на меня выпрыгнул демон.").pack()

fram32= tk.Frame(win46)

def fhghd(): 
  win46.destroy()
  win48.destroy()
def kfgh(): 
  win49.destroy()
  win46.destroy()

tk.Button(fram32,text="Попробывать уклоница.", bd=5, command=fhghd).grid(column=1,row=1,columnspan=2,stick="wens",padx=5,pady=5)
tk.Button(fram32,text="Попробувать рубануть его мечём", bd=5, command=kfgh).grid(column=1,row=2,columnspan=2,stick="wens",padx=5,pady=5)

fram32.pack()

win47 = tk.Tk()
win47.geometry("500x500")
win47.title("Глава вторая - оборона замка Гингер.")

lbl = tk.Label(win47, text="'Ох! Какой крикливый попался, может зря тебя спасал,'").pack()
lbl = tk.Label(win47, text="'ладно, давай подымайся и иди чёртиков рубить.'").pack()
lbl = tk.Label(win47, text="Вы встали и продолжили сражаться так вы смогли побидить их.").pack()
lbl = tk.Label(win47, text="Потери демонов составили 200, а ваши 93 бойца.").pack()
lbl = tk.Label(win47, text="После сражения у блокпоста нас осталось 257 человек. На ").pack()
lbl = tk.Label(win47, text="половине пути к замку, мы попали в засаду демонов, как ").pack()
lbl = tk.Label(win47, text="это было: Я шел в конце армии с мечом в руках и на меня выпрыгнул демон.").pack()


fram33= tk.Frame(win47)

def sdjfg(): 
  win47.destroy()
  win48.destroy()
def dfhg(): 
  win49.destroy()
  win47.destroy()

tk.Button(fram33,text="Попробывать уклоница.", bd=5, command=sdjfg).grid(column=1,row=1,columnspan=2,stick="wens",padx=5,pady=5)
tk.Button(fram33,text="Попробувать рубануть его мечём.", bd=5, command=dfhg).grid(column=1,row=2,columnspan=2,stick="wens",padx=5,pady=5)

fram33.pack()

win49 = tk.Tk()
win49.geometry("500x500")
win49.title("Глава вторая - оборона замка Гингер.")

lbl = tk.Label(win49, text="Вы пытаетесь укланица но не успиваете и демон отрубает вам голову.").pack()

tk.Button(win49, text="заново", bd=5, command=gdf).pack()

win48 = tk.Tk()
win48.geometry("500x500")
win48.title("Глава вторая - оборона замка Гингер.")

lbl = tk.Label(win48, text="Вы на реакции бьёте его и отрубаете голову.").pack()
lbl = tk.Label(win48, text="Замок уже виднелся вдалеке, скоро уже рассвет, а это ").pack()
lbl = tk.Label(win48, text="значит, что осада пройдет не удачно, демоны умирают от ").pack()
lbl = tk.Label(win48, text="солнечных лучей . Я увидел как замок горит, в его ").pack()
lbl = tk.Label(win48, text="стороне было огромное количество вспышек, от ").pack()
lbl = tk.Label(win48, text="использования магии, смрад от трупов доносился аж до").pack()
lbl = tk.Label(win48, text="сюда(дистанция около 500 м). Осада шла полным ходом, но ").pack()
lbl = tk.Label(win48, text="гарнизон очень хорошо держался. Я услышал: В атаку! На ").pack()
lbl = tk.Label(win48, text="помощь замку! На осадный лагерь!                ").pack()
lbl = tk.Label(win48, text="Все ринулись в бой. Я напал на одного из демонов,").pack()
lbl = tk.Label(win48, text=" он сразу отпрыгнул и стал в блоке.             ").pack()

fram34= tk.Frame(win48)

def dfgh(): 
  win48.destroy()
  win52.destroy()
  win51.destroy()

def dkghh(): 
  win48.destroy()
  win50.destroy()
  win52.destroy()

def hjfh(): 
  win48.destroy()
  win50.destroy()
  win51.destroy()

tk.Button(fram34,text="Стоять и ждать Атаки.", bd=5, command=dfgh).grid(column=1,row=1,columnspan=2,stick="wens",padx=5,pady=5)
tk.Button(fram34,text="Атаковать мечём.", bd=5, command=hjfh).grid(column=1,row=2,columnspan=2,stick="wens",padx=5,pady=5)
tk.Button(fram34,text="Атаковать огненным шаром(Магия огня).", bd=5, command=dkghh).grid(column=1,row=3,columnspan=2,stick="wens",padx=5,pady=5)

fram34.pack()

win50 = tk.Tk()
win50.geometry("500x500")
win50.title("Глава вторая - оборона замка Гингер.")

lbl = tk.Label(win50, text="Вы смотрите друг на друга и вдруг он покрываеться огнём, и исчезает,").pack()
lbl = tk.Label(win50, text="и через секунду появляется у вас за спиной, вас убили.").pack()

tk.Button(win50, text="заново", bd=5, command=gdf).pack()

win51 = tk.Tk()
win51.geometry("500x500")
win51.title("Глава вторая - оборона замка Гингер.")

lbl = tk.Label(win51, text="Вы кидает огненный шар, а демон исчезает и через секунду ").pack()
lbl = tk.Label(win51, text="появляеться у вас за спиной, вас убили.").pack()

tk.Button(win51, text="заново", bd=5, command=gdf).pack()

win52 = tk.Tk()
win52.geometry("500x500")
win52.title("Глава вторая - оборона замка Гингер.")

lbl = tk.Label(win52, text="Вы атакуете, но демон отбивает атаку.").pack()

fram35= tk.Frame(win52)

def dfgh(): 
  win52.destroy()
  win54.destroy()
  win55.destroy()

def dkghh(): 
  win55.destroy()
  win53.destroy()
  win52.destroy()

def hjfh(): 
  win52.destroy()
  win54.destroy()
  win53.destroy()

tk.Button(fram35,text="Ударить ещё раз", bd=5, command=dfgh).grid(column=1,row=1,columnspan=2,stick="wens",padx=5,pady=5)
tk.Button(fram35,text="Отступить", bd=5, command=dkghh).grid(column=1,row=2,columnspan=2,stick="wens",padx=5,pady=5)
tk.Button(fram35,text="Ударить с разворота", bd=5, command=hjfh).grid(column=1,row=3,columnspan=2,stick="wens",padx=5,pady=5)

fram35.pack()

win53 = tk.Tk()
win53.geometry("500x500")
win53.title("Глава вторая - оборона замка Гингер.")

lbl = tk.Label(win53, text="Вы его бьёте, но он вдруг исчезает и через секунду ").pack()
lbl = tk.Label(win53, text="появляеться у вас за спиной, вас убивают.").pack()

tk.Button(win53, text="заново", bd=5, command=gdf).pack()

win54 = tk.Tk()
win54.geometry("500x500")
win54.title("Глава вторая - оборона замка Гингер.")

lbl = tk.Label(win54, text="Вы пытаетесь отступить, но он вдруг исчезает и через секунду").pack()
lbl = tk.Label(win54, text="появляеться у вас за спиной, вас убили.").pack()

tk.Button(win54, text="заново", bd=5, command=gdf).pack()

win55 = tk.Tk()
win55.geometry("500x500")
win55.title("Глава вторая - оборона замка Гингер.")

lbl = tk.Label(win55, text="Вы начинаете поворачиваться и замечаете, что он исчезает ").pack()
lbl = tk.Label(win55, text="и чуствуете что попали по кому-то мечём ,поворачиваете ").pack()
lbl = tk.Label(win55, text="голову, и видете демона он телепортировался вам за ").pack()
lbl = tk.Label(win55, text="спину, но это была его ошибка, вы вонзили меч ему в шею.").pack()
lbl = tk.Label(win55, text="После этого вы видете того очистителя, который вас").pack()
lbl = tk.Label(win55, text="спас на блокпосте, он сражался с несколькимя демонами и").pack()
lbl = tk.Label(win55, text="к нему сзади приближался ещё один.").pack()

fram36= tk.Frame(win55)

def ghfg(): 
  win55.destroy()
  win57.destroy()

def dogj(): 
  win55.destroy()
  win56.destroy()

tk.Button(fram36,text="Попробывать пробить его доспех, в слабую зону около шеи", bd=5, command=dogj).grid(column=1,row=1,columnspan=2,stick="wens",padx=5,pady=5)
tk.Button(fram36,text="кинуть в него огненный шар", bd=5, command=ghfg).grid(column=1,row=2,columnspan=2,stick="wens",padx=5,pady=5)

fram36.pack()

win56 = tk.Tk()
win56.geometry("500x500")
win56.title("Глава вторая - оборона замка Гингер.")

lbl = tk.Label(win56, text="Вы кидаете в него огненный шар и он поварачивается на вас,").pack()
lbl = tk.Label(win56, text="и использует огненную спираль, убивая вас.").pack()

tk.Button(win56, text="заново", bd=5, command=gdf).pack()

win57 = tk.Tk()
win57.geometry("500x500")
win57.title("Глава вторая - оборона замка Гингер.")

lbl = tk.Label(win57, text="Вы бежите на него и попадаете мечем в шею.").pack()
lbl = tk.Label(win57, text="Очиститель закончил со своими.").pack()

fram37= tk.Frame(win57)

def fgdh(): 
  win57.destroy()
  win59.destroy()

def fdhgj(): 
  win58.destroy()
  win57.destroy()

tk.Button(fram37,text="Не ушибся, малыш?", bd=5, command=fgdh).grid(column=1,row=1,columnspan=2,stick="wens",padx=5,pady=5)
tk.Button(fram37,text="Как ты?", bd=5, command=fdhgj).grid(column=1,row=2,columnspan=2,stick="wens",padx=5,pady=5)

fram37.pack()

win58 = tk.Tk()
win58.geometry("500x500")
win58.title("Глава вторая - оборона замка Гингер.")

lbl = tk.Label(win58, text="О! Одобряю. Я Рэйн, тебя, как завут?").pack()
lbl = tk.Label(win58, text="Фубуки").pack()
lbl = tk.Label(win58, text="Рад знакомству. Ладно, Фу, пошли дальше чёртиков резать.").pack()
lbl = tk.Label(win58, text="Конечно.").pack()
lbl = tk.Label(win58, text="Так и сражалось наше войско, а под рассвет демоны ").pack()
lbl = tk.Label(win58, text="отступили, мы остались в Гингере до прихода ").pack()
lbl = tk.Label(win58, text="подкрепления, которое нас заменит.").pack()

win59 = tk.Tk()
win59.geometry("500x500")
win59.title("Глава вторая - оборона замка Гингер.")

lbl = tk.Label(win59, text="Нормально. Я Рэин, тебя, как завут?").pack()
lbl = tk.Label(win59, text="Фубуки").pack()
lbl = tk.Label(win59, text="Рад знакомству. Ладно, Ф, пошли дальше чёртиков рубить.").pack()
lbl = tk.Label(win59, text="Конечно.").pack()
lbl = tk.Label(win59, text="Так и сражалось наше войско, а под рассвет демоны ").pack()
lbl = tk.Label(win59, text="отступили, мы остались в Гингере до прихода ").pack()
lbl = tk.Label(win59, text="подкрепления, которое нас заменит.").pack()



win1.mainloop()

#После сражения у блокпоста нас осталось 257 человек. На половине пути к замку, мы попали в засаду демонов. Они были в плохих доспехах, поэтому мы их быстро разбили. Я даже убил одного такого, как это было: Я шел в конце армии и он на меня выпрыгнул, я шел с мечом в руках, и на реакции отрубил ему голову!
#Замок уже виднелся вдалеке, скоро уже рассвет, а это значит, что осада пройдет не удачно, демоны умирают от солнечных лучей . Я увидел как замок горит, в его стороне было огромное количество вспышек, от использования магии, смрад от трупов доносился аж до сюда(дистанция около 500 м). Осада шла полным ходом, но гарнизон очень хорошо держался. Я услышал: В атаку! На помощь замку! На осадный лагерь! 
#Все ринулись в бой. Я напал на одного из демонов, он сразу отпрыгнул и стал в блок.