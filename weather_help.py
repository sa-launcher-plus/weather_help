from tkinter import *
import pyowm, pygame, random, os

root = Tk()
root.geometry('600x450')
root.config(bg='lightgrey')
root.title('Weather help')
root.resizable(width=False, height=False)
root.iconbitmap('icon.ico')

owm = pyowm.OWM('f604f4c688b4fba2557a1916e6e06ee3', language='ru')

textStartMenu = Label(root, text='Weather help', fg='red', bg='lightgrey')
textStartMenu.config(font=('Obelix pro', 25))
textStartMenu.pack()

textStart = Label(root, text='Введите город:', fg='midnightblue', bg='lightgrey')
textStart.config(font=('Times', 17))
textStart.pack()

entry1 = Entry(root, width=65)
entry1.pack()

helloAudio = "hello2.mp3", "hello.mp3", "hello3.mp3", "hello4.mp3"

pygame.mixer.init()
pygame.mixer.music.load(random.choice(helloAudio))
pygame.mixer.music.play()

def url():
    pygame.mixer.init()
    pygame.mixer.music.load("url.mp3")
    pygame.mixer.music.play()
    
    os.startfile('webDocum.bat')

def tempInfo():
    entyInfo = entry1.get()
    observation = owm.weather_at_place(entyInfo)
    w = observation.get_weather()

    entyInfo = entry1.get()
    temp = w.get_temperature('celsius')["temp"]
    tempMax = w.get_temperature('celsius')["temp_max"]
    tempMin = w.get_temperature('celsius')["temp_min"]
    stStatus = w.get_detailed_status()
    wind = w.get_wind()['speed']

    textInfo1.config(text='Погода в городе ' + str(entyInfo) + ':')
    textStatus.config(text='В городе ' + str(entyInfo) + ' ' + str(stStatus))
    textWind.config(text='Скорость ветра в городе примерно ' + str(wind) + ' М/С')
    textTemp.config(text='Температура сейчас примерно ' + str(temp) + ' по Цельсию')
    textMax.config(text='Максимальная температура за сегодня ' + str(tempMax) + ' по Цельсию')
    textMin.config(text='Минимальная температура за сегодня ' + str(tempMin) + ' по Цельсию')

    if temp == 0:
        pygame.mixer.init()
        pygame.mixer.music.load("temp 0.mp3")
        pygame.mixer.music.play()
        
        window1 = Tk()
        window1.geometry('400x300')
        window1.config(bg='lightgrey')
        window1.title('Советы от Weather help')
        window1.resizable(width=False, height=False)

        textStartMenu = Label(window1, text='Weather help', fg='red', bg='lightgrey')
        textStartMenu.config(font=('Obelix pro', 25))
        textStartMenu.pack()

        lab = Label(window1, text='''Привет, я тебе посоветую,
        что надеть для похода на улицу...
        А именно на улицу города, который ты ввёл!
                
        0 градусов по цельсию.
        В такую температуру тает лёд,
        но всё равно холодно! :-)
        Одевай тйплые вещи!''', fg='black', bg='lightgrey')
        lab.config(font=('HACKED', 13))
        lab.pack()
            
        window1.mainloop()

    elif temp < -30:
        pygame.mixer.init()
        pygame.mixer.music.load("temp -30.mp3")
        pygame.mixer.music.play()
        
        window1 = Tk()
        window1.geometry('400x300')
        window1.config(bg='lightgrey')
        window1.title('Советы от Weather help')
        window1.resizable(width=False, height=False)

        textStartMenu = Label(window1, text='Weather help', fg='red', bg='lightgrey')
        textStartMenu.config(font=('Obelix pro', 25))
        textStartMenu.pack()

        lab = Label(window1, text='''Привет, я тебе посоветую,
        что одеть для похода на улицу...
        А именно на улицу города, который ты ввёл!
               
        На улице менее -30 по Цельсию!!!
        Обычно в такую погоду даже в школу не ходят!
        Но раз пошёл, одевайся теплее...)
        Шарф, зимняя куртка, шапка и т.д.)))''', fg='black', bg='lightgrey')
        lab.config(font=('HACKED', 13))
        lab.pack()

        window1.mainloop()

    elif temp < -20:
        pygame.mixer.init()
        pygame.mixer.music.load("temp -20.mp3")
        pygame.mixer.music.play()
        
        window1 = Tk()
        window1.geometry('400x300')
        window1.config(bg='lightgrey')
        window1.title('Советы от Weather help')
        window1.resizable(width=False, height=False)

        textStartMenu = Label(window1, text='Weather help', fg='red', bg='lightgrey')
        textStartMenu.config(font=('Obelix pro', 25))
        textStartMenu.pack()

        lab = Label(window1, text='''Привет, я тебе посоветую,
        что одеть для похода на улицу...
        А именно на улицу города, который ты ввёл!
                
        Температура менее -20 по Цельсию...
        Оденься теплее!) И шарф не забудь!
        Всё таки зима на дворе)))''', fg='black', bg='lightgrey')
        lab.config(font=('HACKED', 13))
        lab.pack()

        window1.mainloop()

    elif temp < -10:
        pygame.mixer.init()
        pygame.mixer.music.load("temp -10.mp3")
        pygame.mixer.music.play()
        
        window1 = Tk()
        window1.geometry('400x300')
        window1.config(bg='lightgrey')
        window1.title('Советы от Weather help')
        window1.resizable(width=False, height=False)

        textStartMenu = Label(window1, text='Weather help', fg='red', bg='lightgrey')
        textStartMenu.config(font=('Obelix pro', 25))
        textStartMenu.pack()

        lab = Label(window1, text='''Привет, я тебе посоветую,
        что одеть для похода на улицу...
        А именно на улицу города, который ты ввёл!
                
        Холодно-холодно на улице!
        Менее -10 по Цельсию...
        Одевайся по-теплее)''', fg='black', bg='lightgrey')
        lab.config(font=('HACKED', 13))
        lab.pack()

        window1.mainloop()

    elif temp < 0:
        pygame.mixer.init()
        pygame.mixer.music.load("temp -0.mp3")
        pygame.mixer.music.play()
        
        window1 = Tk()
        window1.geometry('400x300')
        window1.config(bg='lightgrey')
        window1.title('Советы от Weather help')
        window1.resizable(width=False, height=False)

        textStartMenu = Label(window1, text='Weather help', fg='red', bg='lightgrey')
        textStartMenu.config(font=('Obelix pro', 25))
        textStartMenu.pack()

        lab = Label(window1, text='''Привет, я тебе посоветую,
        что одеть для похода на улицу...
        А именно на улицу города, который ты ввёл!
                
        Холодновато на улице, дружище...
        Ниже нуля градусов по Цельсию...
        Одевайся теплее.
        Кажется зима там ;-)''', fg='black', bg='lightgrey')
        lab.config(font=('HACKED', 13))
        lab.pack()

        window1.mainloop()

    elif temp < 10:
        pygame.mixer.init()
        pygame.mixer.music.load("temp 10.mp3")
        pygame.mixer.music.play()
        
        window1 = Tk()
        window1.geometry('400x300')
        window1.config(bg='lightgrey')
        window1.title('Советы от Weather help')
        window1.resizable(width=False, height=False)

        textStartMenu = Label(window1, text='Weather help', fg='red', bg='lightgrey')
        textStartMenu.config(font=('Obelix pro', 25))
        textStartMenu.pack()

        lab = Label(window1, text='''Привет, я тебе посоветую,
        что одеть для похода на улицу...
        А именно на улицу города, который ты ввёл!
                
        Весна? Осень? Погода точно...
        не летняя! Ниже 10 градусов по Цельсию!
        Одевай кофту и ей подобные вещи ;-)''', fg='black', bg='lightgrey')
        lab.config(font=('HACKED', 13))
        lab.pack()

        window1.mainloop()

    elif temp < 20:
        pygame.mixer.init()
        pygame.mixer.music.load("temp 20.mp3")
        pygame.mixer.music.play()
        
        window1 = Tk()
        window1.geometry('400x300')
        window1.config(bg='lightgrey')
        window1.title('Советы от Weather help')
        window1.resizable(width=False, height=False)

        textStartMenu = Label(window1, text='Weather help', fg='red', bg='lightgrey')
        textStartMenu.config(font=('Obelix pro', 25))
        textStartMenu.pack()

        lab = Label(window1, text='''Привет, я тебе посоветую,
        что надеть для похода на улицу...
        А именно на улицу города, который ты ввёл!
                
        Температура ниже 20 градусов.
        Тут на свой выбор, но скажу одно...
        Температура не тёплая/жаркая :-/''', fg='black', bg='lightgrey')
        lab.config(font=('HACKED', 13))
        lab.pack()
            
        window1.mainloop()
    
    elif temp < 30:
        pygame.mixer.init()
        pygame.mixer.music.load("temp 30.mp3")
        pygame.mixer.music.play()
              
        window1 = Tk()
        window1.geometry('400x300')
        window1.config(bg='lightgrey')
        window1.title('Советы от Weather help')
        window1.resizable(width=False, height=False)

        textStartMenu = Label(window1, text='Weather help', fg='red', bg='lightgrey')
        textStartMenu.config(font=('Obelix pro', 25))
        textStartMenu.pack()

        lab = Label(window1, text='''Привет, я тебе посоветую,
        что надеть для похода на улицу...
        А именно на улицу города, который ты ввёл!
                
        Тепло-тепло! Выше 20 градусов)
        Одевай что хочешь)
        Болеть не будешь, уверяю ;-)''', fg='black', bg='lightgrey')
        lab.config(font=('HACKED', 13))
        lab.pack()

        window1.mainloop()

    elif temp >= 30:
        pygame.mixer.init()
        pygame.mixer.music.load("temp +30.mp3")
        pygame.mixer.music.play()
               
        window1 = Tk()
        window1.geometry('400x300')
        window1.config(bg='lightgrey')
        window1.title('Советы от Weather help')
        window1.resizable(width=False, height=False)

        textStartMenu = Label(window1, text='Weather help', fg='red', bg='lightgrey')
        textStartMenu.config(font=('Obelix pro', 25))
        textStartMenu.pack()

        lab = Label(window1, text='''Привет, я тебе посоветую,
        что одеть для похода на улицу...
        А именно на улицу города, который ты ввёл!
                
        Погода супер!!!)
        Руки в ноги и вперёд на пляж!
        Только конечно, если дождя нет :-)''', fg='black', bg='lightgrey')
        lab.config(font=('HACKED', 13))
        lab.pack()

        window1.mainloop()

    elif temp >= 40:
        pygame.mixer.init()
        pygame.mixer.music.load("temp 40.mp3")
        pygame.mixer.music.play()
                 
        window1 = Tk()
        window1.geometry('400x300')
        window1.config(bg='lightgrey')
        window1.title('Советы от Weather help')
        window1.resizable(width=False, height=False)

        textStartMenu = Label(window1, text='Weather help', fg='red', bg='lightgrey')
        textStartMenu.config(font=('Obelix pro', 25))
        textStartMenu.pack()

        lab = Label(window1, text='''Привет, я тебе посоветую,
        что одеть для похода на улицу...
        А именно на улицу города, который ты ввёл!
                
        Оххх... Ну и жара!
        В одном купальнике ходить)
        Шучу... Иди в чём хочешь ;-)''', fg='black', bg='lightgrey')
        lab.config(font=('Times', 13))
        lab.pack()       

        window1.mainloop()

