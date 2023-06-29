import play
import pygame


pygame.mixer_music.load("hello-1.mp3")
pygame.mixer_music.play()

#загрузка звуков в список (пианино)
sounds = []
for i in range(1,9):
    s = pygame.mixer.Sound(str(i) + ".ogg")
    sounds.append(s)

#загрузка звуков в список (флейта)
sounds2 = []
for i in range(1,9):
    s = pygame.mixer.Sound("f" + str(i) + ".ogg")
    sounds2.append(s)

#загрузка звуков в список (гитара)
sounds3 = []
for i in range(1,9):
    s = pygame.mixer.Sound("g" + str(i) + ".ogg")
    sounds3.append(s)

#загрузка звуков в список (виоланчели)
sounds4 = []
for i in range(1,9):
    s = pygame.mixer.Sound("v" + str(i) + ".ogg")
    sounds4.append(s)


play.set_backdrop('violet')
play.new_text(words = "Это игра пианино!", x = 0, y = 200, color='green', font_size=60)

#создание кнопок
buttons = []
x1 = -265
for i in range(8):
    but = play.new_box(color= 'white', x=x1, y=0 , width=60, height=150, border_color='black', border_width=5)
    buttons.append(but)
    x1 += 75

#создаем две вспомагательные кнопки для запуска мелодии и для ее отчистки
but1 = play.new_box(color= 'white', x=-75, y=-170 , width=100, height=40, border_color='green', border_width=5)
but2 = play.new_box(color= 'white', x=75, y=-170 , width=100, height=40, border_color='red', border_width=5)
text1 = play.new_text(words = "Играть", x = -75, y = -170, color='green', font_size=30)
text2 = play.new_text(words = "Чистка", x = 75, y = -170, color='red', font_size=30)

circle1 = play.new_circle(color='black', x=-75, y=-120, radius=10)
circle_text = play.new_text(words = "Пианино", x = -75, y = -135, color='black', font_size=15)

circle2 = play.new_circle(color='black', x=0, y=-120, radius=10)
circle2_text = play.new_text(words = "Флейта", x = 0, y = -135, color='black', font_size=15)

circle3 = play.new_circle(color='black', x=75, y=-120, radius=10)
circle3_text = play.new_text(words = "Гитара", x = 75, y = -135, color='black', font_size=15)

circle4 = play.new_circle(color='black', x=150, y=-120, radius=10)
circle4_text = play.new_text(words = "Виоланчели", x = 150, y = -135, color='black', font_size=15)

melody = []
clear_melody_sound = pygame.mixer.Sound("clear_melody.wav")

state = 1 #1 - пианино, 2 - флейта, 3 - гитара, 4 - виоланчели

def check_state(state, k):
    if state == 1:
        sounds[k].play()
    if state == 2:
        sounds2[k].play()
    if state == 3:
        sounds3[k].play()
    if state == 4:
        sounds4[k].play()
    
@play.repeat_forever
async def do():
    global state
    k = 0 #счетчик для подсчета номера кнопки
    for i in buttons: #перебираем списков кнопок
        if i.is_clicked: #если кнопка была нажата
            check_state(state, k)
            i.color = 'yellow' #меням цвет кнопки на желтый
            melody.append(k) #добавляем в список номер кнопки
            print(melody) #временно выводим его в консоль, чтобы отладить и понаблюдать за работой проргаммы
            await play.timer(seconds=0.2) #делаем задержку в 0.2 секунды
            i.color = 'white' #меняем кнопку на белый цвет, который был изначально
        k += 1 #увеличиваем номер для кнопки
    
    if but1.is_clicked: #если нажата кнопка играть
        but1.color = 'blue' #делаем цвет кнопки - синий
        await play.timer(seconds=0.2) #ждем 0.2 секунды 
        but1.color = 'white' #обратно делаем - белый
        for i in melody: #пробегаемся циклом по списку мелодии
            check_state(state, i)
            await play.timer(seconds=0.3) #делаем задержку в 0.2 секунды

    if but2.is_clicked: #если 
        clear_melody_sound.play() #играю микрозвук нажатия на кнопку чистка
        but2.color = 'blue'
        await play.timer(seconds=0.2)
        but2.color = 'white'
        melody.clear() #чищу список мелодии
    
    if circle1.is_clicked:
        state = 1
        circle1.color = 'blue' #делаем цвет кнопки - синий
        await play.timer(seconds=0.2) #ждем 0.2 секунды 
        circle1.color = 'black' #обратно делаем - белый
    
    if circle2.is_clicked:
        state = 2
        circle2.color = 'blue' #делаем цвет кнопки - синий
        await play.timer(seconds=0.2) #ждем 0.2 секунды 
        circle2.color = 'black' #обратно делаем - белый

    if circle3.is_clicked:
        state = 3
        circle3.color = 'blue' #делаем цвет кнопки - синий
        await play.timer(seconds=0.2) #ждем 0.2 секунды 
        circle3.color = 'black' #обратно делаем - белый
    
    if circle4.is_clicked:
        state = 4
        circle4.color = 'blue' #делаем цвет кнопки - синий
        await play.timer(seconds=0.2) #ждем 0.2 секунды 
        circle4.color = 'black' #обратно делаем - белый

play.start_program()