import pygame

black = (0,0,0)
white = (255,255,255)

pygame.init()

surfaceWidth = 800
surfaceHeight = 500

surface = pygame.display.set_mode((surfaceWidth,surfaceHeight))
pygame.display.set_caption("Helicopter")
clock = pygame.time.Clock()

img = pygame.image.load("Docs/Helicopter.png")
x = 150
y = 200

y_move = 0

def msgSurface(text):
    

def gameOver():
    msgSurface("Kaboom!")

def helicopter(x, y, image):
    surface.blit(img, (x,y))

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_move = -5
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                y_move = 5

    y += y_move
    
    surface.fill(black)
    helicopter(x,y,img)

    if y > surfaceHeight-40 or y < 0:
        gameOver()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()