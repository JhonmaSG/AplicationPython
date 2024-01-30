import pygame

def game_main():
    #Inicializamos un Motor
    pygame.init()
    #Dimensiones de la pantalla
    screen = pygame.display.set_mode((450,450))
    #Nombre de la ventana
    pygame.display.set_caption("Triqui by JhonmaSG")

    #Recursos graficos
    #Usar ruta completa O probar con abreviación
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

    def verificar_ganador():
        for i in range(3):
            if tablero[i][0] == tablero[i][1] == tablero[i][2] != '':
                return True #Horizontal
            if tablero[0][i] == tablero[1][i] == tablero[2][i] != '':
                return True #Vertical
        #Diagonal
        if tablero[0][0] == tablero[1][1] == tablero[2][2] != '':
            return True
        if tablero[0][2] == tablero[1][1] == tablero[2][0] != '':
            return True
        return False
    
    def verificar_tablero():
        cont = 0
        for i in range(3):
            for j in range(3):
                if tablero[i][j] != '':
                    cont += 1
        if cont == 9:
            return True
        return False

    while not game_over:
        clock.tick(30)  #30 FPS
        for event in pygame.event.get(): #Detección de un evento
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.MOUSEBUTTONDOWN: #Evento de un click Mouse
                mouseX, mouseY = event.pos
                #print(mouseX, mouseY)
                
                if (mouseX >= 40 and mouseX < 400) and \
                    (mouseY >= 35 and mouseY < 410):    #Limitación de rango Triqui
                    fila = (mouseY - 35) // 125
                    col = (mouseX - 40)  // 125
                    if tablero[fila][col] == '': # Si esta vacio, Agregar caracter del turno
                        tablero[fila][col] = turno
                        fin_juego = verificar_ganador()
                        reset_game = verificar_tablero()
                        if fin_juego:
                            print("El jugador (", turno, ") Ha ganado!")
                            game_over = True
                            return True
                        elif reset_game:
                            print("Empate!")
                            return False
                        turno = 'O' if turno == 'X' else 'X'    #Condicional Ternario, Cambio de Turno
        graficar_board()
        pygame.display.update()

reset_triqui = False
while not reset_triqui:
    reset_triqui = game_main()

pygame.quit()