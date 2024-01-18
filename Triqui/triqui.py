import pygame
#Inicializamos un Motor
pygame.init()
#Dimensiones de la pantalla
screen = pygame.display.set_mode((450,450))
#Nombre de la ventana
pygame.display.set_caption("Triqui by JhonmaSG")

#Recursos graficos
#Usar ruta completa
fondo = pygame.image.load('C:/Users/Jhon/Documents/Visual Studio Code/Python/AplicationPython/Triqui/images/fondo.png')
circulo = pygame.image.load('C:/Users/Jhon/Documents/Visual Studio Code/Python/AplicationPython/Triqui/images/circle.png')
equis = pygame.image.load('C:/Users/Jhon/Documents/Visual Studio Code/Python/AplicationPython/Triqui/images/x.png')

#Escalar las imagenes
fondo = pygame.transform.scale(fondo,(450,450))
circulo = pygame.transform.scale(circulo,(100,100))
equis = pygame.transform.scale(equis,(100,100))

#Matriz Bidimensional
coor = [[(45,50),(175,50),(305,50)],
        [(45,180),(175,180),(305,180)],
        [(45,300),(175,300),(305,300)]]

tablero = [['','',''],
           ['','',''],
           ['','','']]

turno = 'X'
game_over = False
#Objeto .Clock
clock = pygame.time.Clock()

#Definicion de functions
def graficar_board():
    screen.blit(fondo, (0,0))
    for fila in range(3):
        for col in range(3):
            if tablero[fila][col] == 'X':
                dibujar_x(fila, col)
            elif tablero[fila][col] == 'O':
                dibujar_o(fila, col)

#Dibujar x , o
def dibujar_x(fila, col):
    # blit (Elemento a dibujar, coordenadas)
    screen.blit(equis, coor[fila][col])

def dibujar_o(fila, col):
    screen.blit(circulo, coor[fila][col])

#Definicion logica turns and X/Y
def add_XO(coor, tablero, to_move):
    position_pos = pygame.mouse.get_pos()
    #convertion Comming soon
    converted_x = (position_pos[0]-65)/835*2
    converted_y = position_pos[1]/835*2
    if coor[round(converted_y)][round(converted_x)] != 'O' and coor[round(converted_y)][round(converted_x)] != 'X':
        coor[round(converted_y)][round(converted_x)] = to_move
        if to_move == 'O':
            to_move = 'X'
        else:
            to_move = 'O'
    
def pos_mouse():
    return pygame.mouse.get_pos()

while not game_over:
    clock.tick(10)  #30 FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    print('PosMouse',pos_mouse())
    graficar_board()
    pygame.display.update()

pygame.quit()