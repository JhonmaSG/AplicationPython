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
        self.speed_x = 0
        self.speed_y = 0
    
    #Mover el Jugador
    def changespeed(self, x):
        self.speed_x += x
    
    def update(self):
        #mouse_pos = pygame.mouse.get_pos()
        self.rect.x += self.speed_x
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
        self.rect.y -= 4

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()
done = False
max_score = 20
score = 0
game_over = False

#Lista de Sprites, deteccion
all_sprite_list = pygame.sprite.Group()
meteor_list = pygame.sprite.Group()
laser_list = pygame.sprite.Group()

# # meteor
for i in range(max_score):
    meteor = Meteor()
    meteor.rect.x = random.randrange(SCREEN_WIDTH - 50)
    meteor.rect.y = random.randrange(SCREEN_HEIGHT - 150)

    # Agregar a List_sprite
    meteor_list.add(meteor)
    all_sprite_list.add(meteor)

#Creacion instancia
player = Player()
all_sprite_list.add(player)

#Implements sound and keys
#load sound : .ogg .wav .....
sound = pygame.mixer.Sound(r'C:\Users\Jhon\Documents\Visual Studio Code\Python\AplicationPython\Shooter\laser5.ogg')

#########################

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # Logic Sound
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3)
            if event.key == pygame.K_RIGHT:
                player.changespeed(3)
            if event.key == pygame.K_SPACE:
                laser = Laser()
                # pos de la nave + 45 px : center
                laser.rect.x = player.rect.x + 45
                laser.rect.y = player.rect.y - 40

                laser_list.add(laser)
                all_sprite_list.add(laser)
                sound.play()
            
        #Logic Controller keyboard Arrows left and right
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3)
            if event.key == pygame.K_RIGHT:
                player.changespeed(-3)
            
    # Orden Estricto: update, fill and sprite
    all_sprite_list.update()

    # Colisiones: iterar en la lista de los laseres
    for laser in laser_list:
        # "Condicion" (laser y la lista de meteoro)
        meteor_hit_list = pygame.sprite.spritecollide(laser, meteor_list, True)
        for meteor in meteor_hit_list:
            all_sprite_list.remove(laser)
            laser_list.remove(laser)
            score += 1
            print(score)
            if score >= max_score:
                print('Has Salvado al mundo')
                pygame.quit()
        # Liberacion de recursos de la maquina (laser al rebasar el limite de la screen)
        if laser.rect.y < -10 :
            all_sprite_list.remove(laser)
            laser_list.remove(laser)

    screen.fill(WHITE)
    all_sprite_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()