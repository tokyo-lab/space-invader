import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# spaceship
spaceship_img = pygame.image.load("images/spaceship.png")
spaceship_x = 608
spaceship_y = 650
spaceship_x_change = 0


def spaceship(x, y):
    screen.blit(spaceship_img, (x, y))


# setup title and icon
icon = pygame.image.load("images/ufo.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Space Invaders")
while running:
    screen.fill((72, 60, 148))
    # spaceship_x += 0.1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                spaceship_x_change = -1.5
            if event.key == pygame.K_RIGHT:
                spaceship_x_change = 1.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                spaceship_x_change = 0

    spaceship_x += spaceship_x_change
    spaceship(spaceship_x, spaceship_y)

    pygame.display.update()