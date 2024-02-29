import pygame
import random as r

pygame.init() # Inicializando

# variaveis gerais
largura_tela = 800
altura_tela = 500

fps = 60

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Aprendendo piá')
pygame.display.set_icon(pygame.image.load('img/bird-up.png'))

relogio = pygame.time.Clock()

# Classes
class Player():
    def __init__(self, position=pygame.Vector2(0, 0), color='white', velocity=10, controls=[pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d]) -> None:
        self.position = position
        self.velocity = velocity
        self.color = color

        self.controls = controls

    def draw(self, format='circle'):
        if format == 'circle':
            self.colisor = pygame.draw.circle(tela, self.color, self.position, 40) # fazendo nosso player
        elif format == 'rect':
            self.colisor = pygame.draw.rect(tela, self.color, (self.position.x, self.position.y, 60, 60)) # fazendo nosso player


    def move(self):

        keys = pygame.key.get_pressed()
        if keys[self.controls[0]]:
            self.position.y -= self.velocity

        if keys[self.controls[1]]:
            self.position.x -= self.velocity

        if keys[self.controls[2]]:
            self.position.y += self.velocity

        if keys[self.controls[3]]:
            self.position.x += self.velocity



# funções úteis
def setPosition():
    return pygame.Vector2(r.randint(0, 800), r.randint(0, 500))

# objetos aqui
player = Player(setPosition())
player2 = Player(setPosition(), color='blue', controls=[pygame.K_UP, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT])
    




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    tela.fill('black')

    # desenhando objetos
    player.draw()
    player2.draw('rect')

    # movimentando o player
    player.move()
    player2.move()


    pygame.display.update() # atualizando os objetos

    relogio.tick(fps)

pygame.quit()