def tempInfoCity():
    f = open('city.txt', 'r', -1, 'utf-8')
    city = f.readline()
    f.close()
    
    entyInfo = entry1.get()
    observation = owm.weather_at_place(city)
    w = observation.get_weather()

    entyInfo = entry1.get()
    temp = w.get_temperature('celsius')["temp"]
    tempMax = w.get_temperature('celsius')["temp_max"]
    tempMin = w.get_temperature('celsius')["temp_min"]
    stStatus = w.get_detailed_status()
    wind = w.get_wind()['speed']

    textInfo1.config(text='Погода в городе ' + str(city) + ':')
    textStatus.config(text='В городе ' + str(entyInfo) + ' ' + str(stStatus))
    textWind.config(text='Скорость ветра в городе примерно ' + str(wind) + ' М/С')
    textTemp.config(text='Температура сейчас примерно ' + str(temp) + ' по Цельсию')
    textMax.config(text='Максимальная температура за сегодня ' + str(tempMax) + ' по Цельсию')
    textMin.config(text='Минимальная температура за сегодня ' + str(tempMin) + ' по Цельсию')

    if temp == 0:
        pygame.mixer.init()
        pygame.mixer.music.load("temp 0.mp3")
        pygame.mixer.music.play()
        
        window1 = Tk()
        window1.geometry('400x300')
        window1.config(bg='lightgrey')
        window1.title('Советы от Weather help')
        window1.resizable(width=False, height=False)

        textStartMenu = Label(window1, text='Weather help', fg='red', bg='lightgrey')
        textStartMenu.config(font=('Obelix pro', 25))
        textStartMenu.pack()

        lab = Label(window1, text='''Привет, я тебе посоветую,
        что надеть для похода на улицу...
        А именно на улицу города, который ты ввёл!
                
        0 градусов по цельсию.
        В такую температуру тает лёд,
        но всё равно холодно! :-)
        Одевай тйплые вещи!''', fg='black', bg='lightgrey')
        lab.config(font=('HACKED', 13))
        lab.pack()
            
        window1.mainloop()

    elif temp < -30:
        pygame.mixer.init()
        pygame.mixer.music.load("temp -30.mp3")
        pygame.mixer.music.play()
        
        window1 = Tk()
        window1.geometry('400x300')
        window1.config(bg='lightgrey')
        window1.title('Советы от Weather help')
        window1.resizable(width=False, height=False)

        textStartMenu = Label(window1, text='Weather help', fg='red', bg='lightgrey')
        textStartMenu.config(font=('Obelix pro', 25))
        textStartMenu.pack()

        lab = Label(window1, text='''Привет, я тебе посоветую,
        что одеть для похода на улицу...
        А именно на улицу города, который ты ввёл!
               
        На улице менее -30 по Цельсию!!!
        Обычно в такую погоду даже в школу не ходят!
        Но раз пошёл, одевайся теплее...)
        Шарф, зимняя куртка, шапка и т.д.)))''', fg='black', bg='lightgrey')
        lab.config(font=('HACKED', 13))
        lab.pack()

        window1.mainloop()

    elif temp < -20:
        pygame.mixer.init()
        pygame.mixer.music.load("temp -20.mp3")
        pygame.mixer.music.play()
        
        window1 = Tk()
        window1.geometry('400x300')
        window1.config(bg='lightgrey')
        window1.title('Советы от Weather help')
        window1.resizable(width=False, height=False)

        textStartMenu = Label(window1, text='Weather help', fg='red', bg='lightgrey')
        textStartMenu.config(font=('Obelix pro', 25))
        textStartMenu.pack()

        lab = Label(window1, text='''Привет, я тебе посоветую,
        что одеть для похода на улицу...
        А именно на улицу города, который ты ввёл!
                
        Температура менее -20 по Цельсию...
        Оденься теплее!) И шарф не забудь!
        Всё таки зима на дворе)))''', fg='black', bg='lightgrey')
        lab.config(font=('HACKED', 13))
        lab.pack()

        window1.mainloop()

    elif temp < -10:
        pygame.mixer.init()
        pygame.mixer.music.load("temp -10.mp3")
        pygame.mixer.music.play()
        
        window1 = Tk()
        window1.geometry('400x300')
        window1.config(bg='lightgrey')
        window1.title('Советы от Weather help')
        window1.resizable(width=False, height=False)

        textStartMenu = Label(window1, text='Weather help', fg='red', bg='lightgrey')
        textStartMenu.config(font=('Obelix pro', 25))
        textStartMenu.pack()

        lab = Label(window1, text='''Привет, я тебе посоветую,
        что одеть для похода на улицу...
        А именно на улицу города, который ты ввёл!
                
        Холодно-холодно на улице!
        Менее -10 по Цельсию...
        Одевайся по-теплее)''', fg='black', bg='lightgrey')
        lab.config(font=('HACKED', 13))
        lab.pack()

        window1.mainloop()

    elif temp < 0:
        pygame.mixer.init()
        pygame.mixer.music.load("temp -0.mp3")
        pygame.mixer.music.play()
        
        window1 = Tk()
        window1.geometry('400x300')
        window1.config(bg='lightgrey')
        window1.title('Советы от Weather help')
        window1.resizable(width=False, height=False)

        textStartMenu = Label(window1, text='Weather help', fg='red', bg='lightgrey')
        textStartMenu.config(font=('Obelix pro', 25))
        textStartMenu.pack()

        lab = Label(window1, text='''Привет, я тебе посоветую,
        что одеть для похода на улицу...
        А именно на улицу города, который ты ввёл!
                
        Холодновато на улице, дружище...
        Ниже нуля градусов по Цельсию...
        Одевайся теплее.
        Кажется зима там ;-)''', fg='black', bg='lightgrey')
        lab.config(font=('HACKED', 13))
        lab.pack()

        window1.mainloop()

    elif temp < 10:
        pygame.mixer.init()
        pygame.mixer.music.load("temp 10.mp3")
        pygame.mixer.music.play()
        
        window1 = Tk()
        window1.geometry('400x300')
        window1.config(bg='lightgrey')
        window1.title('Советы от Weather help')
        window1.resizable(width=False, height=False)

        textStartMenu = Label(window1, text='Weather help', fg='red', bg='lightgrey')
        textStartMenu.config(font=('Obelix pro', 25))
        textStartMenu.pack()

        lab = Label(window1, text='''Привет, я тебе посоветую,
        что одеть для похода на улицу...
        А именно на улицу города, который ты ввёл!
                
        Весна? Осень? Погода точно...
        не летняя! Ниже 10 градусов по Цельсию!
        Одевай кофту и ей подобные вещи ;-)''', fg='black', bg='lightgrey')
        lab.config(font=('HACKED', 13))
        lab.pack()

        window1.mainloop()

    elif temp < 20:
        pygame.mixer.init()
        pygame.mixer.music.load("temp 20.mp3")
        pygame.mixer.music.play()
        
        window1 = Tk()
        window1.geometry('400x300')
        window1.config(bg='lightgrey')
        window1.title('Советы от Weather help')
        window1.resizable(width=False, height=False)

        textStartMenu = Label(window1, text='Weather help', fg='red', bg='lightgrey')
        textStartMenu.config(font=('Obelix pro', 25))
        textStartMenu.pack()

        lab = Label(window1, text='''Привет, я тебе посоветую,
        что надеть для похода на улицу...
        А именно на улицу города, который ты ввёл!
                
        Температура ниже 20 градусов.
        Тут на свой выбор, но скажу одно...
        Температура не тёплая/жаркая :-/''', fg='black', bg='lightgrey')
        lab.config(font=('HACKED', 13))
        lab.pack()
            
        window1.mainloop()
    
    elif temp < 30:
        pygame.mixer.init()
        pygame.mixer.music.load("temp 30.mp3")
        pygame.mixer.music.play()
              
        window1 = Tk()
        window1.geometry('400x300')
        window1.config(bg='lightgrey')
        window1.title('Советы от Weather help')
        window1.resizable(width=False, height=False)

        textStartMenu = Label(window1, text='Weather help', fg='red', bg='lightgrey')
        textStartMenu.config(font=('Obelix pro', 25))
        textStartMenu.pack()

        lab = Label(window1, text='''Привет, я тебе посоветую,
        что надеть для похода на улицу...
        А именно на улицу города, который ты ввёл!
                
        Тепло-тепло! Выше 20 градусов)
        Одевай что хочешь)
        Болеть не будешь, уверяю ;-)''', fg='black', bg='lightgrey')
        lab.config(font=('HACKED', 13))
        lab.pack()

        window1.mainloop()

    elif temp >= 30:
        pygame.mixer.init()
        pygame.mixer.music.load("temp +30.mp3")
        pygame.mixer.music.play()
               
        window1 = Tk()
        window1.geometry('400x300')
        window1.config(bg='lightgrey')
        window1.title('Советы от Weather help')
        window1.resizable(width=False, height=False)

        textStartMenu = Label(window1, text='Weather help', fg='red', bg='lightgrey')
        textStartMenu.config(font=('Obelix pro', 25))
        textStartMenu.pack()

        lab = Label(window1, text='''Привет, я тебе посоветую,
        что одеть для похода на улицу...
        А именно на улицу города, который ты ввёл!
                
        Погода супер!!!)
        Руки в ноги и вперёд на пляж!
        Только конечно, если дождя нет :-)''', fg='black', bg='lightgrey')
        lab.config(font=('HACKED', 13))
        lab.pack()

        window1.mainloop()

    elif temp >= 40:
        pygame.mixer.init()
        pygame.mixer.music.load("temp 40.mp3")
        pygame.mixer.music.play()
                 
        window1 = Tk()
        window1.geometry('400x300')
        window1.config(bg='lightgrey')
        window1.title('Советы от Weather help')
        window1.resizable(width=False, height=False)

        textStartMenu = Label(window1, text='Weather help', fg='red', bg='lightgrey')
        textStartMenu.config(font=('Obelix pro', 25))
        textStartMenu.pack()

        lab = Label(window1, text='''Привет, я тебе посоветую,
        что одеть для похода на улицу...
        А именно на улицу города, который ты ввёл!
                
        Оххх... Ну и жара!
        В одном купальнике ходить)
        Шучу... Иди в чём хочешь ;-)''', fg='black', bg='lightgrey')
        lab.config(font=('Times', 13))
        lab.pack()       

        window1.mainloop()

