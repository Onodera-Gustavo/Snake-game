import tkinter #biblioteca de interface gráfica do Usuário do python
import random #bilbioteca de randomização

COL = 25
ROWS = 25
TILESIZE = 25

WINDOW_WIDTH =  COL * TILESIZE
WINDOW_HEIGHT = ROWS * TILESIZE
#625px no total


class tile:
     def __init__(self, x, y):
          self.x = x
          self.y = y


# janela
window = tkinter.Tk() #abre a janela
window.title('Snake')
window.resizable(False, False) #imepde o redimensionamento
canvas = tkinter.Canvas(window, bg = "black", width= WINDOW_WIDTH, height= WINDOW_WIDTH, borderwidth= 0, highlightthickness= 0)
canvas.pack()
window.update()

#centralizar a janela

window_wid = window.winfo_width()
window_hei = window.winfo_height()
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()

window_x = int((screenwidth/2) - (window_wid/2))
window_y = int((screenheight/2) - (window_hei/2))

window.geometry(f"{window_wid}x{window_hei}+{window_x}+{window_y}"); #def pelas normas de codigo do .geometry

#iniciar o jogo // espaço dos argumentos globais 
snake = tile(5*TILESIZE, 5*TILESIZE) #125, 125px -- unico tile pra cabeça da cobra
food = tile(10*TILESIZE, 10*TILESIZE)
snake_body = [] #vários tiles
velocx = 0
velocy = 0
game_over = False
score = 0

def change_direction(e): #e = evento
     # print(e.keysym)
    global velocx, velocy, game_over
   
   
    if (e.keysym == "Up" and velocy != 1):
        velocx = 0
        velocy = -1
    elif (e.keysym == 'Down' and velocy != -1):
        velocx = 0
        velocy = 1
    elif (e.keysym == "Left" and velocx != 1):
        velocx = -1
        velocy = 0
    elif (e.keysym == 'Right' and velocx != -1):
        velocx = 1
        velocy = 0


def move():
    global snake, food, snake_body, game_over, score

    if (game_over):
        return
    
    if (snake.x < 0 or snake.x >= WINDOW_WIDTH or snake.y < 0 or snake.y >= WINDOW_HEIGHT):
        game_over = True
        return
    
    for tile1 in snake_body:
        if (snake.x == tile1.x and snake.y == tile1.y):
            game_over = True
            return

     #colisão
    if (snake.x == food.x and snake.y == food.y):
        snake_body.append(tile(food.x, food.y))
        food.x = random.randint(0, COL - 1) * TILESIZE
        food.y = random.randint(0, ROWS - 1) * TILESIZE
        score += 1

    #atulizar o corpo da snake
    for i in range(len(snake_body)-1, -1, -1):
        tile1 = snake_body[i]
        if (i == 0):
            tile1.x = snake.x
            tile1.y = snake.y
        else:
            prev_tile1 = snake_body[i-1]
            tile1.x = prev_tile1.x   
            tile1.y = prev_tile1.y #usei o 'tile1' pra não confundir a variável com a classe do começo do código 

    snake.x += velocx * TILESIZE
    snake.y += velocy * TILESIZE #verifica a posição da snake após sua colisão, caso for antes da colisão, a primeira food nãp será contada, apenas a partir da segunda, pois irá verificar a posição antes da food, que já tera uma armazenada.

    
def draw():

    global snake, food, snake_body, game_over, score #define que as próximas funções com 'snake' vão se referir a váriavel 'snake' anterior
    move()   

    canvas.delete("all")

     #desenhar a comida
    canvas.create_rectangle(food.x, food.y, food.x + TILESIZE, food.y + TILESIZE, fill= "SaddleBrown", outline= "white")

    for tile1 in snake_body:
        canvas.create_rectangle(tile1.x, tile1.y, tile1.x + TILESIZE, tile1.y + TILESIZE, fill= "purple", outline="white")

     #desenhar o corpo da snake
    canvas.create_rectangle(snake.x, snake.y, snake.x + TILESIZE, snake.y + TILESIZE, fill= "purple", outline= "pink")

    if(game_over):
        canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, font="comicsans 20", text= f"perdeu kkk fudido, seus ponto de bosta: {score}", fill="white")
    else:
        canvas.create_text(110, 20, font="comicsans 15", text= f"merdas comidas: {score}", fill="white")

    window.after(100, draw) #100ms = 10frames

    
draw()



window.bind("<KeyPress>", change_direction)
window.mainloop() #mantém a janela aberta



