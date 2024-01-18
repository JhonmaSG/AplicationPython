#Shooter Galaga for python
import pygame, random

#Clases
class Player(pygame.sprite.Sprite):
    def __init__(self):
        #Superclase
        super().__init__()
        self.image = pygame.image.load(r'C:\Users\Jhon\Documents\Visual Studio Code\Python\AplicationPython\Shooter\player.png').convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
    #Mover el Jugador
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        player.rect.x = mouse_pos[0] - 50
        player.rect.y = 510 #Coordenada fija, Vertical

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        #Superclase
        super().__init__()
        self.image = pygame.image.load(r'C:\Users\Jhon\Documents\Visual Studio Code\Python\AplicationPython\Shooter\meteor.png').convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

class Laser(pygame.sprite.Sprite):
    def __init__(self):
        #Superclase
        super().__init__()
        self.image = pygame.image.load(r'C:\Users\Jhon\Documents\Visual Studio Code\Python\AplicationPython\Shooter\laser.png').convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        # Velocidad del laser: lento 1 - rapido > 5
        self.rect.y -= 5

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
pygame.init()
screen = pygame.display.set_mode([900, 600])
clock = pygame.time.Clock()
done = False
max_score = 20
score = 0



    screen.fill(WHITE)
    all_sprite_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()