def infoBut():
    infoAudio = "info.mp3", "info2.mp3"
    
    pygame.mixer.init()
    pygame.mixer.music.load(random.choice(infoAudio))
    pygame.mixer.music.play()
    
    winInfo = Tk()
    winInfo.geometry('400x650')
    winInfo.config(bg='lightgrey')
    winInfo.title('Доп.Информация о Weather help')
    winInfo.resizable(width=False, height=False)

    textStartMenu = Label(winInfo, text='Weather help', fg='red', bg='lightgrey')
    textStartMenu.config(font=('Obelix pro', 25))
    textStartMenu.pack()

    textInf = Label(winInfo, text='Дополнительная информация о приложении:', fg='dimgray', bg='lightgrey')
    textInf.config(font=('Times', 14))
    textInf.pack()

    textInf2 = Label(winInfo, text='''Версия приложения: V5.2-FULL_2020
    Разработчик: Кибердружина НСО
    Программист(ы): Матвей Воронцов
    Язык программирования: Python версии 3
    Доп.Модули языка: Tkinter, pyowm
    Что нового: Описано в
    установщике/setup файле
    Информация о погоде: API key взят
    с OpenWeatherMap...
    вся информация о погоде
    ими же и предостовляются

    !!!ВАЖНО!!!
    Если вы ввели город и нажали
    кнопку "Посмотреть",...
    но ничего нет :/... Это из-за того,
    что вы не правильно ввели название или
    приложение не смогло найти
    в базе данных город!
    Также возможно, что вы не подключены
    к сети/WI-FI/интернету!''', fg='black', bg='lightgrey')
    textInf2.config(font=('Times', 14))
    textInf2.pack()

    textInf3 = Label(winInfo, text='''За помощью обращайтесь:
    - E-mail: kiberdruzina.nso@ya.ru''', fg='darkblue', bg='white')
    textInf3.config(font=('Times', 13))
    textInf3.pack()
    
    buttonURL_Docum = Button(winInfo, text='Документация')
    buttonURL_Docum.config(width=25, height=2, fg='black', bg='lightgrey', command=url)
    buttonURL_Docum.pack()

    winInfo.mainloop()

