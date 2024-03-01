import pygame
import random as r


# Classes
class Player():
    def __init__(self, position=pygame.Vector2(0, 0), color='', velocity=10, controls=[]):
        super().__init__()

        self.position = position
        self.velocity = velocity
        self.color = color

        self.controls = controls


    def update(self):
        self.draw()



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
        
        try:
            self.assets.rect = [self.position.x, self.position.y]
        except:
            ...




class AssetsModel(pygame.sprite.Sprite):
    def __init__(self, list_image, position, index=0):
        super().__init__()

        self.index = index

        self.list_image = list_image
        self.image = self.list_image[self.index]

        self.rect = [position[0], position[1]]




# funções úteis
def setPosition():
    return pygame.Vector2(r.randint(0, 800), r.randint(0, 500))


def colision_event():
    ...


    



if __name__ == '__main__':
    pygame.init() # Inicializando

    # variaveis de jogo
    largura_tela = 800
    altura_tela = 500

    fps = 60

    default_controls = [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d]
    player2_controls = [pygame.K_UP, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT]

    tela = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption('Aprendendo piá')
    pygame.display.set_icon(pygame.image.load('img/bird-up.png'))

    relogio = pygame.time.Clock()

    # objetos aqui
    player = Player(setPosition(), color='white', controls=default_controls)
    player2 = Player(setPosition(), color='blue', controls=player2_controls)

    running = True
    while running:# Rodando efetivamente o jogo
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

        # colisões
        if player.colisor.colliderect(player2.colisor):
            print('sim')


        pygame.display.flip() # atualizando os objetos

        relogio.tick(fps)

    pygame.quit()