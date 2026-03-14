import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Параметры экрана
WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Падение снежинок")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Класс снежинки
class Snowflake:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-HEIGHT, 0)  # начинаем выше экрана
        self.radius = random.randint(1, 4)
        self.speed = random.uniform(1, 3)    # скорость падения
        self.wind = random.uniform(-0.5, 0.5)  # горизонтальный дрейф

    def update(self):
        self.y += self.speed
        self.x += self.wind
        # если ушла за границы снизу – сбросить наверх
        if self.y > HEIGHT + self.radius:
            self.y = random.randint(-HEIGHT, -self.radius)
            self.x = random.randint(0, WIDTH)
            self.wind = random.uniform(-0.5, 0.5)

    def draw(self, surface):
        pygame.draw.circle(surface, WHITE, (int(self.x), int(self.y)), self.radius)

# Основная функция
def main():
    clock = pygame.time.Clock()
    snowflakes = []
    # Заполняем начальными снежинками
    for _ in range(200):
        snowflakes.append(Snowflake())

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Добавляем новые снежинки с небольшой вероятностью
        if random.random() < 0.005:  # 10% шанс за кадр
            snowflakes.append(Snowflake())

        # Обновление
        for flake in snowflakes:
            flake.update()

        # Отрисовка
        screen.fill(BLACK)
        for flake in snowflakes:
            flake.draw(screen)

        pygame.display.flip()
        clock.tick(120)  # 60 кадров в секунду

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()