def docum():
    pygame.mixer.init()
    pygame.mixer.music.load("docum.mp3")
    pygame.mixer.music.play()

def stopAudio():
    pygame.mixer.init()
    pygame.mixer.music.load("stopAudio.mp3")
    pygame.mixer.music.play()

def writE():
    f = open('city.txt', 'w', -1, 'utf-8')
    f.write(entry1.get())
    f.close()
        
textPs = Label(root, text='''P.S. Убедитесь что все символы написаны правильно
и что ваш компьютер подключен к сети/интернету/WI-FI!
(Примеры: Москва, Екатеринбург, London, Dubai)''', fg='grey', bg='lightgrey')
textPs.config(font=('Times', 15))
textPs.pack()

butWeather = Button(root, text='Посмотреть погоду')
butWeather.config(width=25, height=2, fg='black', bg='whitesmoke', command=tempInfo)
butWeather.place(x=100, y=358)

textCity = '''Посмотреть погоду в
городе из избранного'''

butCity = Button(root, text=textCity)
butCity.config(width=25, height=2, fg='black', bg='whitesmoke', command=tempInfoCity)
butCity.place(x=320, y=358)

textInfo1 = Label(root, text='Сначала введите город!', fg='midnightblue', bg='lightgrey')
textInfo1.config(font=('Times', 20))
textInfo1.pack()

