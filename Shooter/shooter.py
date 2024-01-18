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


#Lista de Sprites, deteccion
all_sprite_list = pygame.sprite.Group()
meteor_list = pygame.sprite.Group()
laser_list = pygame.sprite.Group()

# # meteor
for i in range(max_score):
    meteor = Meteor()
    meteor.rect.x = random.randrange(880)
    meteor.rect.y = random.randrange(450)

    # Agregar a List_sprite
    meteor_list.add(meteor)
    all_sprite_list.add(meteor)
#Creacion instancia
player = Player()
all_sprite_list.add(player)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # pos del laser
        if event.type == pygame.MOUSEBUTTONDOWN:
            laser = Laser()
            # pos de la nave + 45 px : center
            laser.rect.x = player.rect.x + 45
            laser.rect.y = player.rect.y - 40

            all_sprite_list.add(laser)
            laser_list.add(laser)
            
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
                print('Has Ganado')
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