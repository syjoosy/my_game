import pygame
import time

pygame.init()
#win = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
win = pygame.display.set_mode((700,500)) #размеры окна
pygame.display.set_caption("Просто программирую") # имя окна
gameWork = True
clock = pygame.time.Clock()
walkLeft = [pygame.transform.scale(pygame.image.load('Enemy_Sprites/robotturn.png'),(320,320)),
pygame.transform.scale(pygame.image.load('Enemy_Sprites/robot_stand_reverse.png'),(320,320)),
pygame.transform.scale(pygame.image.load('Enemy_Sprites/robotland_reverse.png'),(320,320)),
pygame.transform.scale(pygame.image.load('Enemy_Sprites/robothover1_reverse.png'),(320,320)),
pygame.transform.scale(pygame.image.load('Enemy_Sprites/robothover2_reverse.png'),(320,320))]  # Все картинки хождения влево
walkRight = [pygame.transform.scale(pygame.image.load('Enemy_Sprites/robot_turn_reverse.png'),(320,320)),
pygame.transform.scale(pygame.image.load('Enemy_Sprites/robotstand.png'),(320,320)),
pygame.transform.scale(pygame.image.load('Enemy_Sprites/robotland.png'),(320,320)),
pygame.transform.scale(pygame.image.load('Enemy_Sprites/robothover1.png'),(320,320)),
pygame.transform.scale(pygame.image.load('Enemy_Sprites/robothover2.png'),(320,320))] # Все картинки хождения вправо
#robot = pygame.image.load('Enemy_Sprites/robotstand.png')
background = pygame.image.load('PA_BG/PNG/War3/Bright/War3.png') # задний фон
background = pygame.transform.scale(background, (1750, 1000)) # изменяем размеры заднего фона


x = 50 # Начальный х положения героя
y = 150 # Начальный у положения героя
#y = 710 # При фулл хд робот стоит на земле

speed = 5 # скорость перемещения героя
left = False # Поворачивает налево?
right = False # Поворачивает направо?
lastmove = "right" # Последний поворот героя
animCount = 0 # Номер анимации
ifleft = 0 # 2 переменные, для
ifright = 0 #                  красивого поворота робота

def drawWindow():
    global animCount
    win.blit(background,(0,0)) #рисуем задний фон

    if animCount + 1 >= 25: # Список анимаций
        animCount = 0       #

    if left == True: # Если повернул налево
        global ifleft
        global ifright
        global y
        if ifleft == 0: # Для единоразового отображения
            win.blit(walkLeft[0],(x,y)) # анимации
            ifleft = 1 # поворота
        win.blit(walkLeft[animCount // 5],(x,y)) # перебор всех анимаций

        if animCount == 2: # имитация
            for i in range(50): # прыжка
                y -=2 # при взлете

        if animCount == 20:
            win.blit(walkLeft[4],(x,y)) # остановка на анимации полета
        else:
            animCount +=1
    elif right == True:
        if ifright == 0: # Для единоразового отображения
            win.blit(walkRight[0],(x,y)) # анимации
            ifright = 1 # поворота
        win.blit(walkRight[animCount // 5],(x,y)) # перебор всех анимаций

        if animCount == 2: # имитация
            for i in range(50): # прыжка
                y -=2 # при взлете

        if animCount == 20:
            win.blit(walkRight[4],(x,y)) # остановка на анимации полета
        else:
            animCount +=1

    else:
        #if lastmove == 'left':                                    #Рисует героя, даже если ничего не делать
        #    win.blit(walkLeft[animCount // 5],(x,y))              #
        #    animCount +=1                                         #
        #elif lastmove == 'right':                                 #
        #    win.blit(walkRight[animCount // 5],(x,y))             #
        #    animCount +=1                                         #
        win.blit(walkLeft[4],(x,y))
        pass
    pygame.display.update() # Обновляет экран


while gameWork == True: # Главный цикл
    clock.tick(60) # устанавливаем 60 fps

    for event in pygame.event.get(): # При нажатии на крестик
        if event.type == pygame.QUIT: # все закрывается
            gameWork = False # иначе только через
            pygame.Quit() # диспетчер задач

    keys = pygame.key.get_pressed() # проверяем нажатия клавиш
    if keys[pygame.K_ESCAPE]: # При нажатии ESC
        pygame.Quit() # выходим из программы
    if keys[pygame.K_LEFT]: # стрелочка влево
        x -= speed # отнимаем от х нашу скорость
        left = True
        right = False
        lastmove = "left"
    elif keys[pygame.K_RIGHT]: # стрелочка вправо
        x += speed # прибавляем к х нашу скорость
        left = False
        right = True
        lastmove = "right"
    elif keys[pygame.K_UP]: # стрелочка вверх
        y -= speed # отнимаем от у нашу скорость
        left = False
        right = False
    elif keys[pygame.K_DOWN]: # стрелочка вниз
        y += speed # прибавляем к у нашу скорость
        left = False
        right = False

    else:
        left = False # Если ничего не нажимаем
        right = False #
        animCount = 0 #
    drawWindow() # вызов функции drawWindow


pygame.Quit() # Если мы вне главного цикла, то выходим из игры
