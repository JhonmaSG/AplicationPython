#Shooter Galaga for python
#JhonmaSG
import pygame, random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

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
        self.rect.y = 510 #Coordenada fija, Vertical
    

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

#Class Game
class Game(object):

    def __init__(self, max_score, SCREEN_WIDTH, SCREEN_HEIGHT):
        
        self.score = 0

        self.all_sprite_list = pygame.sprite.Group()
        self.meteor_list = pygame.sprite.Group()
        self.laser_list = pygame.sprite.Group()

        # # meteor
        for i in range(max_score):
            meteor = Meteor()
            meteor.rect.x = random.randrange(SCREEN_WIDTH - 50)
            meteor.rect.y = random.randrange(SCREEN_HEIGHT - 150)

            # Agregar a List_sprite
            self.meteor_list.add(meteor)
            self.all_sprite_list.add(meteor)

        #Creacion instancia
        self.player = Player()
        self.all_sprite_list.add(self.player)
    
    #Process_Events
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("EXIT SUCCESS")
                return True
        return False
    
    #Run_logic
    def run_logic(self, sound, max_score):
        for event in pygame.event.get():
            if event.key == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.changespeed(-3)
                if event.key == pygame.K_RIGHT:
                    self.player.changespeed(3)
                if event.key == pygame.K_SPACE:
                    laser = Laser()
                    # pos de la nave + 45 px : center
                    laser.rect.x = self.player.rect.x + 45
                    laser.rect.y = self.player.rect.y - 40

                    self.laser_list.add(laser)
                    self.all_sprite_list.add(laser)
                    sound.play()
            
            #Logic Controller keyboard Arrows left and right
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.changespeed(3)
                if event.key == pygame.K_RIGHT:
                    self.player.changespeed(-3)

            
        # Orden Estricto: update, fill and sprite
        self.all_sprite_list.update()

        # Colisiones: iterar en la lista de los laseres
        for laser in self.laser_list:
            # "Condicion" (laser y la lista de meteoro)
            meteor_hit_list = pygame.sprite.spritecollide(laser, self.meteor_list, True)
            for meteor in meteor_hit_list:
                self.all_sprite_list.remove(laser)
                self.laser_list.remove(laser)
                score += 1
                print(score)
                if score >= max_score:
                    print('Has Salvado al mundo')
                    pygame.quit()
            # Liberacion de recursos de la maquina (laser al rebasar el limite de la screen)
            if laser.rect.y < -10 :
                self.all_sprite_list.remove(laser)
                self.laser_list.remove(laser)

    def display_frame(self, screen):
        screen.fill(WHITE)
        self.all_sprite_list.draw(screen)
        pygame.display.flip()

#Main
def main():
    pygame.init()

    SCREEN_WIDTH = 900
    SCREEN_HEIGHT = 600

    #Implements sound and keys
    #load sound : .ogg .wav .....
    sound = pygame.mixer.Sound(r'C:\Users\Jhon\Documents\Visual Studio Code\Python\AplicationPython\Shooter\laser5.ogg')

    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    clock = pygame.time.Clock()
    done = False
    max_score = 20
    score = 0
    game_over = False

    game = Game(max_score, SCREEN_WIDTH, SCREEN_HEIGHT)

    while not done:
        done = game.process_events()

        game.run_logic(sound, max_score)
        game.display_frame(screen)
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()