textStatus = Label(root, fg='red', bg='lightgrey')
textStatus.config(font=('Times', 16))
textStatus.pack()

textWind = Label(root, fg='orangered', bg='lightgrey')
textWind.config(font=('Times', 16))
textWind.pack()

textTemp = Label(root, fg='red', bg='lightgrey')
textTemp.config(font=('Times', 16))
textTemp.pack()

textMax = Label(root, fg='black', bg='lightgrey')
textMax.config(font=('Times', 16))
textMax.pack()

textMin = Label(root, fg='black', bg='lightgrey')
textMin.config(font=('Times', 16))
textMin.pack()

butInfo = Button(root, text='Доп.Информация')
butInfo.config(width=25, height=2, fg='black', bg='lightgrey', command=infoBut)
butInfo.place(x=0, y=409)

butDocum = Button(root, text='Инструкция')
butDocum.config(width=25, height=1, fg='black', bg='lightgrey', command=docum)
butDocum.place(x=207.5, y=424)

butWrite = Button(root, text='Добавить город в избранное')
butWrite.config(width=25, height=1, fg='black', bg='lightgrey', command=writE)
butWrite.place(x=207.5, y=400)

butStopAudio = Button(root, text='Стоп аудио')
butStopAudio.config(width=25, height=2, fg='black', bg='lightgrey', command=stopAudio)
butStopAudio.place(x=415, y=409)

root.mainloop()