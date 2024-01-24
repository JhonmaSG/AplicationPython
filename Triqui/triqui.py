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

while not game_over:
    clock.tick(30)  #30 FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos
            #print(mouseX, mouseY)
            if (mouseX >= 40 and mouseX < 400) and \
                (mouseY >= 35 and mouseY < 410):
                fila = (mouseY - 35) // 125
                col = (mouseX - 40)  // 125
                if tablero[fila][col] == '':
                    tablero[fila][col] = turno
                    turno = 'O' if turno == 'X' else 'X'
    graficar_board()
    pygame.display.update()

pygame.quit()