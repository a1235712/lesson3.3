import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра ТИР")
icon = pygame.image.load('image/cosmosT.jpg')
pygame.display.set_icon(icon)

target_img = pygame.image.load('image/target.png')
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
target_speed = 5  # Скорость движения цели по осям X и Y

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Начальное количество очков
score = 0

# Шрифт для отображения очков
font = pygame.font.Font(None, 36)

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                score += 10  # Добавление очков при попадании в цель

    # Движение цели
    target_x += random.randint(-1, 1) * target_speed
    target_y += random.randint(-1, 1) * target_speed

    # Проверка на выход за границы экрана
    if target_x < 0:
        target_x = 0
    elif target_x > SCREEN_WIDTH - target_width:
        target_x = SCREEN_WIDTH - target_width

    if target_y < 0:
        target_y = 0
    elif target_y > SCREEN_HEIGHT - target_height:
        target_y = SCREEN_HEIGHT - target_height

    screen.blit(target_img, (target_x, target_y))

    # Отрисовка очков
    text = font.render(f'Очки: {score}', True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.update()

pygame.quit()